import numpy as np
import pygad
import time

# Labirynt jako macierz, gdzie 0 oznacza puste pole, a 1 oznacza ścianę.
labirynt = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0,0,1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1,0,1],
    [1, 0, 0, 0, 1, 0, 1, 0,0, 0,0,1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1,0,1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0,0,1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0,1,1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0,0,1],
    [1, 0, 1, 1, 1, 0, 0,0, 1, 1,0,1],
    [1, 0, 1, 0,1, 1, 0, 1, 0,1,0,1],
    [1, 0, 1, 0, 0,0, 0, 0,0, 0,0,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1],
])

# Początkowe położenie agenta.
start = (1, 1)
end = (10, 10)

def fitness_func(model, solution, solution_idx):
    x, y = start
    penalty = 0 
    for direction in solution:
        new_x, new_y = start
        if direction == 0:
            new_x += 1
        elif direction == 1:
            new_x -= 1
        elif direction == 2:
            new_y += 1
        elif direction == 3:
            new_y -= 1
        if x < 0 or x >= labirynt.shape[0] or y < 0 or y >= labirynt.shape[1] or labirynt[x, y] == 1:
            penalty +=  1e-6
        else:
            x, y = new_x, new_y
        if (x, y) == end:
            return 1e3 - penalty
    distance = np.sqrt((x - end[0])**2 + (y - end[1])**2)
    return 1 / (1 + distance) + max(0, (1 - distance / 10)) - penalty

fitness_function = fitness_func

num_generations = 1000
sol_per_pop = 50
keep_parents = 3
num_parents_mating = 5
mutation_percent_genes = 1
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
num_genes = len(labirynt) * len(labirynt[0])

gene_space = [0, 1, 2, 3] # 0 - prawo, 1 - lewo, 2 - góra, 3 - dół

def on_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Best solution : {solution}".format(solution=ga_instance.best_solution()[1]))
    # print("Route: ", ga_instance.best_solution()[0])

ga_instance = pygad.GA(gene_space=gene_space,
                          num_generations=num_generations,
                          num_parents_mating=num_parents_mating,
                          fitness_func=fitness_function,
                          sol_per_pop=sol_per_pop,
                          num_genes=num_genes,
                          on_generation= on_generation,
                          parent_selection_type=parent_selection_type,
                          keep_parents=keep_parents,
                          crossover_type=crossover_type,
                          mutation_type=mutation_type,
                          mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

print("Best solution : {solution}".format(solution=ga_instance.best_solution()[0]))

print("Fitness value of the best solution : {solution}".format(solution=ga_instance.best_solution()[1]))  

ga_instance.plot_fitness()





