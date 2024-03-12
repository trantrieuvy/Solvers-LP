# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:25:40 2023

@author: trant
"""
import pulp
import datetime
from test_input import *


def knapsack_pulp(values, weights, capacity):
        
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    knapsack_problem = pulp.LpProblem("Knapsack Problem", pulp.LpMaximize)
    
    # Define decision variables
    items = range(len(weights))
    x = pulp.LpVariable.dicts("Item", items, lowBound=0, upBound = 1, cat=pulp.LpInteger)
    
    # Add the objective function
    knapsack_problem += pulp.lpSum([values[i] * x[i] for i in items])
    
    # Add the constraint for the knapsack capacity
    knapsack_problem += pulp.lpSum([weights[i] * x[i] for i in items]) <= capacity
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()

    # Solve the problem
    knapsack_problem.solve()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2

    # Print the solution
    if pulp.LpStatus[knapsack_problem.status] == "Optimal":
        print("Solution found:")
        for i in items:
            if x[i].value() == 1:
                print(f"Item {i} is selected (Weight: {weights[i]}, Value: {values[i]})")
    total_cost = pulp.value(knapsack_problem.objective)

    return total_cost, running_time1, running_time2
        
result = knapsack_pulp(values, weights, capacity)
print(result)