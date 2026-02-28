import pandas as pd


df = (
    pd.read_csv("work/input.csv")
        .query("Age >= 30")
        .sort_values("Age")
)
data = df.values.tolist()

print(data)

df.to_excel("work/out/age.xlsx", index=False)

