def longestConsecutive(self, nums: List[int]) -> int:
    max_len = 0
    nset = set(nums)
    for num in nums:
        if num - 1 in nset:
            continue
        cur_len = 1
        while num + 1 in nset:
            num += 1
            cur_len += 1
        max_len = max(max_len, cur_len)
    return max_len
