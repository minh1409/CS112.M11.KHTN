import math

n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
k = sum(a)
v = s % k

mdp = []
prior = [0] * n
for i in range(0, 100):
    mdp.append([1000000000]*1005)
    mdp[i][0] = 0

def dp(n, S, mdp):
    for j in range(1, S + 1):
        for i in reversed(range(n, len(a))):
            if (j - a[i]) >= 0:
                mdp[i][j] = min(mdp[i][j], mdp[i][j - a[i]] + 1)
            if i + 1 < len(a):
                mdp[i][j] = min(mdp[i][j], mdp[i + 1][j])
    return mdp[0][S]

def trace(n, S, arr, mdp):
    if S == 0:
        return
    if n == len(a) or S < 0:
        return
    if mdp[n][S - a[n]] + 1 < mdp[n+1][S]:
        arr[n] += 1
        trace(n, S - a[n], arr, mdp)
        return
    trace(n+1, S, arr, mdp)
    return

dp(0, 1000, mdp)

for i in range(0, 1000):
    # print(i)
    # if v + k*i > 3000:
    #     break
    trace(0, i, prior, mdp)

prior_sum = [prior[i] * a[i] for i in range(0, len(a))]
prior_sum_mean = sum(prior_sum)/len(prior_sum)
prior_std_deviation = 0
for i in prior_sum:
    prior_std_deviation += (i - prior_sum_mean)*(i - prior_sum_mean)
prior_std_deviation /= len(prior_sum)
prior_std_deviation = math.sqrt(prior_std_deviation)
prior_sum = [(prior_sum[i] - prior_sum_mean)/prior_std_deviation for i in range(0, len(prior_sum))]

# print(prior)
for i in range(0, len(prior)):
    if prior_sum[i] < 0:
        prior[i] = 0

block_size = sum(prior)
prior = [prior[i] * a[i] for i in range(0, len(a))]
block_value = sum(prior)

# print(prior_sum)
new_a = [x for y, x in sorted(zip(prior_sum, a), reverse=True)]
while(len(new_a)>20):
    new_a.pop()
new_n = len(new_a)
#
# print(new_a)

def huyhoang(n, s, a):
    a.sort()

    # Recursive
    d = [int(-1) for i in range(10105)]

    def sol(s, a, n):
        if s == 0:
            return 0
        if s < a[0]:
            return (int)(1e9)
        if d[s] != -1:
            return d[s]

        res = (int)(1e9)
        for i in range(n - 1, -1, -1):
            if s >= a[i]:
                res = min(res, sol(s - a[i], a, n))
        d[s] = res + 1
        return d[s]

    # Greedy
    val = a[n - 1] * 100
    res = (s - val) // a[n - 1]
    if res < 0:
        res = 0
    s -= res * a[n - 1]

    res += sol(s, a, n)
    return res

print(huyhoang(new_n, s, new_a))
