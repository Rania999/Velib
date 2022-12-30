import folium
import webbrowser


class Map:
    def __init__(self, center = ['48.8586', '2.3474'], zoom_start = 12, tiles = ""):
        self.center = center
        self.zoom_start = zoom_start
        self.tiles = tiles
    
    def showMap(self):
        #Create the map
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start, tiles =self.tiles)

        #Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")


