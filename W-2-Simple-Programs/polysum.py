import math
pi = math.pi

def polysum(n, s):
    '''
    n: int - number of sides of the polygon
    s: float - the length of each side of the polygon
    
    returns: The sum of the area and the square of the perimeter of the regular polygon, rounded to 4 decimal places.
    '''
    area = abs((0.25*n*s**2)/(math.tan(pi/n)))
    perimeter = n*s
    return float(format(area + perimeter**2, '.4f')) 


print(str(polysum(10, 1.43)))
