import json, sys, itertools
import numpy as np
from scipy import stats
sd = sys.argv[1]; recs = []
def rec(**kw): recs.append(kw)

# --- CALC-001/002: Fig 2h VSV & EMCV, wt vs Znfx1-/-, vs workbook-stored p-values
f2 = {
 "VSV":  ([1645.1134584,1819.3239154,1389.8948452],[5197.2435706,6954.1226332,4753.3331206], 0.004186885624489595, "E53"),
 "EMCV": ([543.3221987,432.6434711,662.3130688],[2580.6415624,2142.8244013,1842.6429847], 0.0018500638904232246, "I53"),
}
for k,(wt,ko,stored,cell) in f2.items():
    t,p = stats.ttest_ind(wt,ko,equal_var=True)
    tw,pw = stats.ttest_ind(wt,ko,equal_var=False)
    rec(id=f"CALC-{k}-2h", panel="Fig 2h", comparison=f"wt vs Znfx1-/- ({k})",
        n_per_group=[len(wt),len(ko)], stored_p=stored, stored_cell=f"Source Data Fig 2.xlsx!Sheet1!{cell}",
        recomputed_p_student=float(p), recomputed_p_welch=float(pw), t=float(t),
        match_student=bool(abs(p-stored)<1e-9), match_welch=bool(abs(pw-stored)<1e-9))

# --- CALC-003: Fig 2h H1N1/HSV-1 replicate count vs legend n=3
rec(id="CALC-2h-n", panel="Fig 2h", check="replicate rows deposited per arm",
    block1_rows=3, block1_range="Source Data Fig 2.xlsx!Sheet1!B50:I52",
    block2_rows=4, block2_range="Source Data Fig 2.xlsx!Sheet1!B57:I60",
    legend_statement="For d,e,h-j, n = 3 independent experiments (manuscript_extracted.txt:910)")

# --- CALC-004: Fig 7g deposited group coverage + recompute of the ONLY deposited contrast
ifnb_ev=[1,1,1]; ifnb_vsv=[2.5162746,3.8974682,4.1240736]
ifit_ev=[1,1,1]; ifit_vsv=[2.7416836,2.6563682,1.9548904]
for nm,ev,vsv in (("IFNB1",ifnb_ev,ifnb_vsv),("IFIT1",ifit_ev,ifit_vsv)):
    t,p = stats.ttest_ind(ev,vsv,equal_var=True)
    rec(id=f"CALC-7g-{nm}", panel="Fig 7g", comparison="EV vs EV+VSV (the only two deposited columns)",
        deposited_columns=["EV","EV+VSV"], figure_groups_shown=["EV","ZNFX1","EV+VSV","ZNFX1+VSV"],
        n_per_group=[3,3], ev_variance=float(np.var(ev,ddof=1)),
        recomputed_p=float(p), t=float(t),
        printed_panel_p=["0.0004 (manuscript_extracted.txt:2463)","0.0001 (manuscript_extracted.txt:2464)"],
        mapping_note="Printed P values plausibly compare +VSV arms with vs without ZNFX1; those ZNFX1 arms are NOT deposited, so the printed P cannot be attributed to the deposited contrast.")

# --- CALC-005: Fig 3f survival, legend n=10 vs deposited counts
wt=[5,5,5,5,5,5,5,5,3,3]; ko=[5,5,5,5,2,2,1,1,1,1]
rec(id="CALC-3f-n", panel="Fig 3f", check="survival denominators",
    deposited_series_wt=wt, deposited_series_ko=ko,
    max_at_risk_wt=max(wt), max_at_risk_ko=max(ko),
    legend_statement="n = 10 mice per group (manuscript_extracted.txt:1083)",
    alt_tested=["series read as number at risk (max 5)","series read as percent (values are integers 1-5, not 0-100)","two pooled cohorts of 5 (would require a second undeposited cohort)"])
# reconstruct events from at-risk series and run Gehan-Breslow-Wilcoxon-analogous log-rank
def events(series):
    out=[]; 
    for i in range(1,len(series)):
        d=series[i-1]-series[i]
        for _ in range(d): out.append(i)
    cens=[len(series)-1]*series[-1]
    return out,cens
ew,cw=events(wt); ek,ck=events(ko)
rec(id="CALC-3f-events", panel="Fig 3f", reconstructed_deaths_wt=ew, censored_wt=len(cw),
    reconstructed_deaths_ko=ek, censored_ko=len(ck),
    note="Reconstruction assumes the series is number-at-risk at 10 successive timepoints; timepoint units are not deposited.")

# --- CALC-006: Fig 1f/1g sample counts vs legend
rec(id="CALC-1f-n", panel="Fig 1f/1g", check="clinical sample counts",
    fig1f_healthy_n=9, fig1f_treated_n=14, fig1g_n_per_col=18,
    legend_statement="n = 9 uninfected controls, n = 14 HIV (manuscript_extracted.txt:594); n = 18 independent samples (manuscript_extracted.txt:596)",
    result="counts in deposited columns equal the legend-stated n")

# --- CALC-007: Fig 7c label correspondence + outlier screen
g=[45514.8509464,42552.9712536,4176.8590572]
rec(id="CALC-7c-labels", panel="Fig 7c",
    legend_statement="in wild-type or Mda5-/- A549 cells (manuscript_extracted.txt:2537)",
    deposited_row_labels=["Rig-i -/-","Mda5 -/-"],
    outlier_cell="Source Data Fig 7.xlsx!Sheet1!G40", outlier_value=g[2],
    sibling_values=g[:2], ratio_to_sibling_mean=float(np.mean(g[:2])/g[2]))
json.dump(recs, open(sys.argv[2],"w",encoding="utf-8"), indent=2)
for r in recs: print(json.dumps(r))
