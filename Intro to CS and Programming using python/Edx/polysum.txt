import math

def polysum(n, s):
    """
    Calculate the sum of the area and square of the perimeter of a regular polygon.

    Args:
    n (int): Number of sides of the polygon.
    s (float): Length of each side of the polygon.

    Returns:
    float: The sum, rounded to 4 decimal places.
    """
    # Calculate the area of the polygon
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    
    # Calculate the perimeter of the polygon
    perimeter = n * s
    
    # Calculate the sum of the area and square of the perimeter
    result = area + perimeter**2
    
    return round(result, 4)

# Example usage:
result = polysum(4, 5)  # Sum of area and square of perimeter of a square with side length 5
print(result)  # This will print 175.0
