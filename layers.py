import folium
from geopy import ArcGIS

myMap = folium.Map()


def film_layer(contents):
    """
    list -> layer

    Takes a list of lists and returns a layer with marked locations where the movie was set.
    """
    fg = folium.FeatureGroup(name="Pointers")
    count = 0
    # Receive a numbers of films user want to be shown on the map
    film_number = int(input("How much films do you want to receive from {} films: ".format(len(contents))))
    if film_number > len(contents):
        return "Wrong input"
    for line in contents:
        if count == film_number:
            break
        count += 1
        try:
            # Decoding an address of location
            geolocator = ArcGIS(timeout=10)
            location = geolocator.geocode(line[1])
            fg.add_child(
                folium.Marker(location=[location.latitude, location.longitude], popup=line[0],
                              icon=folium.Icon(color="red")))
        except AttributeError:
            continue
    return fg


def population_layer():
    """
    Returns a layer with painted countries by populationю
    """
    population = folium.FeatureGroup(name="Population")
    population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {
        'fillColor': 'red' if x['properties']['POP2005'] < 10000000 else 'blue' if 10000000 <= x['properties'][
            'POP2005'] < 20000000 else 'yellow'}))
    return population


def okean_elzy_layer():
    """
    -> layer
    Returns a layer with marked locations where the Okean Elzy group concerts will take place in 2018
    """
    okean_elzy = folium.FeatureGroup(name="Concerts of Slavko")
    geolocator = ArcGIS(timeout=10)
    # Takes only one address because only one is given on the official site
    location_conc = geolocator.geocode('Velyka Vasylkivska St, 55, Kyiv')
    # Adding image of icon we want to use
    icon_v = folium.features.CustomIcon('vakarchuk.png', icon_size=(40, 40))
    okean_elzy.add_child(
        folium.Marker(location=[location_conc.latitude, location_conc.longitude], popup="Concerts of Okean Elzy",
                      icon=icon_v))
    return okean_elzy


def ice_edge_layer():
    """
    -> layer
    Returns a layer marked with Antarctica ice cover
    """
    ice = folium.FeatureGroup(name="Ice Edge")
    return ice.add_child(folium.TopoJson(open('antarctic_ice_shelf_topo.json'), 'objects.antarctic_ice_shelf'))
