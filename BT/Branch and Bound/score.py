s, k, n = map(int, input().split())
arr = []

for i in range(n):
    arr.append([])
    arr[i] = list(map(int, input().split()))

def thu(pos, total, prev, s, k, n, arr):
    if pos == k:
        if total == s:
            return "YES"
        return "NO"

    for i in range(n):
        if arr[i][pos] >= prev:
            test = total + arr[i][pos]
            if test <= s:
                ret = thu(pos + 1, test, arr[i][pos], s, k, n, arr)
                if ret == "YES":
                    return "YES"
    return "NO"

print(thu(0, 0, 0, s, k, n, arr))
