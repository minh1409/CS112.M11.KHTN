n = int(input())
a = list(map(int, input(). split()))
dp = []
m = 0

for i in range(n):
    dp.append(0)
    t = 1
    for j in range(len(dp)-1):
        if a[j] < a[i]:
            t = max(dp[j] + 1, t)
    dp[len(dp)-1] = t;
    m = max(t, m)
print(m)
