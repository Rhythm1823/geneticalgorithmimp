import random
import numpy as np
import time
from genetic_algorithm import GeneticAlgorithm
from visualization import plot_route, plot_progress
from delivery_points import DELIVERY_POINTS, LABELS

def main():
    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    # Display available locations
    print("Available locations:")
    for idx, label in enumerate(LABELS):
        print(f"{idx + 1}. {label}")
    
    # Prompt user for starting location
    start_idx = int(input("Enter the number of the starting location: ")) - 1
    start_location = DELIVERY_POINTS[start_idx]
    
    # Reorder delivery points to start from the chosen location
    delivery_points = [DELIVERY_POINTS[start_idx]] + [pt for i, pt in enumerate(DELIVERY_POINTS) if i != start_idx]
    labels = [chr(65 + start_idx)] + [chr(65 + i) for i in range(len(DELIVERY_POINTS)) if i != start_idx]
    
    # Create a mapping for the abbreviations
    label_mapping = {chr(65 + i): LABELS[i] for i in range(len(LABELS))}
    
    # Set the parameters
    population_size = 200
    mutation_rate = 0.01
    elite_size = 20
    crossover_rate = 0.6
    
    # Initialize Genetic Algorithm
    ga = GeneticAlgorithm(delivery_points, population_size, mutation_rate, elite_size, crossover_rate)
    
    generations = 50
    progress = []
    
    # Start time
    start_time = time.time()
    
    for generation in range(generations):
        ga.evolve_population()
        best_route = ga.population[0]
        progress.append(best_route.distance)
        print(f'Generation {generation + 1}, Distance: {best_route.distance:.2f} km')
    
    # End time
    end_time = time.time()
    
    # Total computation time
    computation_time = end_time - start_time
    print(f'Total computation time: {computation_time:.2f} seconds')
    
    # Plot results
    plot_route(best_route, 'Final Route', labels)
    plot_progress(progress)
    
    # Print the label mapping for reference
    print("\nLabel Mapping:")
    for abbr, full_name in label_mapping.items():
        print(f"{abbr} = {full_name}")

    # Print the order of nodes visited in the best route with labels
    print("\nOrder of nodes visited in the best route:")
    for loc in best_route.locations:
        # Find the index of the location in DELIVERY_POINTS
        idx = DELIVERY_POINTS.index(loc)
        # Print the label and original name for the location
        label = chr(65 + idx)
        original_name = LABELS[idx]
        print(f"{label} = {original_name}")

if __name__ == "__main__":
    main()
