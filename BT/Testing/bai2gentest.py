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

