import geopandas as gpd
import folium
from folium import plugins
from controler.lib import *



def display_Iris(stations):
    """Produit un fichier html avec le nombre de vélos disponibles et de places libres dans chaque zone IRIS."""
    # A séparer pour faciliter le traitement
    iris = get_Iris()
    gdf = gpd.GeoDataFrame(stations, geometry=gpd.points_from_xy(stations.lon, stations.lat))
    gdf.set_crs(epsg=4326, inplace=True) # definition de la transformee en WSG 84
    #print(iris.head())
    data_merged = gpd.sjoin(gdf, iris, how="inner", op='within')
    data_merged = data_merged.groupby('CODE_IRIS')['num_bikes_available', 'num_docks_available'].agg('sum')
    data_merged.reset_index(inplace=True)

    #creation de la carte
    m = folium.Map(location = ['48.8586', '2.3474'], zoom_start=12)
    #ajout des couches
    folium.Choropleth(
        geo_data=iris,
        name="Vélos disponibles",
        data=data_merged,
        columns=['CODE_IRIS',"num_bikes_available"],
        key_on="feature.properties.CODE_IRIS",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Nombre de vélos disponibles",
        nan_fill_color = "None"
    ).add_to(m)
    folium.Choropleth(
        geo_data=iris,
        name="Emplacements disponibles",
        data=data_merged,
        columns=['CODE_IRIS',"num_docks_available"],
        key_on="feature.properties.CODE_IRIS",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Nombre d'emplacements disponibles",
        nan_fill_color = "None",
        show=False
    ).add_to(m)
    folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)


    folium.LayerControl(collapsed=False).add_to(m)


    m.save("./output/IRIS.html")
    success("./output/IRIS.html")
    return m