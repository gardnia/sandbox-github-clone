import sys
from itertools import combinations
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def turn(v1, v2):
    result = v1.x * v2.y - v2.x * v1.y  # 1 cross 2
    if result < 0:
        return 1  # P->Q->R is a right turn
    if result > 0:
        return -1  # P->Q->R is a left turn
    return 0  # P->Q->R is a straight line, i.e. P, Q, R are collinear


sys.stdin = open('input.txt')
numTest = int(input())
for itertest in range(numTest):
    points = set()
    for i in range(int(input())):
        x, y = map(float, raw_input().split())
        points.add(Point(x, y))
    result = 0
    N = len(points)
    points = list(points)
    for i in range(N):
        for j in range(i + 1, N):
            v1 = Point(points[j].x - points[i].x,
                       points[j].y - points[i].y)
            counter = 2
            for k in range(j + 1, N):
                v2 = Point(points[k].x - points[j].x,
                           points[k].y - points[j].y)
                if not turn(v1, v2):
                    counter += 1
            result = max(result, counter)
    print 'Data set #%d contains %d gnus, out of which a maximum of %d are aligned.' %\
        (itertest + 1, N, result)
