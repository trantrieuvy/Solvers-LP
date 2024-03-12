# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:55:48 2023

@author: trant
"""

import pulp
import datetime
from test_input import *

def transportation_pulp(supply, demand, costs):
    pulp.LpSolverDefault.msg = 0
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()

    # Create a linear programming problem
    problem = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)
    
    # Define decision variables
    num_suppliers = len(supply)
    num_consumers = len(demand)
    
    x = [[pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat=pulp.LpInteger) for j in range(num_consumers)] for i in range(num_suppliers)]
    
    # Define the objective function
    problem += pulp.lpSum(costs[i][j] * x[i][j] for i in range(num_suppliers) for j in range(num_consumers))
    
    # Add supply constraints
    for i in range(num_suppliers):
        problem += pulp.lpSum(x[i][j] for j in range(num_consumers)) <= supply[i]
    
    # Add demand constraints
    for j in range(num_consumers):
        problem += pulp.lpSum(x[i][j] for i in range(num_suppliers)) >= demand[j]
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1

    ### SOLVING THE PROBLEM
     
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    # Solve the problem
    problem.solve()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2
    
    # Print the results
    print("Solution Status:", pulp.LpStatus[problem.status])
    
    for i in range(num_suppliers):
        for j in range(num_consumers):
            print(f"Units from Supplier {i+1} to Consumer {j+1}: {x[i][j].varValue}")
    total_cost = pulp.value(problem.objective)
    print("Total Cost =", total_cost)
    
    return total_cost, running_time1, running_time2

result = transportation_pulp(supply, demand, costs)
print(result)