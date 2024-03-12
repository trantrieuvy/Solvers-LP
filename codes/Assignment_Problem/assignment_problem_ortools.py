# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:24:01 2023

@author: trant

Mostly copied from https://developers.google.com/optimization/assignment/assignment_example?hl=en
"""

from ortools.linear_solver import pywraplp
import datetime
import numpy as np

# Define the cost matrix
#cost_matrix = np.random.randint(1, 10, (4,4))
cost = np.array([[3, 7, 2, 5], [8, 2, 4, 6], [5, 3, 1, 2], [9, 6, 7, 2]])

def assignment_ortools(cost_matrix):
    
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    num_workers = len(cost_matrix)
    num_tasks = len(cost_matrix[0])

    # Solver
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:
        return

    # Variables
    # x[i, j] is an array of 0-1 variables, which will be 1
    # if worker i is assigned to task j.
    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = solver.IntVar(0, 1, "")

    # Constraints
    # Each worker is assigned to at most 1 task.
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) == 1)

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) <= 1)

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(cost_matrix[i][j] * x[i, j])
    solver.Minimize(solver.Sum(objective_terms))
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1

    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()
    
    # Solve the problem
    status = solver.Solve()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        total_cost = solver.Objective().Value()
        print(f"Total cost = {total_cost}\n")
        for i in range(num_workers):
            for j in range(num_tasks):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if x[i, j].solution_value() > 0.5:
                    print(f"Worker {i} assigned to task {j}." + f" Cost: {cost_matrix[i][j]}")
    else:
        print("No solution found.")
        
    return total_cost, running_time1, running_time2


result = assignment_ortools(cost)
print(result)