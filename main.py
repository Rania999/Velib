# %%
import numpy as np
import pandas as pd
import datetime as pkgdt
import geopandas as gpd
import contextily as cx
import folium
#import rasterio
#from rasterio.plot import show as rioshow
import matplotlib.pyplot as plt
from model.Middleware import *
from controler.lib import *
from view.Heat_View import display_heat
from view.Normal_View import display_normal
from view.Iris_View import display_Iris
from view.Evolution_Iris_View import display_evolution_Iris

api = Middleware()

api.update()
infoStations = api.info_stations
statusStations = api.status_stations

stations = merge_StatusInfos(statusStations,infoStations)

#print(stations.head())

display_normal(stations)
display_heat(stations)
display_Iris(stations)
display_evolution_Iris(stations)




#display_heat(statusStations)

