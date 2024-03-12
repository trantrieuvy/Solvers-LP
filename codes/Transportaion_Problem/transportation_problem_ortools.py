from ortools.linear_solver import pywraplp
import datetime
from test_input import *

def transportation_ortools(supply, demand, cost_matrix):
    
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Define decision variables
    num_sources = len(supply)
    num_destinations = len(demand)
    
    x = {}  # Decision variables
    for i in range(num_sources):
        for j in range(num_destinations):
            x[i, j] = solver.IntVar(0, solver.infinity(), f'x[{i},{j}]')
    
    # Define the objective function (minimize transportation cost)
    solver.Minimize(solver.Sum(cost_matrix[i][j] * x[i, j] for i in range(num_sources) for j in range(num_destinations)))
    
    # Add supply and demand constraints
    for i in range(num_sources):
        solver.Add(solver.Sum(x[i, j] for j in range(num_destinations)) == supply[i])
    
    for j in range(num_destinations):
        solver.Add(solver.Sum(x[i, j] for i in range(num_sources)) == demand[j])
    
    # Find the time of setting up the problem
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1
    
    ### SOLVING THE PROBLEM
    
    # Setting the second timer
    start_time2 = datetime.datetime.now()

    # Solve the problem
    result_status = solver.Solve()
    
    # Find the time of solving the problem
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2

    # Check the status of the solver
    if result_status == pywraplp.Solver.OPTIMAL:
        print('Solution found with total cost =', solver.Objective().Value())
        for i in range(num_sources):
            for j in range(num_destinations):
                if x[i, j].solution_value() > 0:
                    print(f'Transport {x[i, j].solution_value()} units from Source {i} to Destination {j}')
    else:
        print('The problem does not have an optimal solution.')
    total_cost =  solver.Objective().Value()
    return total_cost, running_time1, running_time2

result = transportation_ortools(supply, demand, costs)
print(result)