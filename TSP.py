import random

# cities and their coordinates
cities = [[35, 51], [113, 213], [82, 280], [322, 340], [256, 352],
          [160, 24], [322, 145], [12, 349], [282, 20], [241, 8],
          [398, 153], [182, 305], [153, 257], [275, 190], [242, 75],
          [19, 229], [303, 352], [39, 309], [383, 79], [226, 343]]


def distance(city1, city2):
    # Euclidean distance between two cities
    x_diff = city1[0] - city2[0]
    y_diff = city1[1] - city2[1]
    return ((x_diff ** 2) + (y_diff ** 2)) ** 0.5


def total_distance(path):
    # the total distance of a given path
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(cities[path[i]], cities[path[i + 1]])
    return dist


def generate_random_path(n):
    # Generate a random path of cities
    path = list(range(n))
    random.shuffle(path)
    return path


def generate_population(pop_size, n):
    # Generate a population of random paths
    population = []
    for _ in range(pop_size):
        population.append(generate_random_path(n))
    return population


def sort_paths(population):
    # Sort the paths by their total distance
    return sorted(population, key=lambda x: total_distance(x))


def breed(parent1, parent2):
    # Create a new offspring by combining the paths of two parents
    offspring = []
    for i in range(len(parent1)):
        if i < len(parent1) / 2:
            offspring.append(parent1[i])
        else:
            offspring.append(parent2[i])
    return offspring


def mutate(path):
    # Randomly swap two cities in the path
    i, j = random.sample(range(len(path)), 2)
    path[i], path[j] = path[j], path[i]
    return path


def next_generation(population, elite_size, mutation_rate):
    # Generate the next generation of paths
    elite = population[:elite_size]
    non_elite = population[elite_size:]
    random.shuffle(non_elite)

    next_gen = []
    for i in range(0, len(non_elite) - 1, 2):
        offspring = breed(non_elite[i], non_elite[i + 1])
        next_gen.append(offspring)

    for path in next_gen:
        if random.random() < mutation_rate:
            path = mutate(path)

    return elite + next_gen


def genetic_algorithm(pop_size, elite_size, mutation_rate, generations):
    # Initialize the population
    population = generate_population(pop_size, len(cities))
    for i in range(generations):
        population = sort_paths(population)
        population = next_generation(population, elite_size, mutation_rate)

    # Return the shortest path
    return population[0]


# Example
best_path = genetic_algorithm(100, 20, 0.01, 200)
print("Best Path: ", best_path)
print("Total Distance: ", total_distance(best_path))
