def lengthOfLongestSubstring(self, s: str) -> int:
    max_str = ""
    result = ""
    l = len(s)
    j = 0
    while j < l:
        if s[j] not in max_str:
            max_str += s[j]
        else:
            if len(max_str) >= len(result):
                result = max_str
            max_str = max_str[max_str.index(s[j]) + 1:] + s[j]
        j += 1
    if len(max_str) >= len(result):
        result = max_str
    return len(result)