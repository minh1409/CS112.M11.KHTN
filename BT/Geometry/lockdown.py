# A Python3 program to find convex hull of a set of points. Refer
# https://www.geeksforgeeks.org/orientation-3-ordered-points/
# for explanation of orientation()

from functools import cmp_to_key

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

from functools import reduce

def convexHull(points):
    '''
    Returns points on convex hull in CCW order according to Graham's scan algorithm.
    By Tom Switzer <thomas.switzer@gmail.com>.
    '''
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) == TURN_RIGHT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


a = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    # eprint(x, y)
    a.append((x, y))

kq = 0
while True:
    a = sorted(a)
    convex_hull = convexHull(a)
    if len(convex_hull) < 3:
        break
    convex_hull = sorted(convex_hull)
    kq += 1
    pos = 0
    temp = []
    for i in range(len(a)):
        if pos < len(convex_hull) and a[i][0] == convex_hull[pos][0] and a[i][1] == convex_hull[pos][1]:
            pos += 1
        else:
            temp.append(a[i])
    a = temp

print(kq)
