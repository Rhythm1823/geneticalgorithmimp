import random
from route import Route

class GeneticAlgorithm:
    def __init__(self, locations, population_size, mutation_rate, elite_size, start_location=None):
        self.locations = locations
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.elite_size = elite_size
        self.start_location = start_location
        self.population = self.initialize_population()
    
    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            if self.start_location:
                remaining_locations = [loc for loc in self.locations if loc != self.start_location]
                random_route = [self.start_location] + random.sample(remaining_locations, len(remaining_locations))
            else:
                random_route = random.sample(self.locations, len(self.locations))
            population.append(Route(random_route))
        return population
    
    def evolve_population(self):
        new_population = self.select_elite()
        while len(new_population) < self.population_size:
            parent1 = self.tournament_selection()
            parent2 = self.tournament_selection()
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        self.population = new_population
    
    def select_elite(self):
        self.population.sort(key=lambda x: x.distance)
        return self.population[:self.elite_size]
    
    def tournament_selection(self):
        tournament = random.sample(self.population, 5)
        tournament.sort(key=lambda x: x.distance)
        return tournament[0]
    
    def crossover(self, parent1, parent2):
        child_locations = [None] * len(parent1.locations)
        start_pos = random.randint(0, len(parent1.locations) - 1)
        end_pos = random.randint(start_pos, len(parent1.locations))
        
        for i in range(start_pos, end_pos):
            child_locations[i] = parent1.locations[i]
        
        parent2_index = 0
        for i in range(len(child_locations)):
            if child_locations[i] is None:
                while parent2.locations[parent2_index] in child_locations:
                    parent2_index += 1
                child_locations[i] = parent2.locations[parent2_index]
        
        return Route(child_locations)
    
    def mutate(self, route):
        for swapped in range(len(route.locations)):
            if random.random() < self.mutation_rate:
                swap_with = int(random.random() * len(route.locations))
                loc1 = route.locations[swapped]
                loc2 = route.locations[swap_with]
                route.locations[swapped], route.locations[swap_with] = loc2, loc1
        route.distance = route.calculate_distance()
