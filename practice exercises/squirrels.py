import pandas as pd


data = pd.read_csv("squirrel_data.csv")

cinnamon_count = data[data["Primary Fur Color"] == "Cinnamon"].count()["Primary Fur Color"]
gray_count = data[data["Primary Fur Color"] == "Gray"].count()["Primary Fur Color"]
black_count = data[data["Primary Fur Color"] == "Black"].count()["Primary Fur Color"]





fur_colors = {
    "color": ["Cinnamon","Gray","Black"],
    "count": [cinnamon_count,gray_count, black_count]
}

print(fur_colors)
fur_colors = pd.DataFrame(fur_colors)
fur_colors.to_csv("fur_colors.csv")