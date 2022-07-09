from lingpy import *
from cltoolkit import Wordlist as CLWL
from pycldf import Dataset
from pyclts import CLTS
from lexibase.lexibase import LexiBase
from lingpy.compare.partial import Partial

bipa = CLTS().bipa

wl = CLWL(
        [
            Dataset.from_metadata("cldf-dataset/hubercolumbian/cldf/cldf-metadata.json"),
            Dataset.from_metadata("../cldf/cldf-metadata.json")],
        ts=bipa)
gcodes = "desa1247,siri1274,tani1257".split(",")
D = {0: [
    "concept", "concept_in_source", "dataset", "language", "glottocode", 
    "value", "form", "tokens", "lid"]}
idx = 1
for language in wl.languages:
    if language.dataset == "kochtukanoan" or language.glottocode in gcodes:
        if language.dataset == "kochtukanoan":
            pref = "K-"
        else:
            pref = "H-"
        for form in language.forms:
            D[idx] = [
                    form.concept.name if form.concept else form.sense.name,
                    form.sense.name,
                    form.dataset,
                    pref+form.language.name,
                    form.language.glottocode,
                    form.value,
                    form.form,
                    form.sounds,
                    form.id]
            idx += 1
headers = [h for h in D[0]]+["cogids", "alignment"]
lex = Partial(D)
lex.cluster(method="sca", ref="cogids", threshold=0.45)

lex.output('tsv', filename="wordlist", ignore="all", prettify=False,
        columns=headers)

lex = LexiBase("wordlist.tsv", dbase="mottatukano.sqlite3")
lex.create("mottatukano")
