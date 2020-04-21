def reverseWords(self, s: str) -> str:
    s_list = s.strip().split()
    return " ".join(s_list[::-1])