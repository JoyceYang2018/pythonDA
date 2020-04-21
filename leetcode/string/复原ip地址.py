# 暴力破解法
def restoreIpAddresses(self, s: str) -> List[str]:
    def helper(s):
        if not s or (s.startswith('0') and len(s) > 1) or int(s) > 255:
            return False
        return True

    l = len(s)
    res = []
    for i in range(3):
        for j in range(i + 1, i + 4):
            for k in range(j + 1, j + 4):
                if i < l and j < l and k < l:
                    temp1 = s[:i + 1]
                    temp2 = s[i + 1: j + 1]
                    temp3 = s[j + 1: k + 1]
                    temp4 = s[k + 1:]
                    if all(map(helper, [temp1, temp2, temp3, temp4])):
                        res.append(".".join([str(s) for s in [temp1, temp2, temp3, temp4]]))
    return res


# 回溯法
def restoreIpAddresses_2(self, s: str) -> List[str]:
    l = len(s)
    res = []

    def traceback(i, temp, flag):
        if i == l and flag == 0:
            res.append(temp[:-1])
            return
        if flag < 0:
            return
        for j in range(i, i + 3):
            if j < l:
                if j == i and s[j] == "0":
                    traceback(j + 1, temp + s[j] + ".", flag - 1)
                    break
                if 0 < int(s[i: j + 1]) <= 255:
                    traceback(j + 1, temp + s[i: j + 1] + ".", flag - 1)

    traceback(0, "", 4)
    return res