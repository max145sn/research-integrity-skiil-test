# EDA: AI Usage in Schools dataset

- Rows (respondents): 1266
- Columns (variables): 174

## Missingness (top 15 variables, % coded 999/NaN)
| Variable | % missing |
|---|---|
| Years_in_swedish_school | 93.8% |
| S_tips_relating_to_diagnosis | 82.7% |
| S_AI_helps_difficulties | 82.6% |
| Why_not_AI_5 | 55.3% |
| Why_not_AI_4 | 55.3% |
| Why_not_AI_2 | 55.3% |
| Why_not_AI_1 | 55.3% |
| Why_not_AI_3 | 55.3% |
| Why_not_AI_6 | 55.3% |
| Why_not_AI_7 | 55.3% |
| What_start_using_AI_3 | 55.0% |
| What_start_using_AI_2 | 55.0% |
| What_start_using_AI_5 | 55.0% |
| What_start_using_AI_4 | 55.0% |
| What_start_using_AI_1 | 55.0% |

Median missingness across all 174 variables: 0.6%. 83 variables have zero missing values.

## Demographics
- Age: mean=17.01, sd=0.86, min=15, max=20, n=1266
- Gender distribution:
  - Kvinna (Woman): 746 (58.9%)
  - Man: 491 (38.8%)
  - Prefer not to say: 16 (1.3%)
  - Annat (Other): 13 (1.0%)
- Year (grade level) distribution: {0: np.int64(11), 1: np.int64(672), 2: np.int64(462), 3: np.int64(121)}
- 18 distinct school programmes reported.
- Grade (self-reported avg grade, 1=A..5=E): mean=2.26, sd=1.07

## Self-reported diagnoses (% answering 'Yes')
- Diagnosis_1: 2.4%
- Diagnosis_2: 3.6%
- Diagnosis_3: 6.6%
- Diagnosis_4: 0.2%
- Diagnosis_5: 3.7%
- Diagnosis_6: 3.5%
- Diagnosis_8: 4.8%
- Diagnosis_9: 56.9%
- Diagnosis_10: 10.5%

## AI tool awareness vs. usage (% of respondents, Known vs Used)
| Tool # | % know it | % have used it |
|---|---|---|
| 1 | 96.1% | 79.2% |
| 2 | 20.0% | 10.5% |
| 3 | 4.3% | 2.5% |
| 4 | 2.8% | 0.6% |
| 5 | 13.0% | 3.3% |
| 6 | 8.7% | 2.1% |
| 7 | 4.6% | 1.2% |
| 8 | 2.1% | 0.9% |
| 9 | 0.9% | 0.4% |
| 10 | 3.4% | 1.0% |
| 11 | 78.0% | 57.3% |
| 12 | 3.5% | 1.4% |
| 13 | 11.1% | 4.4% |
| 14 | 6.2% | 2.1% |
| 15 | 14.3% | 3.7% |
| 16 | 8.7% | 2.9% |
| 17 | 15.2% | 5.9% |
| 18 | 9.7% | 4.0% |
| 19 | 6.5% | 2.2% |
| 20 | 2.8% | 0.6% |
| 21 | 2.3% | 10.4% |
| 22 | 3.4% | 3.1% |

- AI_Access value counts: {2.0: np.int64(819), 4.0: np.int64(165), 0.0: np.int64(131), 5.0: np.int64(81), 3.0: np.int64(40), 1.0: np.int64(29)}
- Use_school (uses AI for schoolwork) value counts: {3.0: np.int64(323), 2.0: np.int64(309), 4.0: np.int64(285), 1.0: np.int64(266), 5.0: np.int64(47), 0.0: np.int64(31), nan: np.int64(5)}
- Use_sparetime (uses AI in free time) value counts: {2.0: np.int64(439), 3.0: np.int64(296), 1.0: np.int64(287), 4.0: np.int64(162), 0.0: np.int64(35), 5.0: np.int64(33), nan: np.int64(14)}

