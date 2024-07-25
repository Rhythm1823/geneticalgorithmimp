from genetic_algorithm import GeneticAlgorithm
from visualization import plot_route, plot_progress

def display_locations(locations, labels):
    print("Available locations:")
    for i, (loc, label) in enumerate(zip(locations, labels)):
        print(f"{i}: {label} (Lat: {loc[0]}, Lon: {loc[1]})")

def get_starting_location(locations, labels):
    display_locations(locations, labels)
    while True:
        try:
            index = int(input("Enter the index of the starting location: "))
            if 0 <= index < len(locations):
                return locations[index]
            else:
                print("Invalid index. Please choose a valid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    # Delivery points (latitude, longitude)
    delivery_points = [
        (27.7172, 85.3240),  # Kathmandu
        (27.6710, 85.3240),  # Bhaktapur
        (27.6622, 85.4374),  # Patan
        (27.6943, 85.3285),  # Lalitpur
        (27.6830, 85.3192),  # Kirtipur
        (27.6923, 85.3324),  # Madhyapur Thimi
        (27.6884, 85.3423),  # Nagarjun
        (27.7223, 85.3240),  # Gokarneshwor
        (27.7182, 85.3152),  # Budhanilkantha
        (27.7046, 85.3234),  # Jorpati
        (27.7172, 85.3092),  # Teku
        (27.7110, 85.3198),  # Chabahil
        (27.6928, 85.3273),  # Sanepa
        (27.7070, 85.3236),  # Gaushala
        (27.7040, 85.3162),  # Patan Durbar Square
        (27.6901, 85.3215),  # Boudhanath Stupa
        (27.6880, 85.3370),  # Swayambhunath Stupa (Monkey Temple)
        (27.6898, 85.3245),  # Pashupatinath Temple
        (27.7172, 85.3242),  # Hanuman Dhoka
        (27.6948, 85.3202)   # Balaju
    ]

    # Labels for the delivery points
    labels = [
        "Kathmandu",
        "Bhaktapur",
        "Patan",
        "Lalitpur",
        "Kirtipur",
        "Madhyapur Thimi",
        "Nagarjun",
        "Gokarneshwor",
        "Budhanilkantha",
        "Jorpati",
        "Teku",
        "Chabahil",
        "Sanepa",
        "Gaushala",
        "Patan Durbar Square",
        "Boudhanath Stupa",
        "Swayambhunath Stupa",
        "Pashupatinath Temple",
        "Hanuman Dhoka",
        "Balaju"
    ]

    # Prompt user for starting location
    start_location = get_starting_location(delivery_points, labels)

    ga = GeneticAlgorithm(delivery_points, population_size=100, mutation_rate=0.01, elite_size=20, start_location=start_location)
    
    generations = 500
    progress = []

    for generation in range(generations):
        ga.evolve_population()
        best_route = ga.population[0]
        progress.append(best_route.distance)
        print(f'Generation {generation + 1}, Distance: {best_route.distance:.2f} km')
        print(f'Order of locations: {best_route.locations}')

    plot_route(best_route, 'Final Route', labels)
    plot_progress(progress)
