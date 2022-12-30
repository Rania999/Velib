import pandas as pd
import geopandas as gpd
import requests


class Middleware : 
    """Class faisant le lien avec l'API de la Metropoe Velib"""

    def __init__(self):
        self.info_stations = pd.DataFrame.empty
        self.status_stations = pd.DataFrame.empty
    
    def __get(self, url):
        """Fonction permmettant de faire les requetes des JSON issus de Velib Metropole"""
        # TODO : add error handeling 
        return pd.DataFrame(pd.read_json(url)["data"]["stations"])

    def __get_info_stations(self): 
        """Fonction recupperant les donnees issus de l'API information"""
        return self.__get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json")
    
    def __get_status_stations(self):
        """Fonction recupperant les donnees issus de l'API status"""
        return self.__get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json")

    def update(self):
        """Receupère les données depuis l'API velib"""
        # Recupère les tableaux
        infoStations = self.__get_info_stations()
        statusStations = self.__get_status_stations()

        #Supprime les colones non nécessaires
        statusStations.pop('numDocksAvailable')
        statusStations.pop('numBikesAvailable')
        statusStations.pop('stationCode')

        #Crée les colonnes
        statusStations["num_bikes_mechanical"] = 0
        statusStations["num_bikes_ebike"] = 0
        for i in statusStations.index:
            statusStations.loc[i,"num_bikes_mechanical"] = statusStations.loc[i,'num_bikes_available_types'][0]["mechanical"]
            statusStations.loc[i,"num_bikes_ebike"] = statusStations.loc[i,'num_bikes_available_types'][1]["ebike"]
        statusStations.pop('num_bikes_available_types' )

        # Indexe les tableaux
        statusStations.set_index("station_id", inplace=True)
        infoStations.set_index("station_id", inplace=True)

        self.info_stations = infoStations
        self.status_stations = statusStations
        return self

        



