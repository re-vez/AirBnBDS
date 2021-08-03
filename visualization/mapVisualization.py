import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

#TODO #2
data_folder = Path("data/")
location_file = data_folder / "listings.csv"
bg_map_file= data_folder/"img/map.png"

f = open(location_file,encoding="utf8")


df = pd.read_csv(f)

print(df.head())

BBox = (df.longitude.min(), df.longitude.max(), df.latitude.min(), df.latitude.max())
uniq=list(set(df["room_type"]))

def colors_from_factors(unique_factors):
    z = range(1,len(unique_factors))
    hot = plt.get_cmap('hot')
    cNorm  = colors.Normalize(vmin=0, vmax=len(uniq))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=hot)
    return scalarMap
print(BBox)

#TODO #1
#bg_map= plt.imread(bg_map_file)
bg_map=plt.imread(r"C:\Users\Luis\Documents\airbnbds\AirBnBDS\data\img\map.png")

fig= plt.figure(dpi=1200)
ax=fig.add_subplot(1,1,1)
#fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
scalarMap= colors_from_factors(uniq)
for i in range(len(uniq)):
    indx = df['room_type'] == uniq[i]
    ax.scatter(df.longitude[indx], df.latitude[indx], s=5, color=scalarMap.to_rgba(i), label=uniq[i],alpha=.2)
ax.set_title('AirBnBs in Mexico City')
#TODO #3
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(bg_map, zorder=0, extent = BBox, aspect= 'equal')

fig.savefig("visualization/img/locationbytype.png")