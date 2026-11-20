# ROGII Predictive Modelling and Validation

**Solo Kaggle entry · Silver medal · 157th place.** [Final leaderboard](https://www.kaggle.com/competitions/rogii-wellbore-geology-prediction/leaderboard)

I built a Python workflow to predict the geological position of horizontal well sections from trajectory data, gamma-ray measurements and reference logs. The project covered diagnosing where the model failed, testing changes on unseen wells and checking that the selected solution could run at the expected evaluation scale. [Competition task](https://www.kaggle.com/competitions/rogii-wellbore-geology-prediction/data)

| Work | Evidence from ROGII | Application across industries |
| --- | --- | --- |
| Diagnose performance | Decomposed prediction errors into offset, drift and residual variation. Roughly 10% of wells accounted for about 60% of squared error in the held-out analysis. | Identify the customer, product or location groups driving a performance gap and prioritise what to investigate. |
| Validate a change | Grouped validation by well, checked for leakage and tested how rankings changed as evaluation groups were resampled. | Test whether a revised forecast or scoring model holds up on groups outside the development sample. |
| Check delivery readiness | Ran the submission workflow at a 193-well test scale using frozen training outputs. | Test the expected input volume and preserve the artifacts used to produce a result. |

## Run the validation example

```sh
python3 validation_example.py
```

The script runs with Python 3.10 or later. It uses synthetic held-out losses to compare two models, measure how much error comes from a small number of groups and estimate sampling sensitivity by resampling whole groups. It also runs a small numerical check.

The candidate's pooled RMSE is 0.032 lower in the example. The middle 90% of the resampled differences spans −0.471 to +0.247, so the apparent gain depends on which groups are evaluated.

Read the [case study](case-study.md) for the project decisions and evidence, or the [Kaggle working note](https://www.kaggle.com/writeups/zeoyoungy/pricing-the-missing-sign-forty-audits-on-the-rogi) for the original research discussion.
