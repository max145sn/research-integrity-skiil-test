import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = r"C:\Users\MSX6389\.copilot\repos\copilot-worktrees\research-integrity-skiil-test\max145sn-redesigned-meme\trial\ai_usage_in_schools"
OUT = r"C:\Users\MSX6389\.copilot\repos\copilot-worktrees\research-integrity-skiil-test\max145sn-redesigned-meme\audit-output\eda_ai_schools_figs"
import os
os.makedirs(OUT, exist_ok=True)

df = pd.read_csv(BASE + r"\repo_data_fixed.csv")
df = df.drop(columns=[c for c in df.columns if c == ""])

# Recode missing code 999 -> NaN (applies broadly; some vars use 0 as "other/don't know" which we leave as-is)
df_num = df.replace(999, np.nan)

report_lines = []
def p(s=""):
    report_lines.append(str(s))

p("# EDA: AI Usage in Schools dataset")
p()
p(f"- Rows (respondents): {df.shape[0]}")
p(f"- Columns (variables): {df.shape[1]}")
p()

# ---- Missingness ----
miss = df_num.isna().mean().sort_values(ascending=False) * 100
p("## Missingness (top 15 variables, % coded 999/NaN)")
p("| Variable | % missing |")
p("|---|---|")
for k, v in miss.head(15).items():
    p(f"| {k} | {v:.1f}% |")
p()
p(f"Median missingness across all 174 variables: {miss.median():.1f}%. "
  f"{(miss==0).sum()} variables have zero missing values.")
p()

# ---- Demographics ----
p("## Demographics")
p(f"- Age: mean={df_num['Age'].mean():.2f}, sd={df_num['Age'].std():.2f}, "
  f"min={df_num['Age'].min():.0f}, max={df_num['Age'].max():.0f}, n={df_num['Age'].notna().sum()}")
gender_map = {1: "Man", 2: "Kvinna (Woman)", 3: "Annat (Other)", 4: "Prefer not to say"}
gc = df_num["Gender"].map(gender_map).value_counts(dropna=False)
p("- Gender distribution:")
for k, v in gc.items():
    p(f"  - {k}: {v} ({100*v/len(df):.1f}%)")
year_c = df_num["Year"].value_counts(dropna=False).sort_index()
p(f"- Year (grade level) distribution: {dict(year_c)}")
p(f"- {df_num['Programme'].nunique()} distinct school programmes reported.")
p(f"- Grade (self-reported avg grade, 1=A..5=E): mean={df_num['Grade'].mean():.2f}, sd={df_num['Grade'].std():.2f}")
p()

# Diagnosis prevalence (each Diagnosis_x is a 1=Yes/2=No checkbox)
diag_cols = [c for c in df.columns if c.startswith("Diagnosis_")]
p("## Self-reported diagnoses (% answering 'Yes')")
for c in diag_cols:
    yes_pct = (df_num[c] == 1).mean() * 100
    p(f"- {c}: {yes_pct:.1f}%")
p()

# ---- AI awareness & usage ----
known_cols = [c for c in df.columns if c.startswith("Known_AI_")]
used_cols = [c for c in df.columns if c.startswith("Used_AI_")]
p("## AI tool awareness vs. usage (% of respondents, Known vs Used)")
p("| Tool # | % know it | % have used it |")
p("|---|---|---|")
for kc, uc in zip(known_cols, used_cols):
    kp = (df_num[kc] == 1).mean() * 100
    up = (df_num[uc] == 1).mean() * 100
    p(f"| {kc.replace('Known_AI_','')} | {kp:.1f}% | {up:.1f}% |")
p()
p(f"- AI_Access (has access to AI tools): {(df_num['AI_Access']==1).mean()*100:.1f}% say yes (assuming 1=Yes)"
  if df_num['AI_Access'].dropna().isin([1,2]).all() else f"- AI_Access value counts: {dict(df_num['AI_Access'].value_counts())}")
p(f"- Use_school (uses AI for schoolwork) value counts: {dict(df_num['Use_school'].value_counts(dropna=False))}")
p(f"- Use_sparetime (uses AI in free time) value counts: {dict(df_num['Use_sparetime'].value_counts(dropna=False))}")
p()

