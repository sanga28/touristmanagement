from geopy.distance import geodesic
places = {
    "Paris": (48.8566, 2.3522),
    "London": (51.5074, -0.1278),
    "New York": (40.7128, -74.0060),
    "Tokyo": (35.6762, 139.6503),
    "Rome": (41.9028, 12.4964)
}
def calculate_distance(place1, place2):
    if place1 in places and place2 in places:
        coords1 = places[place1]
        coords2 = places[place2]
        distance = geodesic(coords1, coords2).km
        return distance
    else:
        return "One or both places not found."

place1 = "Paris"
place2 = "London"
distance = calculate_distance(place1, place2)
print(f"The distance between {place1} and {place2} is {distance} km.")