import math

def dist(pointx, pointy):
    return math.sqrt((pointx[0]-pointy[0])**2 + (pointx[1]-pointy[1])**2)

def nearest_dist(point_list):
    point_list = sorted(point_list)

    def find(point_list):
        if len(point_list) == 2:
            return dist(point_list[0], point_list[1])
        if len(point_list) == 1:
            return 1000000000000
        mid = len(point_list)//2

        point_list_left = point_list[:mid]
        point_list_right = point_list[mid:]

        result = min(nearest_dist(point_list_left), nearest_dist(point_list_right))

        point_list_revise = []
        for point in point_list:
            if (abs(point_list[mid][0] - point[0]) < result) or (abs(point_list[mid + 1][0] - point[0]) < result):
                point_list_revise.append(point)

        for i in range(0, len(point_list_revise)):
            for j in range(i+1, len(point_list_revise)):
                result = min(result, dist(point_list_revise[i], point_list_revise[j]))

        return result

    return find(point_list)


n = int(input())
lst = []

for i in range(0, n):
    temp1, temp2 = map(int, input().split())
    lst.append((temp1, temp2))

print("%.3f" % nearest_dist(lst))
