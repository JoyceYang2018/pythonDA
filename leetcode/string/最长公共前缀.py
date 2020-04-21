def longestCommonPrefix(self, strs: List[str]) -> str:
    max_prefix = ""
    for i in range(len(min(strs, key=lambda x: len(x))) if strs else 0):
        if len(set([s[i] for s in strs])) > 1:
            break
        else:
            max_prefix += strs[0][i]
    return max_prefix