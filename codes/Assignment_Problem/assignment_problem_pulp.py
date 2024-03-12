# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:59:35 2023

@author: trant
"""

import numpy as np
import pulp
import datetime

# Define the cost matrix
#cost_matrix = np.random.randint(1, 10, (4,4))
cost = np.array([[3, 7, 2, 5], [8, 2, 4, 6], [5, 3, 1, 2], [9, 6, 7, 2]])

def assignment_pulp(costs):
    pulp.LpSolverDefault.msg = 0
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Define variables for the assignment
    num_workers = len(costs)
    num_tasks = len(costs[0])
    
    # Solver
    # Create a LP Minimization problem
    assignment_problem = pulp.LpProblem("Assignment_Problem", pulp.LpMinimize)
    
    # Create a binary variable for each worker-task pair
    assignment_vars = pulp.LpVariable.dicts("Assignment", ((i, j) for i in range(num_workers) for j in range(num_tasks)), cat="Binary")
    
    # Define the objective function
    assignment_problem += pulp.lpSum(costs[i][j] * assignment_vars[(i, j)] for i in range(num_workers) for j in range(num_tasks))
    
    # Constraints: Each worker is assigned to exactly one task
    for i in range(num_workers):
        assignment_problem += pulp.lpSum(assignment_vars[(i, j)] for j in range(num_tasks)) <= 1
    
    # Constraints: Each task is assigned to exactly one worker
    for j in range(num_tasks):
        assignment_problem += pulp.lpSum(assignment_vars[(i, j)] for i in range(num_workers)) == 1
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1

    ### SOLVING THE PROBLEM
     
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    
    # Solve the problem
    assignment_problem.solve()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2

    # Print the status of the problem (should be 1 - Optimal)
    print("Status:", pulp.LpStatus[assignment_problem.status])

    # Print the optimal assignment
    for i in range(num_workers):
        for j in range(num_tasks):
            if assignment_vars[(i, j)].value() == 1:
                print(f"Worker {i+1} is assigned to Task {j+1} with cost {costs[i][j]}")

    total_cost = pulp.value(assignment_problem.objective)
    # Print the total cost of the optimal assignment
    print("Total Cost:", )

    return total_cost, running_time1, running_time2

result = assignment_pulp(cost)
print(result)