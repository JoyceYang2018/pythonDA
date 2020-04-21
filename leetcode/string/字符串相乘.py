def multiply(self, num1: str, num2: str) -> str:
    l1 = len(num1)
    l2 = len(num2)
    res = [0] * (l1 + l2)
    for i in range(l1 - 1, -1, -1):
        for j in range(l2 - 1, -1, -1):
            temp = int(num1[i]) * int(num2[j]) + res[i + j + 1]
            res[i + j + 1] = temp % 10
            res[i + j] = res[i + j] + temp // 10
    for i in range(l1 + l2):
        if res[i] != 0:
            return "".join([str(x) for x in res[i:]])
    return "0"
