import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from patsy import dmatrices

df = pd.read_csv('german_credit_data.csv')
df = df.rename ({'Credit amount': 'Credit_amount'}, axis = 1)

y, X = dmatrices ('Credit_amount ~ Age + Duration', data = df, return_type = 'dataframe')

X = sm.add_constant(X)

mod1=sm.OLS(y,X)

model=mod1.fit()

print(model.params.round(2))
print(model.rsquared.round(2))
