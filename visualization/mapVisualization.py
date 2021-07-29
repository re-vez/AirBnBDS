import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


data_folder = Path("data/")
location_file = data_folder / "listings.csv"
bg_map_file= data_folder/"img/map.png"

f = open(location_file,encoding="utf8")


df = pd.read_csv(f)

print(df.head())

BBox = (df.longitude.min(), df.longitude.max(), df.latitude.min(), df.latitude.max())
print(BBox)


#bg_map= plt.imread(bg_map_file)
bg_map=plt.imread(r"C:\Users\Luis\Documents\airbnbds\AirBnBDS\data\img\map.png")

fig= plt.figure()
ax=fig.add_subplot(1,1,1)
#fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('AirBnBs in Mexico City')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(bg_map, zorder=0, extent = BBox, aspect= 'equal')

fig.savefig("out1.png")