# Comparing Solvers for Linear Programming Problems


## Introduction

This project deals with comparision between different solvers for the following linear programming problems:
- Assignment Problem
- Transportation Problem
- Knapsack Problem
- Traveling Salesman Problem

## Preparation
1. Create virtual Python environment
  ```shell
  conda create -n LP python=3.11
  ```
2. Activate environment
  ```shell
  conda activate LP
  ```
3. Install dependencies
  ```shell
  pip install -r requirements.txt
  ```

## Experiments

The chosen solvers are from the following packages
- Gurobi
- SciPy
- OR-Tools
- PuLP
- CVXOPT

Solving time of the solvers are measured (in [codes](/codes)) to compare the performance of different solvers for each linear programming problem.


## Results

![Solvers for Assignment Problem](/results/assignment_plot.svg "Solvers for Assignment Problem")

![Solvers for Knapsack Problem](/results/knapsack_plot.svg "Solvers for Knapsack Problem")

![Solvers (including CVXOPT) for Transportation Problem](/results/transportation_plot_include_cvxopt.png "Solvers (including CVXOPT) for Transportation Problem")

Since the solving time of CVXOPT is significantly large compared to other solvers, we exclude CVXOPT to solve larger matrix sizes:
![Solvers for Transportation Problem](/results/transportation_plot.svg "Solvers for Transportation Problem")

![Solvers for Traveling Salesman Problem](/results/tsp_plot_small.svg "Solvers for Traveling Salesman Problem")


## Author

- [@trantrieuvy](https://www.github.com/trantrieuvy)


## Acknowledgements

 - [Solving Assignment Problem with OR-Tools](https://developers.google.com/optimization/assignment/assignment_example?hl=en)
 - [Solving Traveling Salesman Problem with OR-Tools](https://developers.google.com/optimization/routing/tsp?hl=en)
