def findLengthOfLCIS(self, nums: List[int]) -> int:
    i = 0
    j = 1
    max_len = 0
    if not nums:
        return max_len
    while j < len(nums):
        if nums[j] > nums[j - 1]:
            j += 1
        else:
            max_len = max(max_len, j - i)
            i = j
            j += 1
    max_len = max(max_len, j - i)
    return max_len
