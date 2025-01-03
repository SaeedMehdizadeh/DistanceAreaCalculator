import unittest
import random
from distances import calculate_distance
import geopandas as gpd

class TestDistances(unittest.TestCase):
    distances = []  # Class-level list to store distances

    @classmethod
    def setUpClass(cls):
        """
        Load the Points.geojson dataset once for all tests.
        """
        cls.file_path = "/Users/saeedmehdizadeh/Desktop/Third Semester/Geospatial Processing/Project/DistanceAreaCalculator/Points.geojson"
        cls.gdf = gpd.read_file(cls.file_path)

    def test_distance_between_random_points(self):
        """
        Test the distance calculation between two randomly selected points.
        """
        # Randomly select two different points
        indices = random.sample(range(len(self.gdf)), 2)
        lon1, lat1 = self.gdf.geometry[indices[0]].coords[0]
        lon2, lat2 = self.gdf.geometry[indices[1]].coords[0]

        # Calculate the distance using the function
        calculated_distance = calculate_distance(lat1, lon1, lat2, lon2)
        TestDistances.distances.append(calculated_distance)  # Store the distance

        # Dynamically calculate the expected distance (same logic as the function)
        from math import radians, cos, sin, sqrt, atan2

        # Convert to radians
        lat1_r, lon1_r = radians(lat1), radians(lon1)
        lat2_r, lon2_r = radians(lat2), radians(lon2)

        # Haversine formula
        dlat = lat2_r - lat1_r
        dlon = lon2_r - lon1_r
        a = sin(dlat / 2) ** 2 + cos(lat1_r) * cos(lat2_r) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        radius = 6371  # Earth's radius in kilometers
        expected_distance = radius * c

        # Assert the calculated distance matches the expected value
        self.assertAlmostEqual(calculated_distance, expected_distance, places=1)

    def test_distance_same_point(self):
        """
        Test that the distance between a point and itself is zero.
        """
        # Randomly select a single point
        index = random.choice(range(len(self.gdf)))
        lon, lat = self.gdf.geometry[index].coords[0]

        # Calculate the distance
        distance = calculate_distance(lat, lon, lat, lon)
        TestDistances.distances.append(distance)  # Store the distance

        # Assert the distance is zero
        self.assertEqual(distance, 0)

if __name__ == "__main__":
    unittest.main(exit=False)  # Prevent unittest from closing the program
    print("\nCalculated Distances:")
    for distance in TestDistances.distances:
        print(distance)
