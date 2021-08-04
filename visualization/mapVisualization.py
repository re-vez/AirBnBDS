import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import mpl_scatter_density

#TODO #2
data_folder = Path("data/")
location_file = data_folder / "listings.csv"
bg_map_file= data_folder/"img/map.png"

f = open(location_file,encoding="utf8")


df = pd.read_csv(f)

print(df.head())

BBox = (df.longitude.min(), df.longitude.max(), df.latitude.min(), df.latitude.max())
BBox=[-99.364924,-98.940303,19.048237,19.592757]
uniq=list(set(df["room_type"]))

def colors_from_factors(unique_factors,cmapname):
    z = range(1,len(unique_factors))
    hot = plt.get_cmap(cmapname)
    cNorm  = colors.Normalize(vmin=0, vmax=len(uniq))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=hot)
    return scalarMap
print(BBox)

#TODO #1
#bg_map= plt.imread(bg_map_file)
bg_map=plt.imread(r"C:\Users\Luis\Documents\airbnbds\AirBnBDS\data\img\clearmap.png")

fig= plt.figure(dpi=800)
ax=fig.add_subplot(1,1,1)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
#ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
scalarMap= colors_from_factors(uniq,"Set1")
for i in range(len(uniq)):
    indx = df['room_type'] == uniq[i]
    ax.scatter(df.longitude[indx], df.latitude[indx], s=.8, color=scalarMap.to_rgba(i), label=uniq[i],alpha=.8,marker="o",edgecolors="none")
ax.set_title('AirBnBs in Mexico City')
#TODO #3
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
#ax.legend(markerscale=8, fontsize=6, bbox_to_anchor=(1, 0.5))
ax.legend(markerscale=8, fontsize=6, loc="best")
ax.imshow(bg_map, zorder=0, extent = BBox, aspect= 'equal')

white_viridis = colors.LinearSegmentedColormap.from_list('white_viridis', [
    (0, '#ffffff'),
    (1e-20, '#440053'),
    (0.2, '#404388'),
    (0.4, '#2a788e'),
    (0.6, '#21a784'),
    (0.8, '#78d151'),
    (1, '#fde624'),
], N=256)


def using_mpl_scatter_density(fig, x, y):
    ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
    density = ax.scatter_density(x, y, cmap=white_viridis,alpha=.6,zorder=5)
    fig.colorbar(density, label='Number of points per pixel')
    ax.imshow(bg_map, zorder=0, extent = BBox, aspect= 'equal')
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])

fig = plt.figure(dpi=800)
using_mpl_scatter_density(fig, df.longitude, df.latitude)


fig.savefig("visualization/img/densityscatterplot2.png")