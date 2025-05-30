import math


# fn definition
def compute(A, B, C, D):
    # compute change in x and change in y
    Delta_y = A - B
    Delta_x = C - D
    # compute distance
    distance = math.sqrt(Delta_x ** 2 + Delta_y ** 2)
    # Compute bearing IN RADIANS
    bearing = math.atan(Delta_y / Delta_x)
   # compute in degrees
    bearing= math.degrees(bearing)
    if Delta_y < 0 and Delta_x > 0:
        direction = 360 - bearing
        if bearing < 0:
            direction = 360 + bearing
        else:direction = 360 - bearing
    elif Delta_y > 0 and Delta_x < 0:
        direction = 180 - bearing
        if bearing < 0:
            direction = 180 + bearing
        else:direction = 180 - bearing

    elif Delta_y < 0 and Delta_x < 0:
        direction = 180 + bearing
    else:
        direction = bearing
    return Delta_y, Delta_x,distance, bearing,direction


A = eval(input('Enter y1 >> '))
B = eval(input('Enter y2 >> '))
C = eval(input('Enter x1 >> '))
D = eval(input('Enter x2 >> '))

Delta_y, Delta_x,distance, bearing, direction= compute(A, B, C, D)
print(f"Delta_y is {Delta_y}")
print(f"Delta_x is {Delta_x}")
print(f"The distance is {distance}")
print(f"The bearing  is {bearing}")
print(f"The direction is {direction}")
