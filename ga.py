from ast import List
import sys
import numpy as np
from mochilaItens import mochilaItens


def cal_pop_fitness(itensMochila: List[mochilaItens], pop):
    # Cálculo do ‘fitness’ de cada solução na população atual
    # A função ‘fitness’ calcula a soma dos produtos entre cada
    # entrada e seu peso correspondente
    points = get_points(itensMochila)
    weight = get_weight(itensMochila)

    totalsPoints = np.sum(pop * points, axis=1)
    totalsWeight = np.sum(pop * weight, axis=1)

    result = []

    for idx, points in enumerate(totalsPoints):
        if totalsWeight[idx] > 30:
            points = 0

        result.append(points)

    return result


def get_points(itensMochila: List[mochilaItens]):
    return [item.points for item in itensMochila]


def get_weight(itensMochila: List[mochilaItens]):
    return [item.weight for item in itensMochila]
def select_mating_pool(pop, fitness, num_parents):
    # Selecionar os melhores indivíduos na geração atual
    # para seren pais para cruzamento
    parents = np.empty((num_parents, pop.shape[1]))

    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -sys.maxsize - 1

    return parents


def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    # o ponto onde o cruzamento acontece entre os dois genitores
    # geramos um número aleatório entre 1 e o tamanho do cromossomo
    crossover_point = np.random.randint(1, offspring_size[1])

    for k in range(offspring_size[0]):
        # índice do primeiro genitor
        parent1_idx = k % parents.shape[0]
        # índice do segundo genitor
        parent2_idx = (k+1) % parents.shape[0]
        # o novo filho terá a primeira parte de seus genes
        # oriunda do primeiro genitor
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # o novo filho terá a segunda parte de seus genes
        # oriunda do segundo genitor
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring


def mutation(offspring_crossover, mutation_rate=0.3):
    # a mutação transforma um gene único em cada filho, aleatoriamente
    for idx in range(offspring_crossover.shape[0]):
        # a mutação só ocorrerá se dentro da 'mutation_rate' (por padrão 30%)
        if np.random.random() < mutation_rate:
            # O valor aleatório a ser adicionado
            random_idx = np.random.randint(0, offspring_crossover.shape[1])
            random_value = np.random.randint(2)
            offspring_crossover[idx, random_idx] = offspring_crossover[idx, random_idx] + random_value

    return offspring_crossover
