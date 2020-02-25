import folium


def build_map(friends_coords):
    '''
    Receives a list of people in format [person, latitude, longitude]
    And returns a map with people locations

    '''

    fr_coords = friends_coords[0]
    user = friends_coords[1]

    map = folium.Map(location=[30, 0],
                    zoom_start=2)

    fg_friends = folium.FeatureGroup(name=f"{user} friends")

    for person, lat, lng in fr_coords:
        fg_friends.add_child(folium.Marker(location=[lat, lng], popup=person))



    map.add_child(fg_friends)
    map.add_child(folium.LayerControl())
    return map._repr_html_()
