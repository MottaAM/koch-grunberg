import pathlib
import attr
from clldutils.misc import slug
from pylexibank import Dataset as BaseDataset
from pylexibank import Concept
from pylexibank import FormSpec


@attr.s
class CustomConcept(Concept):
    Portuguese_Gloss = attr.ib(default=None)
    German_Gloss = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "kochtukanoan"
    concept_class = CustomConcept
    form_spec = FormSpec(
            separators="~;,/", missing_data=[], first_form_only=True,
            replacements=[(" ", "_")])

    def cmd_makecldf(self, args):
        # add bib
        args.writer.add_sources()
        args.log.info("added sources")

        # modify replacements
        # reps = self.raw_dir.read_csv("preprocess-sounds.tsv", delimiter="\t", dicts=True)
        # for row in reps:
        #     self.form_spec.replacements += [(row["KG"], row["IPA"])]
        # args.log.info(self.form_spec.replacements)

        # add concept
        concepts = {}
        for concept in self.conceptlists[0].concepts.values():
            idx = concept.id.split("-")[-1] + "_" + slug(concept.gloss)
            concepts[concept.attributes["german"]] = idx
            args.writer.add_concept(
                ID=idx,
                Name=concept.gloss,
                German_Gloss=concept.attributes["german"],
                Portuguese_Gloss=concept.attributes["portuguese"],
                Concepticon_ID=concept.concepticon_id,
                Concepticon_Gloss=concept.concepticon_gloss,
            )

        args.log.info("added concepts")
        # add language
        args.writer.add_languages()
        args.log.info("added languages")

        # read in data
        data = self.raw_dir.read_csv(
            "koch-grunberg koretu yahuna yupua - Tabela unificada.csv",
            delimiter=",",
            dicts=True
        )
        errors = set()
        for row in data:
            for language in ["Desano", "Yupua", "Yahuna", "Koretu"]:
                entry = row[language]
                if entry.strip():
                    if row["Alemão"] in concepts:
                        args.writer.add_forms_from_value(
                                Language_ID=language,
                                Parameter_ID=concepts[row["Alemão"]],
                                Value=entry,
                                Source=f"Koch1914[{row["Pagina"]}]"
                                )
                    else:
                        errors.add(("concept missing", row["Alemão"]))
        for a, b in errors:
            print(a, b)
