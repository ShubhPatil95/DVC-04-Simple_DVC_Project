
##  School-1 Experiment

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

## Read Data
df = pd.read_csv("data.csv")
df.head()

## Data Preprocessing
X = df.Hours.values.reshape(-1,1)
Y = df.Marks.values

## Apply Linear Regression
lr = LinearRegression()
lr.fit(X,Y)
Y_Pred = lr.predict(X)

## Metrics Evaluation
r_square = r2_score(Y,Y_Pred)
print(f"r_square = {r_square}")
