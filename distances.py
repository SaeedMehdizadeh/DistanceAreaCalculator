from math import radians, cos, sin, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on Earth using the Haversine formula.

    Parameters:
    - lat1, lon1: Latitude and Longitude of the first point in decimal degrees.
    - lat2, lon2: Latitude and Longitude of the second point in decimal degrees.

    Returns:
    - Distance in kilometers between the two points.
    """
    # Convert decimal degrees to radians
    lat1, lon1 = radians(lat1), radians(lon1)
    lat2, lon2 = radians(lat2), radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    radius = 6371  # Earth's radius in kilometers

    # Return the calculated distance
    return radius * c
