from lingpy import *
from lingpy.compare.partial import Partial

def run(wordlist):
    
    cols = [c for c in wordlist.columns]
    part = Partial(wordlist)
    part.partial_cluster(
            ref="cogids", threshold=0.45, method="sca",
            cluster_method="upgma")
    part.add_cognate_ids("cogids", "cogid", idtype="strict")
    alms = Alignments(part, ref="cogids")
    alms.align()
    D = {0: cols+["cogids", "cogid", "alignment"]}
    for idx in alms:
        D[idx] = [alms[idx, h] for h in D[0]]
    return Wordlist(D)
