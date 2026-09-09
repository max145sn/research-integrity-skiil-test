"""
Independent recomputation of the R0 function from pcbi.1007945.s001.Rmd
(S1 File of Ayala & Villela 2020, PLOS Comp Biol pcbi.1007945).

This is a faithful line-by-line translation of the R `R0()` function (not a
copy-paste execution of the R code itself) into Python/NumPy, used to:
  (a) confirm the formula is implemented as described, and
  (b) quantify the numerical impact of the two parameter discrepancies found
      between the manuscript's Table 1 and the code's fixed parameter vectors
      (Nh: 624 vs 625; phit for P. vivax: 0.29 vs 0.21).

Parameter indices follow the R code's 1-based comment exactly:
(1) Nm, (2) Nh, (3) a, (4) b, (5) mm, (6) alpha, (7) cs, (8) ca, (9) sigma,
(10) psi, (11) mvl, (12) phit, (13) phiu, (14) varphi, (15) epsilon, (16) nu,
(17) n, (18) gamma, (19) r
"""
import numpy as np
import json

def R0(par):
    # par is 1-indexed conceptually; store as 0-indexed list, p[i-1] == par[i]
    p = par
    n = np.arange(0, 1.0001, 0.01)
    Nm, Nh, a, b, mm, alpha, cs, ca, sigma = p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]
    psi, mvl, phit, phiu, varphi, epsilon, nu, nrec, gamma, r = p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18]

    R0s = np.sqrt(
        (Nm / Nh * a**2 * b * (psi + mvl) *
         (cs * sigma + ca * (1 - sigma) + n * sigma * gamma * cs * epsilon * (1 - nu) * (1 - varphi)))
        /
        (mm * (((1 - n * sigma) * r + n * sigma * gamma) * (psi + mvl)
               - psi * ((1 - varphi) * n * sigma * gamma * phit + (1 - n * sigma) * phiu * r)))
    )
    R0r = (1 - alpha) * np.sqrt(
        (Nm / Nh * a**2 * b * (psi + mvl) *
         (cs * sigma + ca * (1 - sigma) + n * sigma * gamma * cs * epsilon * (1 - varphi)))
        /
        (mm * (((1 - n * sigma) * r + n * sigma * gamma / (nrec + 1)) * (psi + mvl)
               - psi * ((1 - varphi) * n * sigma * gamma * phit / (nrec + 1) + (1 - n * sigma) * phiu * r)))
    )
    return n, R0s, R0r


def relative_diff(a, b):
    # elementwise relative diff, safe against div by ~0
    denom = np.where(np.abs(b) > 1e-12, b, np.nan)
    return (a - b) / denom


results = {}

# --- P. vivax vector as supplied in code (baseline) ---
# order: Nm,Nh,a,b,mm,alpha,cs,ca,sigma,psi,mvl,phit,phiu,varphi,epsilon,nu,n,gamma,r
parv_code = [2435, 624, 0.21, 0.5, 0.033, 0.28, 0.4, 0.12, 0.33, 1/60, 1/425, 0.29, 0.9, 0.5, 2.1, 1/10**12, 1, 1/9, 1/60]
# --- P. vivax vector with manuscript Table 1 values substituted (Nh=625, phit=0.21) ---
parv_manuscript = list(parv_code)
parv_manuscript[1] = 625      # Nh
parv_manuscript[11] = 0.21    # phit

n_c, R0s_c, R0r_c = R0(parv_code)
n_m, R0s_m, R0r_m = R0(parv_manuscript)

results['vivax_R0s_code'] = R0s_c.tolist()
results['vivax_R0s_manuscript_values'] = R0s_m.tolist()
results['vivax_R0r_code'] = R0r_c.tolist()
results['vivax_R0r_manuscript_values'] = R0r_m.tolist()

diff_s = relative_diff(R0s_c, R0s_m)
diff_r = relative_diff(R0r_c, R0r_m)

summary = {
    "vivax_R0_sensitive": {
        "max_abs_relative_diff_pct": float(np.nanmax(np.abs(diff_s)) * 100),
        "mean_abs_relative_diff_pct": float(np.nanmean(np.abs(diff_s)) * 100),
        "at_n0_code": float(R0s_c[0]), "at_n0_manuscript": float(R0s_m[0]),
        "at_n1_code": float(R0s_c[-1]), "at_n1_manuscript": float(R0s_m[-1]),
    },
    "vivax_R0_resistant": {
        "max_abs_relative_diff_pct": float(np.nanmax(np.abs(diff_r)) * 100),
        "mean_abs_relative_diff_pct": float(np.nanmean(np.abs(diff_r)) * 100),
        "at_n0_code": float(R0r_c[0]), "at_n0_manuscript": float(R0r_m[0]),
        "at_n1_code": float(R0r_c[-1]), "at_n1_manuscript": float(R0r_m[-1]),
    },
}

# --- isolate each discrepancy's individual effect (P. vivax) ---
parv_nh_only = list(parv_code); parv_nh_only[1] = 625
parv_phit_only = list(parv_code); parv_phit_only[11] = 0.21

_, R0s_nh, R0r_nh = R0(parv_nh_only)
_, R0s_phit, R0r_phit = R0(parv_phit_only)

summary["isolated_Nh_effect_R0s_max_relative_diff_pct"] = float(np.nanmax(np.abs(relative_diff(R0s_c, R0s_nh))) * 100)
summary["isolated_phit_effect_R0s_max_relative_diff_pct"] = float(np.nanmax(np.abs(relative_diff(R0s_c, R0s_phit))) * 100)
summary["isolated_Nh_effect_R0r_max_relative_diff_pct"] = float(np.nanmax(np.abs(relative_diff(R0r_c, R0r_nh))) * 100)
summary["isolated_phit_effect_R0r_max_relative_diff_pct"] = float(np.nanmax(np.abs(relative_diff(R0r_c, R0r_phit))) * 100)

# --- falciparum vector: only Nh differs (624 vs 625); phit/phiu/psi/mvl are zeroed
# (no hypnozoite compartment) so those terms are inapplicable to falciparum ---
parf_code = [2435, 624, 0.21, 0.5, 0.033, 0.28, 0.4, 0.12, 0.9, 0, 1, 0, 0, 0.5, 11, 1/10**12, 1, 1/2, 1/287]
parf_manuscript = list(parf_code); parf_manuscript[1] = 625

_, R0s_fc, R0r_fc = R0(parf_code)
_, R0s_fm, R0r_fm = R0(parf_manuscript)

summary["falciparum_R0s_Nh_effect_max_relative_diff_pct"] = float(np.nanmax(np.abs(relative_diff(R0s_fc, R0s_fm))) * 100)
summary["falciparum_R0r_Nh_effect_max_relative_diff_pct"] = float(np.nanmax(np.abs(relative_diff(R0r_fc, R0r_fm))) * 100)

print(json.dumps(summary, indent=2))

with open("recompute_results.json", "w") as f:
    json.dump({"summary": summary, "curves": results}, f, indent=2)
