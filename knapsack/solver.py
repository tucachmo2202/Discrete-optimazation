#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import namedtuple
from operator import attrgetter
from typing import  List, Tuple

def solve_it(input_data):
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []
    for i in range(item_count):
        line = lines[i+1]
        parts = line.split()
        v, w = int(parts[0]), int(parts[1])
        des = float(v) / w
        items.append([Item(i, v, w), des])

    #Sắp xếp items theo tỷ lệ value / weight
    items = sorted(items, key = lambda x : x[1])

    items = [i[0] for i in items[: : -1]]
    obj, opt, taken = search(items, capacity)
    output_data = str(obj) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

class Item:
    def __init__(self, index : int, value : int, weight : int):
        self.index = index 
        self.value = value
        self.weight = weight

#Ước tính giá trị giới hạn của 1 Node nào đó
#Đầu vào là list items, sức chưa của túi index là chỉ số của Node
def get_expectation(items : List[Item], capacity :int, index : int):
    expectation = 0.0 
    for i in range(index, len(items)):
        item = items[i]
        if capacity >= item.weight:
            expectation += item.value
            capacity -= item.weight
        else:
            expectation += float(item.value) * capacity / item.weight
            break
    return expectation

#Hàm tìm kiếm giải pháp
def search(items : List[Item], capacity : int):
    max_value = 0.0
    max_taken = [0 for i in range(len(items))]

    start_value = 0.0
    start_capacity = capacity
    start_expectation = get_expectation(items, capacity, 0)
    start_taken = [0 for i in range(len(items))]
    index = 0
    stack = []
    stack.append([start_value, start_capacity, start_expectation, start_taken, index])
    while(len(stack) != 0):
        #cur_value: tổng value tính từ root
        #cur_capacity: sức chứa còn lại của túi
        #cur_taken: mảng chứa giá các đồ vật được lấy hay không được lấy
        #Mỗi vòng lặp sẽ lấy ra 1 chuỗi các giá trị này để thực hiện ước tính

        cur_value, cur_capacity, cur_expectation, cur_taken, cur_pos = stack[-1]
        del stack[-1]
        if cur_capacity < 0:
            continue
        
        #Nếu giá trị ước tính nhỏ hơn giá trị lớn nhất hiện tại thì tìm kiếm nhánh khác
        if cur_expectation <= max_value:
            continue

        #Nếu giá trị lớn nhất hiện tại nhỏ hơn 1 giá trị được lấy ra thì đi theo nhánh đó
        if max_value < cur_value:
            max_value = cur_value
            max_taken = cur_taken
        if cur_pos >= len(items):
            continue
        cur_item = items[cur_pos]
        
        #Node đang xét không được lấy vào giải pháp
        notake_value = cur_value
        notake_capacity = cur_capacity
        notake_expectation = notake_value + get_expectation(items, notake_capacity, cur_pos + 1)
        notake_taken = cur_taken.copy()     
        stack.append([notake_value, notake_capacity, notake_expectation, notake_taken, cur_pos + 1])
        
        #Node đang xet được lấy
        take_value = cur_value + cur_item.value
        take_capacity = cur_capacity - cur_item.weight
        take_expectation = take_value + get_expectation(items, take_capacity, cur_pos + 1)
        take_taken = cur_taken.copy()
        take_taken[cur_item.index] = 1
        stack.append([take_value, take_capacity, take_expectation, take_taken, cur_pos + 1])
        
    return int(max_value), 1 , max_taken

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

