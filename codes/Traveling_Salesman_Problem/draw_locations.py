# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:54:59 2023

@author: trant
"""

import matplotlib.pyplot as plt

locations = [(0, 0), (1, 2), (2, 2), (3, 1), (0, 2), (2, 3)]

'''
Optimal solution:
Step 1: City 0 - (0, 0)
Step 2: City 4 - (0, 2)
Step 3: City 1 - (1, 2)
Step 4: City 5 - (2, 3)
Step 5: City 2 - (2, 2)
Step 6: City 3 - (3, 1)
Step 7: City 0 - (0, 0)
'''


# Extract x and y coordinates from the list of locations
x = [location[0] for location in locations]
y = [location[1] for location in locations]

# Create a scatter plot
plt.scatter(x, y, marker='o', color='b', label='Locations')

# Add labels for each point
for i, location in enumerate(locations):
    plt.annotate(f'({location[0]}, {location[1]})', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Set labels and title
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Visualization of Locations')

# Show the plot
plt.grid(True)
plt.legend()
plt.show()
