Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
import numpy as np

# Define the structured data type
dtype = np.dtype([
    ('position', [('x', float), ('y', float)]),  # Nested tuple for (x, y)
    ('color', [('r', int), ('g', int), ('b', int)])  # Nested tuple for (r, g, b)
])

# Create an array with sample values
points = np.array([
    ((1.5, 2.0), (255, 0, 0)),   # Red point at (1.5, 2.0)
    ((3.2, 4.1), (0, 255, 0)),   # Green point at (3.2, 4.1)
    ((5.0, 6.7), (0, 0, 255))    # Blue point at (5.0, 6.7)
], dtype=dtype)

# Print the structured array
print(points)

# Access individual elements
print("\nFirst point position:", points[0]['position'])
print("First point color:", points[0]['color'])

import numpy as np

# Create a NumPy array of integers from 1 to 10 (inclusive)
arr = np.arange(1, 11)

# Calculate the square of each element in the array
squared_arr = np.square(arr)

# Calculate the sum, mean, and standard deviation of the squared array
sum_squared = np.sum(squared_arr)
mean_squared = np.mean(squared_arr)
std_dev_squared = np.std(squared_arr)

# Display results
print("Sum of squared array:", sum_squared)
print("Mean of squared array:", mean_squared)
print("Standard Deviation of squared array:", std_dev_squared)
