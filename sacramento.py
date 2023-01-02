import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv('sacramento.csv')

df['baths2'] = np.select([(df['baths'] <= 1), df['baths'] > 1], [0,1])

X = df.loc[:, ['beds','sqft','price']]
X = sm.add_constant(X)

y = df.baths2

mod=sm.Logit(y,X).fit()


print(mod.params.round(2))
print(mod.pvalues.round(2))
print('The smallest p-value is for sqft')
