# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:36:17 2023

@author: trant

codes based on https://developers.google.com/optimization/routing/tsp?hl=en
"""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import datetime
from draw_locations import locations


def create_data_model(locations):
    data = {}
    data['locations'] = locations
    data['num_locations'] = len(locations)
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def compute_euclidean_distance(location1, location2):
    return ((location1[0] - location2[0])**2 + (location1[1] - location2[1])**2)**0.5

def create_distance_matrix(data):
    num_locations = data['num_locations']
    distance_matrix = [[0] * num_locations for _ in range(num_locations)]
    
    for from_node in range(num_locations):
        for to_node in range(num_locations):
            if from_node == to_node:
                distance_matrix[from_node][to_node] = 0
            else:
                distance_matrix[from_node][to_node] = int(compute_euclidean_distance(data['locations'][from_node], data['locations'][to_node]) + 0.5)
    
    return distance_matrix

def print_solution(manager, routing, solution):
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    print('Route distance: {}'.format(route_distance))

def tsp_ortools(locations):
    # Structure of the problem
    start_time1 = datetime.datetime.now()
    
    data = create_data_model(locations)

    distance_matrix = create_distance_matrix(data)

    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    end_time1 = datetime.datetime.now()
    running_time1 = end_time1 - start_time1

    # Solving the problem
    start_time2 = datetime.datetime.now()

    solution = routing.SolveWithParameters(search_parameters)
    
    end_time2 = datetime.datetime.now()
    running_time2 = end_time2 - start_time2
    if solution:
        print_solution(manager, routing, solution)
    return running_time1, running_time2

tsp_ortools = tsp_ortools(locations)