## Attitude/perception item descriptives (scale ~1-5, higher = stronger agreement)
| Item | Mean | SD | N valid |
|---|---|---|---|
| Society_pos | 2.98 | 1.28 | 1266 |
| Society_neg | 3.17 | 1.26 | 1266 |
| School_pos | 2.96 | 1.40 | 1266 |
| School_neg | 2.18 | 1.24 | 1266 |
| Learn_more | 2.88 | 1.41 | 1266 |
| Learn_less | 2.18 | 1.32 | 1266 |
| Affect_neg | 2.18 | 1.34 | 1266 |
| Show_knowledge_neg | 2.74 | 1.58 | 1266 |
| Show_knowledge_pos | 2.26 | 1.35 | 1266 |
| Trust_neg | 3.72 | 1.43 | 1266 |
| Increased_motivation | 2.42 | 1.36 | 1000 |

## Derived composite/factor score descriptives
| Factor | Mean | SD | Min | Max | N valid |
|---|---|---|---|---|---|
| Use_F | 4.85 | 2.06 | 0.00 | 10.00 | 1247 |
| P_AI | -0.00 | 0.97 | -2.55 | 2.19 | 1266 |
| AI_P | -0.00 | 1.06 | -2.66 | 2.13 | 1266 |
| AI_S | -0.00 | 1.08 | -2.42 | 2.58 | 1266 |
| S_AI | -0.00 | 1.15 | -2.15 | 2.80 | 1266 |
| AI_K | -0.00 | 0.94 | -1.66 | 1.72 | 1266 |
| T_AI_W | 0.00 | 0.72 | -2.73 | 1.21 | 1266 |
| T_AI_U | -0.00 | 0.80 | -2.18 | 1.68 | 1266 |

- gender_binary (categorical, derived from Gender): {'female': np.int64(746), 'male': np.int64(491), nan: np.int64(29)}

## Correlation matrix (composite factors + Age)
|        |   Use_F |   P_AI |   AI_P |   AI_S |   S_AI |   AI_K |   T_AI_W |   T_AI_U |   Age |
|:-------|--------:|-------:|-------:|-------:|-------:|-------:|---------:|---------:|------:|
| Use_F  |    1    |   0.78 |   0.71 |   0.57 |   0.27 |   0.31 |     0.11 |     0.34 | -0.04 |
| P_AI   |    0.78 |   1    |   0.96 |   0.78 |   0.39 |   0.51 |     0.2  |     0.51 | -0.04 |
| AI_P   |    0.71 |   0.96 |   1    |   0.82 |   0.39 |   0.46 |     0.21 |     0.44 | -0.03 |
| AI_S   |    0.57 |   0.78 |   0.82 |   1    |   0.38 |   0.42 |     0.08 |     0.37 |  0.01 |
| S_AI   |    0.27 |   0.39 |   0.39 |   0.38 |   1    |   0.47 |     0.15 |     0.32 |  0.06 |
| AI_K   |    0.31 |   0.51 |   0.46 |   0.42 |   0.47 |   1    |     0.1  |     0.26 |  0.01 |
| T_AI_W |    0.11 |   0.2  |   0.21 |   0.08 |   0.15 |   0.1  |     1    |     0.65 |  0.06 |
| T_AI_U |    0.34 |   0.51 |   0.44 |   0.37 |   0.32 |   0.26 |     0.65 |     1    |  0.02 |
| Age    |   -0.04 |  -0.04 |  -0.03 |   0.01 |   0.06 |   0.01 |     0.06 |     0.02 |  1    |

## AI use (Use_F factor score) by subgroup
### By gender
| Gender            |   mean |   std |   count |
|:------------------|-------:|------:|--------:|
| Annat (Other)     |   3.23 |  1.54 |      13 |
| Kvinna (Woman)    |   4.83 |  1.94 |     732 |
| Man               |   4.95 |  2.22 |     486 |
| Prefer not to say |   3.75 |  2.21 |      16 |

### By any self-reported diagnosis (excluding 'none'/'prefer not to say' options)
| any_diagnosis   |   mean |   std |   count |
|:----------------|-------:|------:|--------:|
| False           |   4.85 |  2    |     992 |
| True            |   4.84 |  2.29 |     255 |
