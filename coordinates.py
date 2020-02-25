from geopy.geocoders import Nominatim


def get_friends_coordinates(friends:list) -> list:
    """
    Converts physical address to coordinates and returns
    a list of friends and their coordinates
    """
    coords = []
    geolocator = Nominatim(user_agent='FindDruzi', timeout=3)
    for friend in friends:
        location = geolocator.geocode(friend[1])
        try:
            coords.append([friend[0], location.latitude, location.longitude])
        except AttributeError:
            pass
    return coords


def adjust_coords(friends):
    '''
    Receives list of people and their coordinates
    and adjust coordinates to make them perfectly fit on the map
    '''
    friends_coords = []
    num = 0
    for friend in friends:
        friend_lst = friend[:]
        friend_lst[2] += num * 0.0002
        friends_coords.append(friend_lst)
        num += 1
    return friends_coords