import math
from statistics import mean, stdev

def welch(a, b):
    na, nb = len(a), len(b)
    ma, mb = mean(a), mean(b)
    va, vb = stdev(a) ** 2, stdev(b) ** 2
    se2 = va / na + vb / nb
    t = (ma - mb) / math.sqrt(se2)
    df = se2 ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
    return t, df

def student(a, b):
    na, nb = len(a), len(b)
    ma, mb = mean(a), mean(b)
    sp2 = ((na - 1) * stdev(a) ** 2 + (nb - 1) * stdev(b) ** 2) / (na + nb - 2)
    t = (ma - mb) / math.sqrt(sp2 * (1 / na + 1 / nb))
    return t, na + nb - 2

def pval(t, df):
    # two-sided p from t via incomplete beta
    x = df / (df + t * t)
    return betainc(df / 2, 0.5, x)

def betacf(a, b, x):
    MAXIT, EPS, FPMIN = 200, 3e-16, 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    if abs(d) < FPMIN: d = FPMIN
    d = 1 / d; h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1 / d; h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1 / d; de = d * c; h *= de
        if abs(de - 1) < EPS: break
    return h

def betainc(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lbeta) * betacf(a, b, x) / a
    return 1 - math.exp(lbeta) * betacf(b, a, 1 - x) / b

blocks = {
 "Fig 2h VSV  wt vs Znfx1-/- (stated p=0.004187)": (
    [1645.113458, 1819.323915, 1389.894845], [5197.243571, 6954.122633, 4753.333121], 0.004187),
 "Fig 2h EMCV wt vs Znfx1-/- (stated p=0.00185)": (
    [543.322199, 432.643471, 662.313069], [2580.641562, 2142.824401, 1842.642985], 0.00185),
 "Fig 2h H1N1 wt vs Znfx1-/- (no p stated)": (
    [425.33483, 586.246242, 571.476816, 412.758586],
    [1479.365436, 1292.843775, 1452.854368, 1198.644796], None),
 "Fig 2h HSV-1 wt vs Znfx1-/- (no p stated)": (
    [7129.862657, 6653.135659, 4439.759703, 6989.423686],
    [9512.427304, 5987.132277, 7218.425002, 7285.074946], None),
}

for name, (a, b, stated) in blocks.items():
    ts, dfs = student(a, b)
    tw, dfw = welch(a, b)
    ps, pw = pval(ts, dfs), pval(tw, dfw)
    print(f"{name}")
    print(f"   wt   n={len(a)} mean={mean(a):.2f} sd={stdev(a):.2f}")
    print(f"   KO   n={len(b)} mean={mean(b):.2f} sd={stdev(b):.2f}   fold={mean(b)/mean(a):.2f}")
    print(f"   Student t={ts:.4f} df={dfs} p={ps:.6f}")
    print(f"   Welch   t={tw:.4f} df={dfw:.2f} p={pw:.6f}")
    if stated:
        print(f"   stated p={stated}  -> Student {'MATCH' if abs(ps-stated)<5e-5 else 'no match'}; "
              f"Welch {'MATCH' if abs(pw-stated)<5e-5 else 'no match'}")
    print()
