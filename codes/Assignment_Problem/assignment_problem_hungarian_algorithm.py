# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:02:23 2023

@author: trant
"""

from scipy.optimize import linear_sum_assignment
import datetime
import numpy as np

# Assignment problem

# Define the cost matrix
# cost_matrix = np.random.randint(1, 10, (4,4))
cost = np.array([[3, 7, 2, 5], [8, 2, 4, 6], [5, 3, 1, 2], [9, 6, 7, 2]])

# Define the Solver with Hungarian Algorithm
def assignment_hungarian_algorithm(cost_matrix):    
    # Running time for setting up the problem here is 0
    running_time1 = 0
    
    # Setting the timer
    start_time = datetime.datetime.now()
    
    # Solve the assignment problem using linear_sum_assignment
    row_indices, col_indices = linear_sum_assignment(cost_matrix)

    # Find the time of solving the problem
    end_time = datetime.datetime.now()
    running_time2 = end_time - start_time
    
    # Print the optimal assignments and total cost
    for i, j in zip(row_indices, col_indices):
        print(f"Task {i+1} assigned to Worker {j+1}. Cost: {cost_matrix[i, j]}")
    
    total_cost = cost_matrix[row_indices, col_indices].sum()
    print(f"Total cost: {total_cost}")

    return total_cost, running_time1, running_time2

result = assignment_hungarian_algorithm(cost)
print(result)