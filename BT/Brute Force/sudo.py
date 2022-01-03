from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def sudoku_solver(table):
    unsolved = []
    cnt = [[[0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10],
           [[0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10],
           [[0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10, [0] * 10]]
    pre_computed = [[0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9]

    def backtrack(depth=0, time=[0]):
        time[0] += 1
        if time[0] >= 300000:
            return False
        if depth == len(unsolved):
            return True

        for i in range(1, 10):
            table[unsolved[depth][0]][unsolved[depth][1]] = i

            cnt[0][unsolved[depth][0]][i] ^= 1
            cnt[1][unsolved[depth][1]][i] ^= 1
            cnt[2][pre_computed[unsolved[depth][0]][unsolved[depth][1]]][i] ^= 1

            if cnt[0][unsolved[depth][0]][i] & \
                    cnt[1][unsolved[depth][1]][i] & \
                    cnt[2][(unsolved[depth][0] // 3 * 3 + unsolved[depth][1] // 3 % 3)][i]:
                if backtrack(depth + 1, time):
                    return True
                if time[0] >= 300000:
                    return False
            cnt[0][unsolved[depth][0]][i] ^= 1
            cnt[1][unsolved[depth][1]][i] ^= 1
            cnt[2][pre_computed[unsolved[depth][0]][unsolved[depth][1]]][i] ^= 1

            table[unsolved[depth][0]][unsolved[depth][1]] = 0

        return False

    for i in range(0, 9):
        for j in range(0, 9):
            pre_computed[i][j] = i // 3 * 3 + j // 3 % 3
            cnt[0][i][table[i][j]] ^= 1
            cnt[1][j][table[i][j]] ^= 1
            cnt[2][i // 3 * 3 + j // 3 % 3][table[i][j]] ^= 1

    for i in range(0, 9):
        for j in range(0, 9):
            if table[i][j] == 0:
                unsolved.append((i, j))

    return backtrack()


def main():
    table = []
    for i in range(0, 9):
        table.append(list(map(int, input().split())))
    sve = sudoku_solver(table)
    if sve == False:
        print("None")
    else:
        for row in table:
            print(*row, sep=" ")


if __name__ == "__main__":
    main()
