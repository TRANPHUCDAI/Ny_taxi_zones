import sys
print("arguments", sys.argv)
month = int(sys.argv[1])
print(f"Hello-world month {month}")

import pandas as pd

df = pd.DataFrame({"day":[1,2], "month":[3,4],"number":[5,6]})

print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f"hello pipeline, month {month}")