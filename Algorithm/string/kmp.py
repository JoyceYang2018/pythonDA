def next_kmp(pattern):
    l = len(pattern)
    pi = [0 for i in range(l)]
    j = 0
    for i in range(1,l):
        while j and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


def next_kmp_imp(pattern):
    l = len(pattern)
    pi = [0 for i in range(l)]
    j = 0
    for i in range(1, l):
        while j and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            if pattern[j] == pattern[pi[j]]:
                pi[i] = pi[j]
                j+=1
            else:
                j += 1
                pi[i] = j

    return pi


def kmp(text, pattern):
    j = 0
    ret = []
    pi = next_kmp(pattern)
    n = len(text)
    m = len(pattern)
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            j+=1
            if j == m:
                ret.append(i-m+1)
                j = pi[j-1]
    return ret


def kmp_imp(text, pattern):
    j = 0
    ret = []
    pi = next_kmp_imp(pattern)
    n = len(text)
    m = len(pattern)
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            j+=1
            if j == m:
                ret.append(i-m+1)
                j = pi[j-1]
    return ret


if __name__ == '__main__':
    print(next_kmp('ababaaaba'))
    print(next_kmp_imp('ababaaaba'))
    print(kmp('xgssababbbababaaabahgsabbbgsababaaabahhh','ababaaaba'))
    print(kmp_imp('xgssababbbababaaabahgsabbbgsababaaabahhh', 'ababaaaba'))

