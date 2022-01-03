mdp = [int(-1) for i in range(200105)]
MOD = int(1e9+7)

mdp[0] = 1
mdp[1] = 1
mdp[2] = 1
mdp[3] = 1
mdp[4] = 1
mdp[5] = 1
mdp[6] = 1
mdp[7] = 1
mdp[8] = 1
mdp[9] = 2

for i in range(10, 200105):
    mdp[i] = (mdp[i - 10] % MOD + mdp[i - 9] % MOD) % MOD

def f(x, q):
    # if x == 9 and q >= 2:
    #     return mdp[q - 1] + mdp[q - 2]
    if x == 0 and q == 0:
        return 1
    return mdp[q + x - 1]

for s in [*open(0)][1:]:
    x, q = s.split()
    q = int(q)
    res = sum(f(int(ch), q) % MOD for ch in x)
    print(res % MOD)
