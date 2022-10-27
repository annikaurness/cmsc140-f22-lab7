import pandas as pd
from pathlib import Path

datapath = Path("city_temperature.csv")

df = pd.read_csv(datapath, sep=",", low_memory=False)

data = df.loc[df.groupby(['Region'])['AvgTemperature'].idxmax()]
print(data)

outfile = Path("city_max_temp.csv")

data.to_csv(outfile, index = False)