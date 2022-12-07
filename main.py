# %%
import numpy as np
import pandas as pd
import datetime as pkgdt
import geopandas as gpd
import contextily as cx
#import folium
import rasterio
from rasterio.plot import show as rioshow
import matplotlib.pyplot as plt
from model.Middleware import *

# %%

api = Middleware()

api.update()
infoStations = api.info_stations
statusStations = api.status_stations

statusStations = statusStations.join(infoStations)
# Initialisation de Geopandas
gdf = gpd.GeoDataFrame(statusStations, geometry=gpd.points_from_xy(infoStations.lon, infoStations.lat))
gdf.set_crs(epsg=4326, inplace=True) # definition de la transformee en WSG 84

# %%
#J'ai testé ça : j'arrive pas à avoir le background sur la carte, mais j'ai réussi à avoir un truc interactif juste en dessous !
fig,ax = plt.subplots(figsize=(10, 10)) 
gdf.to_crs(epsg=3857).plot("num_bikes_mechanical",
              ax=ax,
              alpha=0.5, 
              legend=True, 
              legend_kwds={'label': "Nombre de vélos mécaniques par station",
                        'orientation': "horizontal"})
ax.set_axis_off()
cx.add_basemap(ax)
plt.show()


