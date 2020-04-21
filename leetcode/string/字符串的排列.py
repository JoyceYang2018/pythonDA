import collections


def checkInclusion(self, s1: str, s2: str) -> bool:
    l1 = len(s1)
    l2 = len(s2)
    c1 = collections.Counter(s1)
    c2 = collections.Counter()
    cnt = 0
    p, q = 0, 0
    while q < l2:
        c2[s2[q]] += 1
        if c2[s2[q]] == c1[s2[q]]:
            cnt += 1
        if cnt == len(c1):
            return True
        q += 1
        if q - p + 1 > l1:
            if c2[s2[p]] == c1[s2[p]]:
                cnt -= 1
            c2[s2[p]] -= 1
            if c2[s2[p]] == 0:
                del c2[s2[p]]
            p += 1
    return False