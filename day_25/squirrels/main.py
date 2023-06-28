# Challenge: Get the squirrels of red/black/gray colors from csv and show their count in new csv

import pandas as pd

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Red"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

squirrels_dict = {
    "Fur Colors": ["gray", "red", "black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}
df = pd.DataFrame(squirrels_dict)
print(df)
df.to_csv("squirrels_count.csv")
