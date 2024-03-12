# Comparing Solvers for Linear Programming Problems

## Experiments

This project deals with comparision between different solvers for the following linear programming problems:
- Assignment Problem
- Transportation Problem
- Knapsack Problem
- Traveling Salesman Problem

The chosen solvers are from the following packages:
- Gurobi
- SciPy
- OR-Tools
- PuLP
- CVXOPT

Solving time of the solvers are measured to compare the performance of different solvers for each linear programming problem.

## Result

![Solvers for Assignment Problem](/results/assignment_plot.svg "Solvers for Assignment Problem")

![Solvers for Knapsack Problem](/results/knapsack_plot.svg "Solvers for Knapsack Problem")

![Solvers (including CVXOPT) for Transportation Problem](/results/transportation_plot_include_cvxopt.png "Solvers (including CVXOPT) for Transportation Problem")

![Solvers for Transportation Problem](/results/transportation_plot.svg "Solvers for Transportation Problem")

![Solvers for Traveling Salesman Problem](/results/tsp_plot_small.svg "Solvers for Traveling Salesman Problem")

## Authors

- [@trantrieuvy](https://www.github.com/trantrieuvy)

## Acknowledgements

 - [Solving Assignment Problem with OR-Tools](https://developers.google.com/optimization/assignment/assignment_example?hl=en)
 - [Solving Traveling Salesman Problem with OR-Tools](https://developers.google.com/optimization/routing/tsp?hl=en)
