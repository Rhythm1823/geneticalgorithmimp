# Route Optimization with Genetic Algorithm

## Overview

This project utilizes a Genetic Algorithm (GA) to optimize routes for delivery points within the Kathmandu Valley. The project calculates distances using Euclidean metrics and provides interactive visualizations of routes and optimization progress.

### Key Features

- Route optimization using Genetic Algorithm.
- Distance calculations based on Euclidean metrics.
- Interactive visualization of routes and optimization progress.
- Ability to choose the starting location from a list of delivery points.

## Prerequisites

- Python 3.x
- Required Python libraries: `numpy`, `matplotlib`

## Setup

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-username/route-optimization.git
    cd route-optimization
    ```

2. **Install Required Libraries**

    Make sure you have `pip` installed, then run:

    ```sh
    pip install numpy matplotlib
    ```

## Files and Their Responsibilities

- **`route.py`**: Defines the `Route` class, which calculates distances using Euclidean metrics.
- **`genetic_algorithm.py`**: Contains the `GeneticAlgorithm` class that handles route optimization through genetic algorithms.
- **`main.py`**: Entry point of the program. Prompts for the starting location, runs the genetic algorithm, and generates visualizations.
- **`visualization.py`**: Contains functions to plot the optimized route and the progress of the genetic algorithm.

## Usage

1. **Run the Program**

    Execute the `main.py` script:

    ```sh
    python main.py
    ```

2. **Input Prompts**

    - Choose the starting location by entering the corresponding index from the list of available locations.

3. **View Results**

    - The program will display the optimized route and its distance in kilometers.
    - Visualization plots will be shown for the final route and the optimization progress over generations.

## Example

```sh
Available locations:
0: Kathmandu (Lat: 27.7172, Lon: 85.3240)
1: Bhaktapur (Lat: 27.6710, Lon: 85.3240)
...
Enter the index of the starting location: 0
Generation 1, Distance: 15.23 km
...
