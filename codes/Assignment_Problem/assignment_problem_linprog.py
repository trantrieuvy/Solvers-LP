# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 01:01:17 2023

@author: trant
"""

import numpy as np
from scipy.optimize import linprog
import datetime

# Define the cost matrix
#cost_matrix = np.random.randint(1, 10, (4,4))

cost= np.array([[3, 7, 2, 5],[8, 2, 4, 6],[5, 3, 1, 2],[9, 6, 7, 2]])

def assignment_linprog(cost_matrix):    
    
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Convert the cost matrix into a linear programming format
    
    # Get the number of workers(rows) and tasks(columns) from the given matrix
    num_workers, num_tasks = cost_matrix.shape
    
    # To convert the cost matrix into a linear programming format, the cost matrix must be flattened into a 1D array as the cost vector c
    c = cost_matrix.flatten()
    
    # Create the equality and inequality constraint matrices
    A_eq = np.zeros((num_tasks + num_workers, num_tasks * num_workers))
    b_eq = np.ones(num_tasks + num_workers)
    for i in range(num_tasks):
        A_eq[i, i*num_workers:(i+1)*num_workers] = 1
    for j in range(num_workers):
        A_eq[num_tasks+j, j::num_workers] = 1
        
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    
    # Solve the problem
    result = linprog(c, A_eq=A_eq, b_eq=b_eq)
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2

    # Reshape the solution into the assignment matrix
    assignment_matrix = result.x.reshape(num_tasks, num_workers)
    
    # Print the optimal assignments and their costs
    for i in range(num_tasks):
        j = np.argmax(assignment_matrix[i])
        print(f"Assign task {i+1} to worker {j+1}. Cost: {cost_matrix[i, j]}")
    
    total_cost = result.fun
    print(f"Total cost: {total_cost}")
    
    return total_cost, running_time1, running_time2

result = assignment_linprog(cost)
print(result)
