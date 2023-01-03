# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:51:43 2023

@author: Rania
"""
import geopandas as gpd
from controler.lib import *
import random
from bokeh.plotting import figure, output_file, show


def display_evolution_Iris(stations):
    """Affiche le nombre de vélos disponibles par zone Iris au cours de la journée."""
    iris = get_Iris()
    gdf = gpd.GeoDataFrame(stations, geometry=gpd.points_from_xy(stations.lon, stations.lat))
    gdf.set_crs(epsg=4326, inplace=True) # definition de la transformee en WSG 84
    #print(iris.head())
    data_merged = gpd.sjoin(gdf, iris, how="inner", op='within')
    for i in data_merged.index:
        data_merged.loc[i,"record_timestamp"] = 10 * random.random()
    
    data_merged = data_merged.groupby(['CODE_IRIS',"record_timestamp"])['num_bikes_available'].sum()
    data_merged = data_merged.reset_index()
    
    # Visualisation
    graph = figure(title = "Nombre de vélos disponibles dans la zone au cours de la journée")
    
    #test sur une zone Iris aléatoire
    iris_code = data_merged['CODE_IRIS'][23]
    data_merged_zone = data_merged.loc[data_merged['CODE_IRIS'] == iris_code]
    
    graph.line(data_merged_zone["num_bikes_available"], data_merged_zone['record_timestamp'])
    graph.xaxis.axis_label = "Heure"
    graph.yaxis.axis_label = "Nombre de vélos"
    show(graph)