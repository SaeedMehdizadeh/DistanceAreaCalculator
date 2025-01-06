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
## Data requirements
The `DistanceAreaCalculator` library requires GeoJSON files for points and polygons to perform calculations. You can create or download the required GeoJSON data from the following link:<br>

http://geojson.io/: A simple tool for creating, editing, and visualizing GeoJSON data.<br>

Simply upload your data or draw your shapes directly on the map, and export the file as GeoJSON to use it with this library.
## Installation
**Using pip (recommended)**
   ```bash
pip install distances
pip install areas
   ```
**From Source**<br>
Clone the repository and install the package manually:

   ```bash
git clone https://github.com/SaeedMehdizadeh/DistanceAreaCalculator.git
cd DistanceAreaCalculator
pip install .

   ```


# Testing

the following instructions should be provided for running the tests, e.g:`TestDistances.py` and `TestAreas.py`

   ```bash
pytest
   ```
or
  ```bash
python -m unittest discover tests/
   ```

# Usage

**Importing the Library**
 ```bash
from .distances import calculate_distance
from .areas import calculate_area
   ```
**Example: Distance Calculation**

 ```bash
from .distances import calculate_distance

point1 = {"type": "Point", "coordinates": [10.0, 20.0]}
point2 = {"type": "Point", "coordinates": [30.0, 40.0]}
distance = calculate_distance(point1, point2)
print(f"Distance: {distance} km")
   ```

**Example: Area Calculation**
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

We welcome contributions to improve the DistanceAreaCalculator library! Whether it’s fixing bugs, adding new features, or improving documentation, your help is greatly appreciated.<br>

- **Fork the Repository**: Click the “Fork” button at the top of this repository.<br>

- **Create a Feature Branch**: Use a meaningful name, like feature/new-distance-method.<br>
 ```bash
git checkout -b feature/new-distance-method
   ```
- **Make Changes**: Add your improvements, ensuring you write clear, reusable code.<br>

- **Write Tests**: Add or update tests in the tests/ directory to cover your changes.<br>

- **Submit a Pull Request**: Push your changes to your fork and create a pull request with a detailed explanation of your changes.


# License

This project is licensed under the `MIT License`. See the [LICENSE](https://github.com/SaeedMehdizadeh/DistanceAreaCalculator/blob/main/LICENSE) file for details.

# Contact

If you have any questions, suggestions, or feedback about the DistanceAreaCalculator library, feel free to reach out!<br>

**Author**: Saeed Mehdizadeh <br>
**Email**: saeed.mehdizadeh@mail.polimi.it


