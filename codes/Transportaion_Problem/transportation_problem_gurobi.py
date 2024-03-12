# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:41:38 2023

@author: trant
"""

import gurobipy as gp
import datetime
from test_input import *

def transportation_gurobi(supply, demand, cost_matrix):
    
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Create a Gurobi model
    model = gp.Model("TransportationProblem")
    
    # Create decision variables
    num_supply = len(supply)
    num_demand = len(demand)
    
    x = {}
    for i in range(num_supply):
        for j in range(num_demand):
            x[(i, j)] = model.addVar(vtype=gp.GRB.CONTINUOUS, name=f"x_{i}_{j}")
    
    # Set the objective function
    model.setObjective(
        gp.quicksum(cost_matrix[i][j] * x[(i, j)] for i in range(num_supply) for j in range(num_demand)),
        sense=gp.GRB.MINIMIZE
    )
    
    # Supply constraints
    for i in range(num_supply):
        model.addConstr(gp.quicksum(x[(i, j)] for j in range(num_demand)) <= supply[i], f"Supply_{i}")
    
    # Demand constraints
    for j in range(num_demand):
        model.addConstr(gp.quicksum(x[(i, j)] for i in range(num_supply)) >= demand[j], f"Demand_{j}")
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    
    # Optimize the model
    model.optimize()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2
    
    # Print the optimal solution
    if model.status == gp.GRB.OPTIMAL:
        print("Optimal Solution Found:")
        for i in range(num_supply):
            for j in range(num_demand):
                if x[(i, j)].x > 0:
                    print(f"Ship {x[(i, j)].x} units from Supplier {i} to Customer {j}")
        total_cost = model.objVal
        print(f"Total Cost: {total_cost}")

    else:
        print("No optimal solution found.")

    return total_cost, running_time1, running_time2

result = transportation_gurobi(supply, demand, costs)
print(result)