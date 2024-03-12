# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:41:44 2023

@author: trant
"""

import gurobipy as gp
from gurobipy import GRB
import math
import datetime
from draw_locations import locations
import os
import sys

def tsp_gurobi(locations):

    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    def calculate_distance(loc1, loc2):
        x1, y1 = loc1
        x2, y2 = loc2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    num_cities = len(locations)
    
    # Calculate distance matrix
    distance_matrix = [[calculate_distance(locations[i], locations[j]) for j in range(num_cities)] for i in range(num_cities)]
    
    # Create a new model
    model = gp.Model("tsp")
    
    # Create binary variables representing if an arc is used
    arcs = {}
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                arcs[i, j] = model.addVar(vtype=GRB.BINARY, name=f'arc_{i}_{j}')
    
    # Create continuous variables for subtour elimination (u_i)
    u = [model.addVar(lb=2, ub=num_cities, vtype=GRB.CONTINUOUS, name=f'u_{i}') for i in range(num_cities)]
    
    # Set objective function
    model.setObjective(gp.quicksum(distance_matrix[i][j] * arcs[i, j] for i in range(num_cities) for j in range(num_cities) if i != j), GRB.MINIMIZE)

    # Add constraints
    # Each city should be visited exactly once
    for i in range(num_cities):
        model.addConstr(gp.quicksum(arcs[i, j] for j in range(num_cities) if j != i) == 1)
    
    # Each city should be left exactly once
    for i in range(num_cities):
        model.addConstr(gp.quicksum(arcs[j, i] for j in range(num_cities) if j != i) == 1)
    
    # Subtour elimination constraints Miller-Tucker-Zemlin (MTZ) 
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                if i != 0 and j != 0:
                    model.addConstr(u[i] - u[j] + (num_cities - 1) * arcs[i, j] <= num_cities - 2)
                    
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
    
    # Extract the order of visited cities
    visited_cities = [0]  # Start from city 0
    
    while True:
        current_city = visited_cities[-1]
        for j in range(num_cities):
            if j != current_city and arcs[current_city, j].x == 1:
                visited_cities.append(j)
                break
    
        if visited_cities[-1] == 0:
            break
    
    # Print the optimal solution
    print("Optimal solution:")
    for i, city in enumerate(visited_cities):
        print(f"Step {i + 1}: City {city} - {locations[city]}")

    # Return the optimal solution
    return running_time1, running_time2

# Example usage
tsp_gurobi = tsp_gurobi(locations)
