import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat / 2) ** 2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

class Route:
    def __init__(self, locations):
        self.locations = locations
        self.distance = self.calculate_distance()
    
    def calculate_distance(self):
        distance = 0.0
        for i in range(len(self.locations) - 1):
            lat1, lon1 = self.locations[i]
            lat2, lon2 = self.locations[i + 1]
            distance += haversine(lat1, lon1, lat2, lon2)
        # Return to start
        lat1, lon1 = self.locations[-1]
        lat2, lon2 = self.locations[0]
        distance += haversine(lat1, lon1, lat2, lon2)
        return distance
