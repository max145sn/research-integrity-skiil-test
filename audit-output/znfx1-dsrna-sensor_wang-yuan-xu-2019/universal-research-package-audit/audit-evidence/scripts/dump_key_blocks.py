import openpyxl, sys
from pathlib import Path
sd = Path(sys.argv[1]); out=open(sys.argv[2],"w",encoding="utf-8")
def blk(fn, rng, label):
    ws = openpyxl.load_workbook(sd/fn, data_only=True).active
    out.write(f"--- {label} [{fn}!{rng}]\n")
    for row in ws[rng]:
        out.write("   " + " | ".join(f"{c.coordinate}={c.value}" for c in row) + "\n")
blk("Source Data Fig 2.xlsx","B48:I53","Fig2h block1 VSV/EMCV + p-value row")
blk("Source Data Fig 2.xlsx","B55:I60","Fig2h block2 H1N1/HSV-1")
blk("Source Data Fig 7.xlsx","H61:K67","Fig7g IFNB1/IFIT1")
blk("Source Data Fig 7.xlsx","H47:K58","Fig7e")
blk("Source Data Fig 3.xlsx","A31:C41","Fig3f survival")
blk("Source Data Fig 1.xlsx","B26:K45","Fig1f/1g clinical samples")
blk("Source Data Fig 7.xlsx","B38:K43","Fig7c genotypes")
out.close()
