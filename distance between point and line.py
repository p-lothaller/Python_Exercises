import math
# Returns the distance between 2 2D points
def distance(x1, y1, x2, y2):
  return math.sqrt((x2-x1)**2+(y2-y1)**2)


# Returns the area of the triangle with sides a, b and c
def area(a, b, c):
  s = (a+b+c)/2
  A = math.sqrt(s*(s-a)*(s-b)*(s-c))
  return A


# Returns the distance between the point (px, py) and the line between (s1x, s1y) and (s2x, s2y)
def point_line_dist(s1x, s1y, s2x, s2y, px, py):
    base = distance(s1x, s1y, s2x, s2y)
    side1 = distance(s1x, s1y, px, py)
    side2 = distance(px, py, s2x, s2y)
    Area = area(base, side1, side2)
    height = (2*Area)/base
    return height

print(point_line_dist(23, -23, 13, 214, 7, 8))
