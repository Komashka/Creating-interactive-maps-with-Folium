import open_file
import layers
import folium

myMap = folium.Map()

myMap.add_child(layers.film_layer(open_file.open_file(str(input('Please write a year(numer only): ')))))
myMap.add_child(layers.population_layer())
myMap.add_child(layers.okean_elzy_layer())
myMap.add_child(layers.ice_edge_layer())

myMap.add_child(folium.LayerControl())
myMap.save("myMap.html")
