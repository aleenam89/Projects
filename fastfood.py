import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv('fastfood.csv')

x = pd.DataFrame(df, columns = ['total_fat','sat_fat','cholesterol','sodium'])
y = pd.DataFrame(df, columns = ['calories'])



x = sm.add_constant(x)

mod1=sm.OLS(y,x)

model=mod1.fit()


print(model.mse_total.round(2))

print(model.rsquared.round(2))

print(model.params.round(2))

print(model.pvalues.round(2))
