import math  # Import the math module for mathematical constants

# Define the function
def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    area = math.pi * (radius ** 2)  # Area formula: π * r^2
    return area  # Return the calculated area

# Call the function and display the result
radius_value = 5  # Define the radius
area_result = circle_area(radius_value)  # Call the function with the radius value

# Print the formatted output
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")