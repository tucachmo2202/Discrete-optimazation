#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import numpy as np 
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])
    if (nodeCount > 10000):
        output_data = " "
        return output_data

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    # build a trivial solution
    # visit the nodes in the order they appear in the file

    #make matrix distance
    khoang_cach = []
    for i in range(nodeCount):
        khoang_cach.append([0]*nodeCount)

    for i in range(nodeCount):
        for j in range(i+1, nodeCount):
            khoang_cach[i][j] = length(points[i], points[j])
            khoang_cach[j][i] = khoang_cach[i][j]

    chieu_dai_gen = nodeCount
    so_luong_quan_the = 200
    GenMax = 300

    def khoi_tao():
        nghiem = []
        for i in range(so_luong_quan_the):
            tp = list(np.random.permutation(chieu_dai_gen))
            nghiem.append(tp)
        return nghiem

    #Ham danh gia do thich nghi, tong khoang cach cua hanh trinh
    def danh_gia(ca_the):
        do_thich_nghi = 0
        for j in range(chieu_dai_gen-1):
            do_thich_nghi += khoang_cach[ca_the[j]][ca_the[j+1]]
        do_thich_nghi += khoang_cach[ca_the[chieu_dai_gen-1]][ca_the[0]]
        return do_thich_nghi

    #Sua chua nhung gen bi sai
    def suachua():
        pass

    def toan_tu_lai_2_diem(cha, me, p1, p2, n_test):
        child1 = cha.copy()
        sub_cha = cha[p1:p2+1]
        child2 = me.copy()
        sub_me = me[p1:p2+1]
        j_1 = 0
        j_2 = 0
        for i in range(n_test):
            if (me[i] not in sub_cha):
                child1[j_1] = me[i]
                if (j_1==p1-1):
                    j_1+=p2+1-p1+1
                else:
                    j_1+=1
            if (cha[i] not in sub_me):
                child2[j_2] = cha[i]
                if (j_2 == p1-1):
                    j_2 += p2+1-p1 +1
                else:
                    j_2+=1    
        return child1, child2

    def dot_bien(cha):
        i = np.random.randint(1, chieu_dai_gen)
        j = np.random.randint(1, chieu_dai_gen)
        child = cha.copy()
        temp = child[i]
        child[i] = child[j]
        child[j] = temp
        return child

    def sinh_quan_the(nghiem):
        cha_me_uu_tu = 0.2
        ti_le_dot_bien = 0.05
        cha_me_ngau_nhien = 0.08

        luong_cha_me_uu_tu = int(cha_me_uu_tu*len(nghiem))
        cha_me = nghiem[:luong_cha_me_uu_tu]
        no_cha_me = nghiem[luong_cha_me_uu_tu:]

        #Lay cha me ngau nhien
        for ran in no_cha_me:
            if cha_me_ngau_nhien > np.random.rand():
                cha_me.append(ran)

        #Dot bien cha me
        for ran in cha_me:
            if(ti_le_dot_bien > np.random.rand()):
                ran = dot_bien(ran)

        con_cai = []
        luong_con_cai = len(nghiem) - len(cha_me)
        while (len(con_cai) < luong_con_cai):
            me = nghiem[np.random.randint(0, len(cha_me) - 1)]
            cha = nghiem[np.random.randint(0, len(cha_me) - 1)]
            p1 = np.random.randint(2, chieu_dai_gen - 1)
            p2 = np.random.randint(1, p1)
            child1, child2 = toan_tu_lai_2_diem(cha, me, p2, p1, chieu_dai_gen)
            if (ti_le_dot_bien > np.random.rand()):
                child1 = dot_bien(child1)
            con_cai.append(child1)
            con_cai.append(child2)
            if (len(con_cai) + 1 == luong_con_cai):
                dot_bien(child2)
                con_cai.append(child2)
            
        cha_me.extend(con_cai)
        return cha_me

    def main():
        nghiem = khoi_tao()
        the_he = 1
        for gen in range(0, GenMax):
            nghiem = sorted(nghiem, key=lambda x: danh_gia(x), reverse=False)
            best = nghiem[0]
            nghiem = sinh_quan_the(nghiem)
            the_he += 1
        return best

    # solution = range(0, nodeCount)

    # isAll = (1<<nodeCount) -1
    # cost = []
    # note = []

    # if (nodeCount*(isAll + 1) > 10**8):
    #     output_data = '0' + ' ' + str(0) + '\n'
    #     #output_data += ' '.join(map(str, solution))

    # for i in range(isAll+1):
    #     cost.append([-1]*nodeCount)
    #     note.append([0]*nodeCount)

    # # calculate the length of the tour
    
    # def tsp(mask, pos):
    #     #Base_case
    #     if (mask == isAll):
    #         return dist[pos][0]
        
    #     if (cost[mask][pos]!= -1):
    #         return cost[mask][pos]    

    #     ans = 10000000000

    #     for city in range(nodeCount):
    #         if((mask&(1<<city)) == 0):
    #             newAns = dist[pos][city] + tsp(mask|(1<<city), city)
    #             if newAns < ans:
    #                 ans = newAns
    #                 note[mask][pos] = city

    #     cost[mask][pos] = ans
    #     return ans

    # def trace():
    #     taken = [0]*nodeCount
    #     S, j = 0, 0
    #     for i in range(0,nodeCount):
    #         taken[i] = note[S][j]
    #         j = taken[i]
    #         S = S | (1<<j)

    #     print(taken)
    #     return taken

    # obj = tsp(1,0)
    # solution = trace()

    nghiem = main()
    val = danh_gia(nghiem)

    # prepare the solution in the specified output format
    output_data = '%.2f' % val + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, nghiem))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

