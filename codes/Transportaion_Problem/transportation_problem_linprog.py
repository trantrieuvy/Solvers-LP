# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:42:09 2023

@author: trant
"""

import numpy as np
from scipy.optimize import linprog
import datetime
from test_input import *

def transportation_linprog(supply, demand, costs):
    
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Constraints for supply and demand
    num_supply = len(supply)
    num_demand = len(demand)
    A_eq = np.zeros((num_supply + num_demand, num_supply * num_demand))
    for i in range(num_supply):
        A_eq[i, i * num_demand:(i + 1) * num_demand] = 1
    for j in range(num_demand):
        A_eq[num_supply + j, j::num_demand] = 1
    
    b_eq = np.concatenate([supply, demand])
    c = ([cost for row in costs for cost in row])
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    
    # Solve the problem
    result = linprog(c=c , A_eq=A_eq, b_eq=b_eq)
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2
    
    # Extract the optimal solution and reshape it
    optimal_solution = result.x
    optimal_matrix = np.reshape(optimal_solution, len(c))
    
    print("Optimal Transportation Plan:")
    print(optimal_matrix)
    total_cost = result.fun
    print("Total Cost:", total_cost)
    
    return total_cost, running_time1, running_time2
    
result = transportation_linprog(supply, demand, costs)
print(result)