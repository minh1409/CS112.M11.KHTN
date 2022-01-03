num = input()

def recursor(nums):
    for i in range(1, len(nums) // 2 + 1):
        if int(nums[0]) == 0:
            i = 1
        for j in range(i + 1, len(nums)):
            if j - i > 1 and nums[i] == '0':
                continue
            x1 = int(nums[0:i])
            x2 = int(nums[i:j])
            s = str(x1 + x2)
            if j + len(s) < len(nums) and int(s) == int(nums[j:j + len(s)]):
                if recursor(nums[i:]) == "false":
                    continue
                else:
                    return "true"
            if j + len(s) == len(nums) and int(s) == int(nums[j:j + len(s)]):
                return "true"
    return "false"


print(recursor(num))
