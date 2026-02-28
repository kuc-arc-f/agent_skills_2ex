import pandas as pd


df = pd.read_csv("work/input.csv")

df.to_excel("work/out/output.xlsx", index=False)

