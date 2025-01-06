# DistanceAreaCalculator

The `DistanceAreaCalculator` is a Python library that provides tools for calculating distances between geospatial points and computing the areas of polygons. It supports GeoJSON data formats, making it easy to integrate with popular geospatial tools.


## Features
- **Calculate Distances**: Compute distances between two points using latitude and longitude.
- **Calculate Areas**: Determine the area of polygons from GeoJSON data.
- **GeoJSON Support**: Work seamlessly with GeoJSON files for geospatial data.
- **Unit Tests**: Includes unit tests to ensure reliability.

## File structure
```bash
DistanceAreaCalculator/
├── init.py               # Package initialization file
├── distances.py          # Module for distance calculations
├── areas.py              # Module for area calculations
├── data/
│   ├── Points.geojson    # GeoJSON file for point data
│   ├── Polygons.geojson  # GeoJSON file for polygon data
├── tests/
│   ├── TestAreas.py      # Unit tests for area functions
│   ├── TestDistances.py  # Unit tests for distance functions
├── LICENSE               # License file for the project
├── README.md             # Project documentation
├── setup.py              # Script for library installation
 ```

## Installation
1.Using pip (recommended)

   ```bash
pip install distances
pip install areas
   ```
2.From Source
Clone the repository and install the package manually:

   ```bash
git clone https://github.com/SaeedMehdizadeh/DistanceAreaCalculator.git
cd DistanceAreaCalculator
pip install .

   ```


### Steps

1.install dependencies:
   ```bash
pip install -r requirements.txt

   ```
2.Run the tests to verify installation:
  ```bash
python -m unittest discover tests
   ```

# Usage

Importing the Library
 ```bash
from .distances import calculate_distance
from .areas import calculate_area
   ```
Example: Distance Calculation

 ```bash
from .distances import calculate_distance

point1 = {"type": "Point", "coordinates": [10.0, 20.0]}
point2 = {"type": "Point", "coordinates": [30.0, 40.0]}
distance = calculate_distance(point1, point2)
print(f"Distance: {distance} km")
   ```

Example: Area Calculation
 ```bash
from .areas import calculate_area

polygon = {
    "type": "Polygon",
    "coordinates": [[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]]
}
area = calculate_area(polygon)
print(f"Area: {area} sq. km")
   ```

# Contributing

We welcome contributions! To contribute:

Fork this repository.
Create a feature branch:
 ```bash
git checkout -b feature-name
   ```
Commit your changes and push them to your fork.

Submit a pull request.


# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Contact

If you have any questions, suggestions, or feedback about the DistanceAreaCalculator library, feel free to reach out!
# Author: Saeed Mehdizadeh
# Email: saeed.mehdizadeh@mail.polimi.it


