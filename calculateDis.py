import pandas as pd
import numpy as np

path = "dr7_v1.2_stellar_LRS光年数据.csv"

csv_file = pd.read_csv(path, sep=',', index_col=0)

data = csv_file['parallax']
star_distance = 1000 / data * 3.2616
csv_file['Star_distance'] = star_distance
csv_file.to_csv(r"dr7_v1.2_stellar_LRS附光年数据.csv", mode='a', index=False)

print(data)
print(star_distance)
print(csv_file)
