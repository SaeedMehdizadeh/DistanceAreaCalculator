import json

def calculate_polygon_area(coordinates):
    """
    Calculate the area of a single polygon using the Shoelace formula.

    Parameters:
    - coordinates: List of (x, y) tuples representing the polygon's outer ring.

    Returns:
    - The area of the polygon.
    """
    n = len(coordinates)
    area = 0.0
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]  # Wrap around to the first point
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0

def calculate_areas_from_geojson(geojson_data):
    """
    Calculate the areas of all polygons in a GeoJSON data object.

    Parameters:
    - geojson_data: Parsed GeoJSON object.

    Returns:
    - A list of dictionaries containing polygon IDs, properties, and areas.
    """
    areas = []
    for feature in geojson_data['features']:
        if feature['geometry']['type'] == 'Polygon':
            coordinates = feature['geometry']['coordinates'][0]
            area = calculate_polygon_area(coordinates)
            areas.append({
                'id': feature.get('id', None),
                'properties': feature.get('properties', {}),
                'area': area
            })
    return areas

def load_geojson(geojson_path):
    """
    Load a GeoJSON file and return the parsed data.

    Parameters:
    - geojson_path: Path to the GeoJSON file.

    Returns:
    - Parsed GeoJSON data.
    """
    with open(geojson_path, 'r') as file:
        return json.load(file)
