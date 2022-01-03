def make_list(input_str, dim):
    split_str = "]"*(dim-1) + ", "
    split_str_rep = "]"*(dim-1) + "@"
    return input_str[1 : len(input_str) - 1].replace(split_str, split_str_rep).split('@')

inp_mat = [[x[1:2] for x in make_list(x, 1)] for x in make_list(input(), 2)]
seq = input()

n = len(inp_mat)
m = len(inp_mat[0])
went = []
for i in range(0, n):
    went.append([0]*m)

def find(pos, inp_mat, seq, depth):
    if depth == len(seq):
        return "true"
    if pos[0] >= n or pos[0] < 0:
        return "false"
    if pos[1] >= m or pos[1] < 0:
        return "false"
    if went[pos[0]][pos[1]] == 1:
        return "false"
    went[pos[0]][pos[1]] = 1
    if inp_mat[pos[0]][pos[1]] != seq[depth]:
        went[pos[0]][pos[1]] = 0
        return "false"

    ret = find((pos[0] + 0, pos[1] + 1), inp_mat, seq, depth + 1)
    if ret == "true":
        went[pos[0]][pos[1]] = 0
        return "true"
    ret = find((pos[0] + 1, pos[1] + 0), inp_mat, seq, depth + 1)
    if ret == "true":
        went[pos[0]][pos[1]] = 0
        return "true"
    ret = find((pos[0] + 0, pos[1] - 1), inp_mat, seq, depth + 1)
    if ret == "true":
        went[pos[0]][pos[1]] = 0
        return "true"
    ret = find((pos[0] - 1, pos[1] + 0), inp_mat, seq, depth + 1)
    if ret == "true":
        went[pos[0]][pos[1]] = 0
        return "true"
    went[pos[0]][pos[1]] = 0
    return "false"

for i in range(0, n):
    for j in range(0, m):
        if find((i, j), inp_mat, seq, 0) == "true":
            print("true")
            exit()
print("false")
