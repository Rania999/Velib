import pandas as pd
import geopandas as gpd
import requests


class Iris() : 
    """Class créeant une liste IRIs"""

    def __init__(self):
        self.gdf = gpd.read_file("./data/IRIS.gpkg")




