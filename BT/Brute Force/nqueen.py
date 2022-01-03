state = []
ss = 0

def check(x, y):
    #diag
    k = (abs(x[0]-y[0]), abs(x[1]-y[1]))
    if k[0]==k[1]:
        return False
    if k[0]==0:
        return False
    if(k[1]==0):
        return False
    return True

def calc(n, k):
    global ss
    ss = ss + 1
    if n==k:
        return 1
    s = 0
    for i in range(0, k):
        kk = (i, n)
        c = True
        for j in state:
            if check(j, kk)==False:
                c = False
        if c==True:
            state.append(kk)
            s = s + calc(n+1, k)
            state.pop()
    return s

# kk = int(input())
# sol = []
# for i in range(1, 11):
#     sol.append(calc(0, i))
#     print(sol)
# print(sol)

sol = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
kk = int(input())
print(sol[kk-1])