# ---- Attitude / perception scales (5-point Likert style, 1..5, 6/999=don't know/missing) ----
attitude_cols = ["Society_pos","Society_neg","School_pos","School_neg","Learn_more","Learn_less",
                  "Affect_neg","Show_knowledge_neg","Show_knowledge_pos","Trust_neg",
                  "Increased_motivation"]
attitude_cols = [c for c in attitude_cols if c in df.columns]
p("## Attitude/perception item descriptives (scale ~1-5, higher = stronger agreement)")
p("| Item | Mean | SD | N valid |")
p("|---|---|---|---|")
for c in attitude_cols:
    s = df_num[c].replace(6, np.nan)  # 6 = "vet ej" (don't know) in many scales
    p(f"| {c} | {s.mean():.2f} | {s.std():.2f} | {s.notna().sum()} |")
p()

# ---- Composite / derived factor scores (last columns) ----
factor_cols = ["Use_F","P_AI","AI_P","AI_S","S_AI","AI_K","T_AI_W","T_AI_U","gender_binary"]
factor_cols = [c for c in factor_cols if c in df.columns]
p("## Derived composite/factor score descriptives")
p("| Factor | Mean | SD | Min | Max | N valid |")
p("|---|---|---|---|---|---|")
for c in factor_cols:
    if c == "gender_binary":
        continue
    s = pd.to_numeric(df_num[c], errors="coerce")
    p(f"| {c} | {s.mean():.2f} | {s.std():.2f} | {s.min():.2f} | {s.max():.2f} | {s.notna().sum()} |")
p()
p(f"- gender_binary (categorical, derived from Gender): {dict(df['gender_binary'].value_counts(dropna=False))}")
p()

# ---- Correlation matrix among factor scores ----
fc_numeric = [c for c in factor_cols if c != "gender_binary"]
corr = df_num[fc_numeric + ["Age"]].apply(pd.to_numeric, errors="coerce").corr()
p("## Correlation matrix (composite factors + Age)")
p(corr.round(2).to_markdown())
p()

fig, ax = plt.subplots(figsize=(7,6))
im = ax.imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
ax.set_xticks(range(len(corr.columns))); ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticks(range(len(corr.columns))); ax.set_yticklabels(corr.columns)
for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", fontsize=7)
plt.colorbar(im, ax=ax, shrink=0.8)
plt.title("Correlation: composite factor scores")
plt.tight_layout()
plt.savefig(OUT + r"\correlation_heatmap.png", dpi=130)
plt.close()

# ---- Distribution plots ----
fig, axes = plt.subplots(1, 3, figsize=(13,4))
df_num["Age"].dropna().plot(kind="hist", bins=15, ax=axes[0], color="steelblue")
axes[0].set_title("Age distribution"); axes[0].set_xlabel("Age")
gc.plot(kind="bar", ax=axes[1], color="darkorange")
axes[1].set_title("Gender"); axes[1].tick_params(axis='x', rotation=30)
df_num["Use_F"].dropna().plot(kind="hist", bins=15, ax=axes[2], color="seagreen")
axes[2].set_title("Use_F (AI use frequency factor)")
plt.tight_layout()
plt.savefig(OUT + r"\distributions.png", dpi=130)
plt.close()

# ---- Use by gender / diagnosis ----
p("## AI use (Use_F factor score) by subgroup")
by_gender = df_num.groupby(df_num["Gender"].map(gender_map))["Use_F"].agg(["mean","std","count"])
p("### By gender")
p(by_gender.round(2).to_markdown())
p()

any_diag = (df_num[diag_cols[:-2]] == 1).any(axis=1)  # exclude "none of the above" / "prefer not" cols
by_diag = df_num.assign(any_diagnosis=any_diag).groupby("any_diagnosis")["Use_F"].agg(["mean","std","count"])
p("### By any self-reported diagnosis (excluding 'none'/'prefer not to say' options)")
p(by_diag.round(2).to_markdown())
p()

with open(r"C:\Users\MSX6389\.copilot\repos\copilot-worktrees\research-integrity-skiil-test\max145sn-redesigned-meme\audit-output\eda_ai_usage_in_schools.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("DONE")
print(df.dtypes.value_counts())
