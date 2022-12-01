# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as pkgdt
import requests 
import geopandas as gpd
#import contextily as cx
import folium
from requests.adapters import HTTPAdapter

# %%
r = requests.get(
    "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json",
    headers = ''
)

if r.status_code != 200: # see HTTP errors
    print("HTTP ERROR")
else:  
    r.text
    infoStations = pd.DataFrame(pd.DataFrame(r.json())["data"]["stations"]) 

# %%

## TODO 
# - put proper error handeling 

r = requests.get(
   "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json",
    headers = ''
)

if r.status_code != 200: # see HTTP errors
    print("HTTP ERROR")
else:  
    r.text
    statusStations = pd.DataFrame(pd.DataFrame(r.json())["data"]["stations"])
    print(statusStations)
    
    #supprime les colones non nécessaires
    statusStations.pop('numDocksAvailable')
    statusStations.pop('numBikesAvailable')
    statusStations.pop('stationCode')


    #création des colonnes
    statusStations["num_bikes_mechanical"] = 0
    statusStations["num_bikes_ebike"] = 0

    for i in statusStations.index:
        statusStations.loc[i,"num_bikes_mechanical"] = statusStations.loc[i,'num_bikes_available_types'][0]["mechanical"]
        statusStations.loc[i,"num_bikes_ebike"] = statusStations.loc[i,'num_bikes_available_types'][1]["ebike"]
    statusStations.pop('num_bikes_available_types' )


# %%
statusStations.set_index("station_id", inplace=True)
infoStations.set_index("station_id", inplace=True)

# %%
statusStations = statusStations.join(infoStations)
# %% Initialisation de Geopandas
gdf = gpd.GeoDataFrame(statusStations, geometry=gpd.points_from_xy(infoStations.lon, infoStations.lat))
gdf.set_crs(epsg=4326, inplace=True) # definition de la transformee en WSG 84

# %%
#J'ai testé ça : j'arrive pas à avoir le background sur la carte, mais j'ai réussi à avoir un truc interactif juste en dessous ! 
ax = gdf.plot("num_bikes_mechanical", 
              alpha=0.5, 
              legend=True, 
              legend_kwds={'label': "Nombre de vélos mécaniques par station",
                        'orientation': "horizontal"})
#cx.add_basemap(ax, zoom = 15)

plt.show()

# %%
#Sur le modèle de ça : 

# %%
df = gpd.read_file(gpd.datasets.get_path('nybb'))
ax = df.plot(figsize=(5, 5), alpha=0.5, edgecolor='k')
df_wm = df.to_crs(epsg=3857)
ax = df_wm.plot(figsize=(5, 5), alpha=0.5, edgecolor='k')
#cx.add_basemap(ax)

# %%
gdf.explore("num_bikes_mechanical", 
              legend=True,            
              legend_kwds={'label': "Nombre de vélos mécaniques par station",
                        'orientation': "horizontal"})

plt.show()

# %%




