import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]


def findKthLargest_heap(nums, k) -> int:
    return heapq.nlargest(k, nums)[-1]


# 实现堆排序
def findKthLargest_heap_made(nums, k) -> int:
    pass


# 快排实现
def findKthLargest_qsort(nums, k) -> int:
    def partition(nums, left, right):
        num = nums[left]
        l = left + 1
        while l <= right:
            while l <= right and nums[l] <= num:
                l += 1
            while l <= right and nums[right] > num:
                right -= 1
            if l <= right and nums[l] > nums[right]:
                nums[l], nums[right] = nums[right], nums[l]
        nums[left], nums[right] = nums[right], nums[left]
        return right

    left = 0
    right = len(nums) - 1
    while True:
        index = partition(nums, left, right)
        if index == len(nums) - k:
            return nums[index]
        elif index < len(nums) - k:
            left = index + 1
        else:
            right = index - 1