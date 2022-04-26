import numpy as np
import pandas as pd


arr = np.array([1, 2, 3, 4, 5])

print(arr)

df = pd.read_csv("Iris.csv")
print(df.head())

print(df.loc[0,:])
print(df["SepalWidthCm"])


