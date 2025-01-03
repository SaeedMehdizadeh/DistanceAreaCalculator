import random
from areas import calculate_polygon_area, load_geojson

def calculate_random_polygon_area_in_m2(geojson_path):
    """
    Randomly select a polygon from the GeoJSON dataset and calculate its area in square meters.

    Args:
        geojson_path (str): Path to the GeoJSON file containing polygons.

    Returns:
        dict: A dictionary containing the ID of the polygon (or "unknown" if ID is missing)
              and its calculated area in square meters.
    """
    # Load GeoJSON data
    geojson_data = load_geojson(geojson_path)
    polygons = [
        feature for feature in geojson_data['features']
        if feature['geometry']['type'] == 'Polygon'
    ]
    
    if not polygons:
        raise ValueError("No polygons found in the GeoJSON file.")

    # Randomly select a polygon
    selected_polygon = random.choice(polygons)
    coordinates = selected_polygon['geometry']['coordinates'][0]  # Outer ring
    area_m2 = calculate_polygon_area(coordinates)  # Area in square meters
    polygon_id = selected_polygon.get('id', 'unknown')  # Default to 'unknown' if 'id' is missing

    return {"id": polygon_id, "area_m2": area_m2}

if __name__ == "__main__":
    geojson_path = "Polygons.geojson"  # Update the path if needed
    result = calculate_random_polygon_area_in_m2(geojson_path)
    print(f"Randomly selected polygon ID: {result['id']}, Area: {result['area_m2']} m²")
