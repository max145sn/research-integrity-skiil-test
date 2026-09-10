import pandas as pd, numpy as np
from scipy import stats
import statsmodels.formula.api as smf

df = pd.read_csv('results/Data.csv', skiprows=[1, 2])
print('rows:', len(df))

recode_map = {7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
df['MLQ_5r'] = df['MLQ_5'].map(recode_map)
df['mil'] = df[['MLQ_1', 'MLQ_2', 'MLQ_3', 'MLQ_4', 'MLQ_5r']].mean(axis=1, skipna=True)
df['epa'] = df[['EA_1', 'EA_3', 'EA_5']].mean(axis=1, skipna=True)
df['ena'] = df[['EA_2', 'EA_4']].mean(axis=1, skipna=True)
df['check'] = df['MLQ_6']
df['cond'] = np.where(df['RO-BR-FL_9'] == 'Coherent', 0, 1)

print('check value counts:', df['check'].value_counts(dropna=False).to_dict())
df['checkbin'] = np.where(df['check'] != 1, 1, 0)
clean = df[df['checkbin'] == 0].copy()
print('final n:', len(clean))
print(clean['cond'].value_counts())

print(clean.groupby('cond')[['mil', 'epa', 'ena']].agg(['mean', 'std', 'count']))

g0 = clean[clean['cond'] == 0]['mil']
g1 = clean[clean['cond'] == 1]['mil']
t, p = stats.ttest_ind(g0, g1, equal_var=True)
n0, n1 = len(g0), len(g1)
print('t-test mil: t=', t, 'p=', p, 'df=', n0 + n1 - 2)

sd0 = g0.std(ddof=1)
sd1 = g1.std(ddof=1)
pooled_var = ((n0 - 1) * sd0 ** 2 + (n1 - 1) * sd1 ** 2) / (n0 + n1 - 2)
pooled_sd = np.sqrt(pooled_var)
d = (g0.mean() - g1.mean()) / pooled_sd
print('cohen d:', d)

model = smf.ols('mil ~ cond + epa + ena', data=clean).fit()
print(model.summary())
