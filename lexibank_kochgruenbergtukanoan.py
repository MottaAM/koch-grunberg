import pathlib
import attr
from clldutils.misc import slug
from pylexibank import Dataset as BaseDataset
from pylexibank import progressbar as pb
from pylexibank import Concept, Lexeme
from pylexibank import FormSpec


#@attr.s
#class CustomLanguage(Language):
#    Sources = attr.ib(default=None)

@attr.s
class CustomConcept(Concept):
    Portuguese_Gloss = attr.ib(default=None)
    German_Gloss = attr.ib(default=None)


#@attr.s
#class CustomLexeme(Lexeme):
#    Page = 


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "kochgruenbergtukanoan"
    concept_class = CustomConcept
    form_spec = FormSpec(
            separators="~;,/", missing_data=[], first_form_only=True,
            replacements=[(" ", "_")])

    def cmd_makecldf(self, args):
        # add bib
        args.writer.add_sources()
        args.log.info("added sources")

        # add concept
        concepts = {}
        for concept in self.concepts:
            idx = concept["NUMBER"]+"_"+slug(concept["ENGLISH"])
            concepts[concept["GERMAN"]] = idx
            args.writer.add_concept(
                    ID=idx,
                    Name=concept["ENGLISH"],
                    German_Gloss=concept["GERMAN"],
                    Portuguese_Gloss=concept["PORTUGUESE"],
                    #Concepticon_ID=concept["CONCEPTICON_ID"],
                    #Concepticon_Gloss=concept["CONCEPTICON_GLOSS"],
                    )
        args.log.info("added concepts")
        # add language
        languages = args.writer.add_languages()
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
                                Source="KochGrünberg2014[{0}]".format(row["Pagina"])
                                )
                    else:
                        errors.add(("concept missing", row["Alemão"]))
        for a, b in errors:
            print(a, b)

