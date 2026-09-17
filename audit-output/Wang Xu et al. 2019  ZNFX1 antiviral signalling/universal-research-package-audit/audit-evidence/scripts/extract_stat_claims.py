import re, sys
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
out = open(sys.argv[2], "w", encoding="utf-8")
pat = re.compile(r"(n\s*=\s*\d+|P\s*[<=>]\s*0?\.\d+|P\s*[<=>]\s*\d|two-tailed|Student|t-test|ANOVA|log-rank|Mann-Whitney|mean\s*\xb1|s\.e\.m|s\.d\.|biological replicate|independent experiment|Source Data)", re.I)
for i, l in enumerate(lines, 1):
    if pat.search(l):
        out.write(f"{i}: {l.strip()}\n")
out.close()
