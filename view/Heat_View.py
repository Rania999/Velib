import geopandas as gpd
import folium
from folium import plugins

from controler.lib import success



def display_heat(statusStations):
    # Initialisation de Geopandas
    gdf = gpd.GeoDataFrame(statusStations, geometry=gpd.points_from_xy(statusStations.lon, statusStations.lat))
    gdf.set_crs(epsg=4326, inplace=True) # definition de la transformee en WSG 84

    #J'ai testé ça : j'arrive pas à avoir le background sur la carte, mais j'ai réussi à avoir un truc interactif juste en dessous !
    gdf.to_crs(epsg=3857)
    m = folium.Map(location = ['48.8586', '2.3474'], zoom_start=12) 


    heat_data = [[point.xy[1][0], point.xy[0][0]] for point in gdf.geometry]
    plugins.HeatMap(heat_data).add_to(m)

    m.save('./output/heatMap.html')
    success('./output/heatMap.html')
    return m
