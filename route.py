# route.py
import numpy as np

class Route:
    def __init__(self, locations):
        self.locations = locations
        self.distance = self.calculate_distance()
    
    def calculate_distance(self):
        def haversine(coord1, coord2):
            lat1, lon1 = np.radians(coord1)
            lat2, lon2 = np.radians(coord2)
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
            c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
            r = 6371  # Radius of Earth in kilometers
            return r * c
        
        distance = 0.0
        for i in range(len(self.locations) - 1):
            distance += haversine(self.locations[i], self.locations[i + 1])
        distance += haversine(self.locations[-1], self.locations[0])  # Return to start
        return distance
