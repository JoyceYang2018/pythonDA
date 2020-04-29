# 类似剪枝的技巧 其实是选择枝
def getPermutation(self, n: int, k: int) -> str:
    str_n = [str(i) for i in range(1, n + 1)]
    res = ""
    k = k - 1
    while n > 0:
        n -= 1
        a, k = divmod(k, math.factorial(n))
        res += str_n.pop(a)
    return res