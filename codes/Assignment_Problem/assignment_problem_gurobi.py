# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 10:47:46 2023

@author: trant
"""

import gurobipy as gp
from gurobipy import GRB 
import numpy as np 
import datetime
import os
import sys

# Assignment problem

# Define the cost matrix
# cost_matrix = np.random.randint(1, 10, (4,4))
cost = np.array([[3, 7, 2, 5], [8, 2, 4, 6], [5, 3, 1, 2], [9, 6, 7, 2]])

# Define the Solver with Gurobi

def assignment_gurobi(cost_matrix):
    ### STRUCTURE OF THE PROBLEM

    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Create a Gurobi model
    model = gp.Model()
    model.setParam('OutputFlag', False)
    
    # Get the number of workers(rows) and tasks(columns) from the given matrix
    num_workers, num_tasks = cost_matrix.shape
    
    # Create binary decision variables indicating assignment
    assignment_vars = model.addVars(num_workers, num_tasks, vtype=GRB.BINARY)
    
    # Set the objective function to minimize total cost
    model.setObjective(gp.quicksum(assignment_vars[i, j] * cost_matrix[i, j] for i in range(num_workers) for j in range(num_tasks)), GRB.MINIMIZE)
    
    # First constraint: Each task is assigned to exactly one worker
    model.addConstrs((assignment_vars.sum('*', j) == 1 for j in range(num_tasks)))
    
    # Second constraint: Each worker is assigned to at most one task
    model.addConstrs((assignment_vars.sum(i, '*') <= 1 for i in range(num_workers)))
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    
    # Solve the problem
    model.optimize()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2

    # Print the optimal assignment and total cost
    print("Optimal Assignment:")
    for i in range(num_workers):
        for j in range(num_tasks):
            if assignment_vars[i, j].x > 0:
               print(f"Task {j+1} assigned to Worker {i+1}. Cost: {cost_matrix[i, j]}")
    
    total_cost = model.objVal
    print(f"Total Cost: {total_cost}")
    
    return total_cost, running_time1, running_time2

a = assignment_gurobi(cost)
print(a)
