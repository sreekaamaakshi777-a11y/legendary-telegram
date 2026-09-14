import math
#Distance formula: distance between two points
x1 = 3
y1 = 2
x2 = 7
y2 = 5
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The distance is",distance)
# CAN ALSO USE 
# distance = math.hypot((x2-x1), (y2-y1)) 
# OR 
# distance = ((x2 - x1)**2 + (y2 - y1)**2)**1/2