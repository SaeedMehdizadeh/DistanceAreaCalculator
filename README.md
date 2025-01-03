# DistanceAreaCalculator

The `DistanceAreaCalculator` is a Python library that provides tools for calculating distances between geospatial points and computing the areas of polygons. It supports GeoJSON data formats, making it easy to integrate with popular geospatial tools.

## Features
- **Calculate Distances**: Compute distances between two points using latitude and longitude.
- **Calculate Areas**: Determine the area of polygons from GeoJSON data.
- **GeoJSON Support**: Work seamlessly with GeoJSON files for geospatial data.
- **Unit Tests**: Includes unit tests to ensure reliability.

from distances import calculate_distance

# Example
point1 = (40.7128, -74.0060)  # New York City (latitude, longitude)
point2 = (34.0522, -118.2437)  # Los Angeles

# Calculate distance in kilometers
distance = calculate_distance(point1, point2)
print(f"Distance: {distance} km")

from areas import calculate_area

# Example GeoJSON polygon
polygon_geojson = {
    "type": "Polygon",
    "coordinates": [
        [
            [-80.190, 25.774],
            [-66.118, 18.466],
            [-64.757, 32.321],
            [-80.190, 25.774]
        ]
    ]
}

# Calculate area in square kilometers
area = calculate_area(polygon_geojson)
print(f"Area: {area} square km")


python -m unittest discover


File Structure

areas.py: Contains functions for calculating polygon areas.
distances.py: Functions for calculating distances between points.
init.py: Package initializer.
setup.py: Library setup and metadata.
Points.geojson: Example GeoJSON data for points.
Polygons.geojson: Example GeoJSON data for polygons.
TestAreas.py: Unit tests for areas.py.
TestDistances.py: Unit tests for distances.py.


