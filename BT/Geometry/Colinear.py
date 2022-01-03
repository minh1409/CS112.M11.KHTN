import math

n = int(input())
x = []
y = []
for i in range(0, n):
    x_, y_ = map(int, input().split())
    x.append(x_)
    y.append(y_)

kq = 0
for i in range(0, n - 2):
    a = []
    count = 1
    for j in range(i + 1, n):
        temp = y[j] - y[i]
        if temp == 0:
            a.append(math.inf)
        else:
            a.append((x[j] - x[i]) / temp)
    a.sort()
    for j in range(0, n - i - 2):
        if a[j] != a[j + 1]:
            kq += int(count*(count - 1) / 2)
            count = 0
        count += 1
    kq += int(count*(count - 1) / 2)

print(kq)
