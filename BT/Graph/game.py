n, m = map(int, input().split())

arr = [[] for i in range(m + n)] 
temp = n

for e in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    if z:
        arr[x].append(temp)
        arr[y].append(temp)
        arr[temp].append(x)
        arr[temp].append(y)
        temp += 1
    else:
        arr[x].append(y)
        arr[y].append(x)

colored = [(-1) for i in range(temp + 1)]

def bfs(u):
    queue = []
    queue.append(u)
    
    while len(queue):
        u = queue.pop(0)
        for v in arr[u]:
            if colored[v] == -1:
                colored[v] = colored[u] ^ 1
                queue.append(v)
            else:
                if colored[v] == colored[u]:
                    return False    

    return True
 
result = True
for u in range(n):
    if colored[u] == -1:
        colored[u] = 0
        result &= bfs(u)

if result:
    print("NO") 
else:
    print("YES")
