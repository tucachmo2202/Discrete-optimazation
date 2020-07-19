#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import random

class Item(object):
    def __init__(self, v, w):
        self.value = v # Item's value. You want to maximize that!
        self.weight = w # Item's weight. The sum of all items should be <= CAPACITY

INF = -10000000


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    
    cost = []

    ITEMS = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        ITEMS.append(Item(int(parts[0]), int(parts[1])))

    value = [0]
    weight = [0]
    taken = [0]*(item_count+1)

    if(item_count*capacity > 10**8): #Su dung giai thuat di truyen
        CAPACITY = capacity

        # Kich thuoc quan the
        POP_SIZE = 100

        # So luong the he lon nhat
        GEN_MAX = 200

        #Lua chon khoi tao quan the bang 0 hoac random
        START_POP_WITH_ZEROES = True

        # END OF CONFIG
        ##########################################################################################

        def fitness(target):
            """
            Dau vao 1 gen tra ve tong value cua gen do, gia tri value cang lon cang tot, neu khoi luong lon hon CAPACITY thi fitness = 0
            """
            total_value = 0
            total_weight = 0
            index = 0
            for i in target:
                if index >= len(ITEMS):
                    break
                if (i == 1):
                    total_value += ITEMS[index].value
                    total_weight += ITEMS[index].weight
                index += 1
                
            
            if total_weight > CAPACITY:
                return 0
            else:
                # OK
                return total_value

        def spawn_starting_population(amount):
            return [spawn_individual() for x in range (0,amount)]

        def spawn_individual():
            if START_POP_WITH_ZEROES:
                return [random.randint(0,0) for x in range (0,len(ITEMS))]
            else:
                return [random.randint(0,1) for x in range (0,len(ITEMS))]

        def mutate(target):
            r = random.randint(0,len(target)-1)
            if target[r] == 1:
                target[r] = 0
            else:
                target[r] = 1

        def evolve_population(pop):
            parent_eligibility = 0.2 #Lay 20 % gia bo me tot nhat
            mutation_chance = 0.05 # Xac suat dot bien la 5%
            parent_lottery = 0.08  # Lay them 8% bo me bat ky

            parent_length = int(parent_eligibility*len(pop))
            parents = pop[:parent_length]
            nonparents = pop[parent_length:]

            # Lay bo me bat ki
            for np in nonparents:
                if parent_lottery > random.random():
                    parents.append(np)

            # Dot bien bo me
            for p in parents:
                if mutation_chance > random.random():
                    mutate(p)

            # Lua chon con 
            children = []
            desired_length = len(pop) - len(parents)
            while len(children) < desired_length :
                male = pop[random.randint(0,len(parents)-1)]
                female = pop[random.randint(0,len(parents)-1)] 
                half = random.randint(1,len(parents) - 1)
                child = male[:half] + female[half:] # Lay 1 nua cha, 1 nua me
                if mutation_chance > random.random():
                    mutate(child)
                children.append(child)

            parents.extend(children)
            return parents

        def opt_big():
            generation = 1
            population = spawn_starting_population(POP_SIZE)
            for g in range(0,GEN_MAX):
                population = sorted(population, key=lambda x: fitness(x), reverse=True)
                best = population[0]
                population = evolve_population(population)
                generation += 1
            return best
        taken = opt_big()
        value = fitness(taken)
        output_data = str(value) + ' ' + str(1) + '\n'
        output_data += ' '.join(map(str, taken))
        return output_data
    else: #Quy hoach dong
        for i in range(1, item_count+1):
            line = lines[i]
            parts = line.split()
            value.append(int(parts[0]))
            weight.append(int(parts[1]))

        #ma tran chi phi
        for i in range(item_count + 1):
            cost.append([0]*(capacity + 1))

        def opt():
            
            for i in range(1, item_count + 1):
                for w in range(1, capacity + 1):
                    if (weight[i] > w):
                        cost[i][w] = cost[i-1][w]
                    else:
                        cost[i][w] = max(cost[i-1][w], cost[i-1][w-weight[i]] + value[i])
            return cost[item_count][capacity]

        def trace():
            i = item_count
            j = capacity
            while (i>0 and j>0):
                if (cost[i][j] != cost[i-1][j]):
                    taken[i] = 1
                    j = j - weight[i]
                    i = i - 1
                else:
                    i = i - 1
        value = opt()
        trace()

        output_data = str(value) + ' ' + str(1) + '\n'
        output_data += ' '.join(map(str, taken[1:]))
        return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

