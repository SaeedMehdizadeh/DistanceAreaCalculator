# DistanceAreaCalculator

The `DistanceAreaCalculator` is a Python library that provides tools for calculating distances between geospatial points and computing the areas of polygons. It supports GeoJSON data formats, making it easy to integrate with popular geospatial tools.

1.requirements of the geospatial library project:

## Features
- **Calculate Distances**: Compute distances between two points using latitude and longitude.
- **Calculate Areas**: Determine the area of polygons from GeoJSON data.
- **GeoJSON Support**: Work seamlessly with GeoJSON files for geospatial data.
- **Unit Tests**: Includes unit tests to ensure reliability.

## Installation

### Prerequisites
- Python 3.8 or higher
- Recommended: Virtual environment (e.g., `venv` or `conda`)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>

2.install dependencies:
   ```bash
pip install -r requirements.txt

   ```
3.Run the tests to verify installation:
  ```bash
python -m unittest discover tests
   ```

Usage

Importing the Library
 ```bash
from distances import calculate_distance
from areas import calculate_area
   ```
Example: Distance Calculation

 ```bash
from distances import calculate_distance

point1 = {"type": "Point", "coordinates": [10.0, 20.0]}
point2 = {"type": "Point", "coordinates": [30.0, 40.0]}
distance = calculate_distance(point1, point2)
print(f"Distance: {distance} km")
   ```

Example: Area Calculation
 ```bash
from areas import calculate_area

polygon = {
    "type": "Polygon",
    "coordinates": [[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]]
}
area = calculate_area(polygon)
print(f"Area: {area} sq. km")
   ```

Contributing

We welcome contributions! To contribute:

Fork this repository.
Create a feature branch:
 ```bash
git checkout -b feature-name
   ```
Commit your changes and push them to your fork.
Submit a pull request.


License

This project is licensed under the MIT License. See the LICENSE file for details.

File Structure

areas.py: Contains functions for calculating polygon areas.
distances.py: Functions for calculating distances between points.
init.py: Package initializer.
setup.py: Library setup and metadata.
Points.geojson: Example GeoJSON data for points.
Polygons.geojson: Example GeoJSON data for polygons.
TestAreas.py: Unit tests for areas.py.
TestDistances.py: Unit tests for distances.py.


