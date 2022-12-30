
import geopandas as gpd
import folium
from folium import plugins

# traitement d'un problème avec la projection --> déclarer la librairie de projection 
import os

from controler.lib import success


def display_normal(stations):
    """Export une carte normal.html avec toutes les stations sous forme de points"""
    # Initialisation de Geopandas
    gdf = gpd.GeoDataFrame(stations, geometry=gpd.points_from_xy(stations.lon, stations.lat))
    gdf.set_crs(epsg=4326, inplace=True) # definition de la transformee en WSG 84
    gdf.to_crs(epsg=3857)
    geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in gdf.geometry]
    #init folium
    m = folium.Map(location = ['48.8586', '2.3474'], zoom_start=12, tiles='stamentoner') 
    
    #ajout de reprères 
    i = 0
    for coordinates in geo_df_list:
        folium.Marker(coordinates, popup= "" + str(gdf.name[i]) +'<br>' + 'Vélos disponibles : ' + str(gdf.num_bikes_available[i]) +'<br>' + 'Places disponibles : ' +str(gdf.num_docks_available[i]) ).add_to(m)
        i = i+1
    m.save('./output/normal.html')
    success('./output/normal.html')
    return m


