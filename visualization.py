import matplotlib.pyplot as plt
import numpy as np

def plot_route(route, title='Route', labels=None):
    locations = np.array(route.locations)
    plt.figure(figsize=(12, 8))
    plt.plot(locations[:, 0], locations[:, 1], 'o-', markersize=10, color='b')
    plt.plot([locations[-1, 0], locations[0, 0]], [locations[-1, 1], locations[0, 1]], 'o-', markersize=10, color='b')  # Return to start
    
    # Add arrows to show the direction
    for i in range(len(locations) - 1):
        plt.annotate('', xy=locations[i + 1], xytext=locations[i],
                     arrowprops=dict(facecolor='black', shrink=0.05))
    
    # Use abbreviations for labels
    if labels:
        for i, label in enumerate(labels):
            plt.text(locations[i, 0], locations[i, 1], label, fontsize=12, ha='right')
    
    plt.title(f'{title} - Distance: {route.distance:.2f} km')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.grid(True)
    plt.show()

def plot_progress(progress):
    plt.figure(figsize=(12, 8))
    plt.plot(progress, marker='o')
    plt.ylabel('Distance (km)')
    plt.xlabel('Generation')
    plt.title('Genetic Algorithm Progress')
    plt.grid(True)
    plt.show()
