import math 
import numpy as np
import pygad

def endurance(x, y, z, u, v, w):
 return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

gene_space = [np.arange(0.0, 1.0, 0.01) for _ in range(6)]

def fitness_func(model ,solution, solution_idx):
    x = solution[0]
    y = solution[1]
    z = solution[2]
    u = solution[3]
    v = solution[4]
    w = solution[5]
    return endurance(x, y, z, u, v, w)

num_generations = 200
sol_per_pop = 10
keep_parents = 3
num_parents_mating = 5
mutation_percent_genes = 17
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
num_genes = len(gene_space)

ga_instance = pygad.GA(gene_space=gene_space,
                        num_generations=num_generations,
                        num_parents_mating=num_parents_mating,
                        fitness_func=fitness_func,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        parent_selection_type=parent_selection_type,
                        keep_parents=keep_parents,
                        crossover_type=crossover_type,
                        mutation_type=mutation_type,
                        mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

print("Best solution : {solution}".format(solution=ga_instance.best_solution()[0]))

print("Fitness value of the best solution : {solution}".format(solution=ga_instance.best_solution()[1]))


ga_instance.plot_fitness()