import random
import networkx as nx
import numpy as np
import os

randNum = lambda l, r: random.randint(l, r)
randArr = lambda n, l, r: [randNum(l, r) for i in range(0, n)]
alphabet = "qwertyuiopasdfghjklzxcvbnm"
randStr = lambda n: ''.join(map(str, [alphabet[randNum(0, len(alphabet)-1)] for i in range(0,n)]))
randTree = lambda n: nx.convert.to_edgelist(nx.random_tree(n, int(1/random.random())))
def randGraph(number_of_node, density):
    res = []
    for i in range(0, number_of_node):
        for j in range(i+1, number_of_node):
            if(random.random()<density):
                res.append((i, j))
    return res

def genTest():
    f = None
    try:
        f = open("bai2_input.inp", "x")
    except:
        os.remove("bai2_input.inp")
        f = open("bai2_input.inp", "x")
    num_of_node = None
    graph = randGraph(num_of_node:=random.randint(10,100), 0.1)
    random.shuffle(graph)
    s = random.randint(0,num_of_node-1)
    d = random.randint(0,num_of_node-1)
    while s==d:
        d = random.randint(0, num_of_node - 1)
    f.write(str(num_of_node) + " " + str(len(graph)) + " " + str(s) + " " + str(d) + "\n")
    for i in graph:
        f.write(str(i[0]) + " " + str(i[1]) + "\n")
    f.close()
    return graph

def check():
    # graph = genTest()
    # exec(open('solve.py').read())
    graph = []
    s, d = None, None
    with open("bai2_input.inp", "r") as f:
        s, s, s, d = [int(x) for x in next(f).split()]
        for line in f:
            ed = [int(x) for x in line.split()]
            graph.append((ed[0], ed[1]))

    ans = None
    with open("bai2_output.out", "r") as f:
        ans = [int(x) for x in next(f).split()]

    edge = set()
    edge.update(graph)
    for i in range(0, len(graph)):
        graph[i] = (graph[i][1], graph[i][0])
    edge.update(graph)

    for vertex_index in range(1,len(ans)):
        if (ans[vertex_index], ans[vertex_index-1]) not in edge:
            return False

    cycle_checker = set()
    for vertex in ans:
        if vertex in cycle_checker:
            return False
        cycle_checker.add(vertex)


    if s!=ans[0] or d!=ans[len(ans)-1]:
        return False

    return True

if check()==True:
    print("Correct")
else:
    print("Incorrect")


