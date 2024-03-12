# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:51:43 2023

@author: trant
"""

from cvxopt import matrix, solvers
from test_input import *
import datetime
import os
import sys


def transportation_cvxopt(supply,demand,costs):

    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    supply = list(supply)
    supply = [float(element) for element in supply]
    
    demand = list(demand)
    demand = [float(element) for element in demand]
    costs = [[float(element) for element in sublist] for sublist in costs]
    
    n_suppliers = len(supply)
    n_demands = len(demand)
    n_rows = n_demands * n_suppliers
    n_columns = n_suppliers + n_suppliers * n_demands
    
    c = ([cost for row in costs for cost in row])
    
    A = ([
        [1.0 if j == i % n_demands else 0.0 for j in range(n_demands)]
        for i in range(n_rows)
    ])
     
    G = [row for row in A[:n_demands-1] for _ in range(n_demands)]
    
    i = 0
    for row in range(len(G)):
        new_row = G[row] + [0.0] * (n_rows - 1)
        new_row[n_suppliers + i] = -1.0
        i += 1
        G[row]  = new_row
    
    h = supply + [0.0] * n_rows
    
    b = demand
    
    c = matrix(c)
    A = matrix(A)
    G = matrix(G)
    h = matrix(h)
    b = matrix(b)
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    
    sol = solvers.lp(c, G, h, A, b)
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2
    
    print(sol['x'])
    
    for i in range(n_rows):
        print('x{}={}'.format(i+1, round(sol['x'][i])))
    
    return running_time1, running_time2

result = transportation_cvxopt(supply2, demand2, costs2)
print(result)
