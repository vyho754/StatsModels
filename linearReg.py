#model x & y arrays

import numpy as np
import pandas as pd
import statsmodels.formula.api as sm

x = np.arange(100)
y = 0.5*x - 20 + np.random.randn(len(x))

df = pd.DataFrame({'x':x,'y':y})

model = sm.ols('y~x', data = df).fit()

print(model.summary())
