#!/usr/bin/python
# -*- coding: utf-8 -*-
from ortools.sat.python import cp_model
import numpy as np 
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    model = cp_model.CpModel()
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = [] 
    taken = []
    result = 0
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i, int(parts[0]), int(parts[1])))
    # create variable 
    x = [model.NewIntVar(0,1,"%i") for i in range(item_count)]
    # create constraint 
    sum_weight = 0
    for i in range(item_count):
        sum_weight += x[i]*items[i].weight
    # add constraints
    model.Add(sum_weight<=capacity)
    sum_value = 0
    for i in range(item_count):
        sum_value += items[i].value *x[i]
    model.Maximize(sum_value)
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status== cp_model.OPTIMAL:
       # print("max is %i"%solver.ObjectiveValue())
        result = solver.ObjectiveValue()
        for i in range(item_count):
           # print(solver.Value(x[i]))
            taken.append(solver.Value(x[i]))
    output_data = str(int(result))+ ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
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

