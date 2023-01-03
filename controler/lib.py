import geopandas as gpd

def get_Iris():
    """Retourne le GeoDataFrame avec les zones IRIS"""
    return gpd.read_file("./data/IRIS.gpkg", index_col=False)

def merge_StatusInfos(statusStations, infoStations):
    """Fusionne les tableaux statusStations et infoStations en un seul"""
    print(statusStations.head())
    print(infoStations.head())
    statusStationsJoined = statusStations.merge(infoStations, how='right')
    statusStationsJoined.reset_index(inplace=True)
    return statusStationsJoined
    
def group_Stations_By_Iris(stations, iris):
    """Regoupe les stations dans une zone IRIS en faisaint la somme des nombres de vélos disponibles et des places dispos."""
    # Pas fini et pas utilisé
    gdf = gpd.GeoDataFrame(stations, geometry=gpd.points_from_xy(stations.lon, stations.lat))
    gdf.set_crs(epsg=4326, inplace=True) # definition de la transformee en WSG 84
    print(iris.head())
    data_merged = gpd.sjoin(gdf, iris, how="inner", op='within')
    data_merged = data_merged.groupby('CODE_IRIS')['num_bikes_available', 'num_docks_available'].agg('sum')
    data_merged.reset_index(inplace=True)
    print(data_merged.head(2))

def success(path):
    print("The map has been created with success and can be found at " + str(path))
    return
