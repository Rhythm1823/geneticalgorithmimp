import matplotlib.pyplot as plt
import numpy as np

def plot_route(route, title='Route', labels=None):
    """
    Plots the route on a 2D plane and shows the distance traveled.

    :param route: Route object containing the locations and distance
    :param title: Title of the plot
    :param labels: List of labels for the locations
    """
    locations = np.array(route.locations)
    plt.figure(figsize=(10, 6))
    plt.plot(locations[:, 1], locations[:, 0], 'o-', markersize=10)
    plt.plot([locations[-1, 1], locations[0, 1]], [locations[-1, 0], locations[0, 0]], 'o-', markersize=10)  # Return to start
    if labels:
        for i, label in enumerate(labels):
            plt.text(locations[i, 1], locations[i, 0], label, fontsize=12, ha='right')
    plt.title(f'{title} - Distance: {route.distance:.2f} km')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()

def plot_progress(progress):
    """
    Plots the progress of the genetic algorithm over generations.

    :param progress: List of distances representing the progress
    """
    plt.figure(figsize=(10, 6))
    plt.plot(progress, marker='o', linestyle='-', color='r')
    plt.ylabel('Distance (km)')
    plt.xlabel('Generation')
    plt.title('Genetic Algorithm Progress')
    plt.grid(True)
    plt.show()
