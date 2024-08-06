import matplotlib.pyplot as plt
import numpy as np

def plot_route(route, title='Route', labels=None):
    locations = np.array(route.locations)
    plt.figure(figsize=(12, 8))
    
    # Plot the route connecting the points
    plt.plot(locations[:, 0], locations[:, 1], 'o-', markersize=10, color='b', linewidth=2)  # Blue lines connecting the points
    plt.plot([locations[-1, 0], locations[0, 0]], [locations[-1, 1], locations[0, 1]], 'o-', markersize=10, color='b', linewidth=2)  # Return to start
    
    # Highlight the start node
    plt.plot(locations[0, 0], locations[0, 1], 'ro', markersize=12, label='Start Node')  # Red color for the start node
    
    if labels:
        for i, label in enumerate(labels):
            plt.text(locations[i, 0], locations[i, 1], label, fontsize=12, ha='right', va='bottom')
    
    plt.title(f'{title} - Distance: {route.distance:.2f} km')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_progress(progress):
    plt.figure(figsize=(12, 8))
    plt.plot(progress, color='g', marker='o', linestyle='-', linewidth=2)
    plt.ylabel('Distance (km)')
    plt.xlabel('Generation')
    plt.title('Genetic Algorithm Progress')
    plt.grid(True)
    plt.show()
