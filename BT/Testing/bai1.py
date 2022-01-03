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