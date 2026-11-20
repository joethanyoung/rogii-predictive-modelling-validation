# From model diagnosis to a scored submission

## Prediction task

The task was to estimate a continuous geological position, TVT, for the evaluation section of each horizontal well. The available inputs included its trajectory, gamma-ray measurements, a vertical reference log and a preceding section with known positions. Evaluation on unseen wells made the well the relevant unit for validation. [Competition data description](https://www.kaggle.com/competitions/rogii-wellbore-geology-prediction/data)

## Locate the errors worth working on

I decomposed errors into level offset, drift along the well and residual variation. That made it possible to investigate different failure modes separately. In a training-side analysis with wells held out during fitting, the highest-error tenth of wells accounted for about 60% of squared error. The result gave me a reason to investigate the tail beyond the pooled score.

I then checked two different questions. Could the available inputs flag a difficult well? Could they indicate which direction to correct its prediction? The audits identified a signal for difficulty and left the correction direction uncertain for the ambiguous cases tested. That supported a conservative prediction in those cases. [Kaggle working note](https://www.kaggle.com/writeups/zeoyoungy/pricing-the-missing-sign-forty-audits-on-the-rogi)

## Choose changes on evidence from held-out wells

I kept rows from each well together when constructing validation folds. I used field or cluster holdouts to probe transfer and checked for overlapping wells and inputs that would be unavailable at prediction time. I compared changes against the existing model on the same evaluation groups and examined how score differences varied with the group mix.

I selected the model favoured by grouped validation. The public leaderboard had favoured a different candidate. Kaggle's hidden evaluation placed the selected model ahead of that candidate.

## Check the workflow at the scale of the evaluation

I packaged per-well execution around saved training outputs and tested the workflow at a 193-well scale in Kaggle's environment. The submission received a score on the hidden evaluation. The solo entry placed 157th and earned a silver medal. [Final leaderboard](https://www.kaggle.com/competitions/rogii-wellbore-geology-prediction/leaderboard)

## Apply the same steps to a new problem

For a forecasting or scoring change, profile errors at the unit that drives the decision, such as an account, product or location. Compare candidates on independent groups using inputs available at the point of use. Check that the chosen workflow can process the expected workload before it is used to make decisions.

The [Python example](validation_example.py) illustrates the paired comparison with synthetic held-out losses. It resamples the groups and recomputes pooled RMSE for both models together. The resulting interval describes sensitivity to the group mix in this example. A new population would call for evaluation on that population.
