# import folium
# import pandas

# data = pandas.read_csv("Volcanoes.csv")
# lat = list(data["LAT"])
# lon = list(data["LON"])
# elev =list(data["ELEV"])


# map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
# fg = folium.FeatureGroup(name="My Map")

# for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color='green')))

# map.add_child(fg)

# map.save("Map.html")


import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev =list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000: 
        return 'orange'
    else:
        return 'red'      



map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
   fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" m", fill_color=color_producer(el), color= 'grey', fill_opacity=0.7))

fgb = folium.FeatureGroup(name="Population")
fgb.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgb)
map.add_child(folium.LayerControl())
map.save("Map.html")


