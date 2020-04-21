def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    res = 0
    traveled_ij = []
    l = len(grid[0])
    w = len(grid)

    def is_iland(i, j):
        if i < 0 or i >= w or j < 0 or j >= l:
            return 0
        if grid[i][j] == 0:
            return 0
        if grid[i][j] == 1:
            # 这里两个处理方法， 直接修改原数组 来表示visited
            # 或者占用一个空间来储存已经遍历过的土地
            # grid[i][j] = 0
            if (i, j) in traveled_ij:
                return 0
            traveled_ij.append((i, j))

            top = is_iland(i - 1, j)
            bottom = is_iland(i + 1, j)
            left = is_iland(i, j - 1)
            right = is_iland(i, j + 1)
            return 1 + top + bottom + left + right

    for i in range(w):
        for j in range(l):
            if (i, j) in traveled_ij:
                continue
            res = max(res, is_iland(i, j))
    return res