import pygad 
import numpy
import time

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def createItemList ():
    items = []
    items.append(Item("zegar", 7, 100))
    items.append(Item("obraz-pejzaż", 7, 300))
    items.append(Item("obraz-portret", 6, 200))
    items.append(Item("radio", 4, 40))
    items.append(Item("laptop", 5, 500))
    items.append(Item("lampka nocna", 6, 70))
    items.append(Item("srebrne sztućce", 1, 100))
    items.append(Item("porcelana", 3, 250))
    items.append(Item("figura z brazu", 10, 300))
    items.append(Item("skorzana torebka", 3, 280))
    items.append(Item("odkurzacz", 15, 300))
    return items

items = createItemList()

def fitness_func(model, solution, solution_idx):
    total_weight = 0
    total_value = 0
    for i in range(len(items)):
        if solution[i] == 1:
            total_weight += items[i].weight
            total_value += items[i].value
    if total_weight > 25:
        total_value = -total_value
    return total_value

fitness_function = fitness_func

num_generations = 150
sol_per_pop = 10
keep_parents = 3
num_parents_mating = 5
mutation_percent_genes = 8
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
num_genes = len(items)

gene_space = [0, 1]

# ga_instance = pygad.GA(gene_space=gene_space,
#                           num_generations=num_generations,
#                           num_parents_mating=num_parents_mating,
#                           fitness_func=fitness_function,
#                           sol_per_pop=sol_per_pop,
#                           num_genes=num_genes,
#                           parent_selection_type=parent_selection_type,
#                           keep_parents=keep_parents,
#                           crossover_type=crossover_type,
#                           mutation_type=mutation_type,
#                           mutation_percent_genes=mutation_percent_genes)

# ga_instance.run()


successful_attemps = 0
avarage_time = 0
# avarage_generations = 0
for _ in range(10):
    ga_instance = pygad.GA(gene_space=gene_space,
                          num_generations=num_generations,
                          num_parents_mating=num_parents_mating,
                          fitness_func=fitness_function,
                          sol_per_pop=sol_per_pop,
                          num_genes=num_genes,
                          parent_selection_type=parent_selection_type,
                          keep_parents=keep_parents,
                          crossover_type=crossover_type,
                          mutation_type=mutation_type,
                          mutation_percent_genes=mutation_percent_genes
                          )

    start_time = time.time()
    # for generation in range(num_generations):
    #     ga_instance.run()
    #     if ga_instance.best_solution()[1] == 1630:
    #         avarage_generations += ga_instance.generations_completed
    #         break
    ga_instance.run()
    end_time = time.time()
    if ga_instance.best_solution()[1] == 1630:
        successful_attemps += 1
        avarage_time += end_time - start_time


print("Successful attemps: ", (successful_attemps / 10) * 100, "%")
print("Avarage time: ", avarage_time / 10, "s")
# print("Avarage generations: ", avarage_generations / 10)

# solution, solution_fitness, solution_idx = ga_instance.best_solution()

# print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

# print("Items to pick:")
# for i in range(len(items)):
#     if solution[i] == 1:
#         print(items[i].name)

# ga_instance.plot_fitness()




