import gurobipy as gp
import datetime
from test_input import *

def knapsack_gurobi(weights, values, capacity):
    
    ### STRUCTURE OF THE PROBLEM
    
    # Setting the first timer
    start_time1 = datetime.datetime.now()
    
    # Create a Gurobi model
    model = gp.Model("Knapsack")
    
    num_items = len(weights)
    
    # Create decision variables
    x = model.addVars(num_items, vtype=gp.GRB.BINARY, name="x")
    
    # Define the objective function
    model.setObjective(gp.quicksum(values[i] * x[i] for i in range(num_items)), gp.GRB.MAXIMIZE)
    
    # Add the capacity constraint
    model.addConstr(gp.quicksum(weights[i] * x[i] for i in range(num_items)) <= capacity)

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
    
    # Extract and print the solution
    if model.status == gp.GRB.OPTIMAL:
        print("Optimal solution found!")
        for i in range(num_items):
            if x[i].x > 0:
                print(f"Item {i} is selected.")
        total_cost = model.objVal
        print(f"Total value: {total_cost}")

    else:
        print("No optimal solution found.")

    return total_cost, running_time1, running_time2

result = knapsack_gurobi(weights, values, capacity)
print(result)
