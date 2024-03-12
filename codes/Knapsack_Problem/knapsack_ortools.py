from ortools.linear_solver import pywraplp
import datetime
from test_input import *

def knapsack_ortools(values, weights, capacity):
    
    values = [float(val) for val in values]
    weights = [float(wt) for wt in weights]
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Create the MIP solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Create binary decision variables for each item.
    num_items = len(values)
    x = [solver.IntVar(0, 1, f'x[{i}]') for i in range(num_items)]

    # Set up the objective function to maximize the total value.
    objective = solver.Objective()
    for i in range(num_items):
        objective.SetCoefficient(x[i], values[i])
    objective.SetMaximization()

    # Add the constraint for the knapsack capacity.
    capacity_constraint = solver.Constraint(0, capacity)
    for i in range(num_items):
        capacity_constraint.SetCoefficient(x[i], weights[i])
        
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()

    # Solve the problem.
    solver.Solve()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2
    
    # Get the selected items.
    selected_items = [i for i in range(num_items) if x[i].solution_value() > 0]
    print(selected_items)
    total_cost = solver.Objective().Value()

    return total_cost, running_time1, running_time2

result = knapsack_ortools(values, weights, capacity)
print(result)