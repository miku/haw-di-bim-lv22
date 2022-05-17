
import pandas as pd

dfs = pd.read_html("https://de.wikipedia.org/wiki/Museen_in_Deutschland", decimal=',', thousands='.')
df = dfs[3]
df["BPA"] = df["Besucher (2016)"] / df["Ausstel-lungen"]
print(df)
