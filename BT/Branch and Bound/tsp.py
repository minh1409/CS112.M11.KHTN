import math
import random

n = int(input())
graph= []
for i in range(n):
    i = list(map(int, input(). split()))
    graph.append(i)

preco = []
for i in range(0, len(graph)):
    min1 = math.inf
    min2 = math.inf
    for j in range(0, len(graph)):
        if i == j:
            continue
        if min1 > graph[i][j]:
            min2 = min1
            min1 =  graph[i][j]
            continue
        if min2 > graph[i][j]:
            min2 =  graph[i][j]
            continue
    preco.append((min1, min2))

def cal_bound(start_vertex, prev_vertex, passed_vertex, graph):
    ret = 0
    for i in range(0, len(graph)):
        if passed_vertex[i] == 0:
            ret += (preco[i][0] + preco[i][1])/2
    ret += preco[start_vertex][0]/2
    return ret

def find(passed_vertex, current_vertex, graph, upper_bound = [math.inf], current_cost = 0):
    min_ = math.inf
    if sum(passed_vertex) == len(graph):
        return graph[current_vertex][0]
    se = list(range(0, len(graph)))
    random.shuffle(se)
    for i in se:
        if passed_vertex[i] == 0:
            passed_vertex[i] = 1
            lower_bound = cal_bound(0, current_vertex, passed_vertex, graph) + current_cost + graph[current_vertex][i]/2
            if lower_bound >= upper_bound[0]:
                passed_vertex[i] = 0
                continue
            min_ = min(find(passed_vertex, i, graph, upper_bound, current_cost + graph[current_vertex][i])
                       + graph[current_vertex][i],
                       min_)
            upper_bound[0] = min(min_ + current_cost, upper_bound[0])
            passed_vertex[i] = 0
    return min_

# print(preco)
pvtx = [0]*len(graph)
pvtx[0] = 1
print(find(pvtx, 0, graph))
