import pandas as pd
import numpy as np

path = "dr8_v1.0_stellar_LRS/dr8_v1.0_stellar_LRS.csv"

csv_file = pd.read_csv(path, sep='|', index_col=0)

# csv_file['lmjd'] = csv_file['lmjd'].astype("str")
# csv_file['mjd'] = csv_file['mjd'].astype("str")
# csv_file['mag5'] = csv_file['mag5'].astype("str")
# csv_file['offsets'] = csv_file['offsets'].astype("bool")


csv_file['gaia_source_id'] = csv_file['gaia_source_id'].astype("str")

print(csv_file.shape)
print(csv_file["gaia_source_id"])
print(csv_file.dtypes)




csv_file.to_excel("dr8_v1.0_stellar_LRS/dr8_v1.0_stellar_LRS.xlsx")
