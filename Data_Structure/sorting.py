# coding: utf-8
import time


def bubble_sort(alist):
    for pass_num in range(len(alist)-1, 0, -1):
        for i in range(pass_num):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def short_bubble_sort(alist):
    exchange = True
    pass_num = len(alist) - 1
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchange = True
        pass_num -= 1


def selection_sort(alist):
    for fill_sort in range(len(alist)-1, 0, -1):
        max_pos = 0
        for loc in range(1, fill_sort+1):
            if alist[loc] > alist[max_pos]:
                max_pos = loc
        alist[fill_sort], alist[max_pos] = alist[max_pos], alist[fill_sort]


def insertion_sort(alist):
    for index in range(1, len(alist)):
        cur_value = alist[index]
        pos = index

        while pos > 0 and alist[pos-1] > cur_value:
            alist[pos] = alist[pos-1]
            pos -= 1
        alist[pos] = cur_value


def shell_sort(alist):
    sub_count = len(alist) // 2
    while sub_count > 0:
        for start_pos in range(sub_count):
            get_insertion_sort(alist, start_pos, sub_count)
        print("After increments of size", sub_count, "The list is", alist)
        sub_count = sub_count // 2


def get_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        cur_value = alist[i]
        pos = i

        while pos >= gap and alist[pos-gap] > cur_value:
            alist[pos] = alist[pos-gap]
            pos -= gap
        alist[pos] = cur_value


# TODO 应该有更好的描述 然后迭代方法应该也可以归并
def merge_sort(alist):
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        if i < len(left_half):
            alist[k:] = left_half[i:]

        if j < len(right_half):
            alist[k:] = right_half[j:]
    print("Merging ", alist)


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition_mid(alist, first, last)
        quick_sort_helper(alist, first, split_point-1)
        quick_sort_helper(alist, split_point+1, last)


# TODO 感觉有更好的实现方法
def partition(alist, first, last):
    part_value = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while right_mark >= left_mark and alist[left_mark] <= part_value:
            left_mark += 1
        while right_mark >= left_mark and alist[right_mark] >= part_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    return right_mark


def partition_mid(alist, first, last):
    def mid(alist, first, last):
        a, b, c = alist[first], alist[(first + last) // 2], alist[last]
        if a < b and a < c:
            return (b,(first + last) // 2) if b < c else (c,last)
        if b < c:
            return (a,first) if a < c else (c,last)
        if b > c:
            return (a,first) if a < b else (b,(first + last) // 2)
    part_value, mid_pos = mid(alist, first, last)
    alist[first], alist[mid_pos] = alist[mid_pos], alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while right_mark >= left_mark and alist[left_mark] <= part_value:
            left_mark += 1
        while right_mark >= left_mark and alist[right_mark] >= part_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    return right_mark


# TODO 需要补充堆排序
def heap_sort(alist):
    pass


if __name__ == "__main__":
    # a = [0, 4, 3, 2, 44, 56, 33, 4, 2, 66, 4, 7, 8, 9]
    # t0 = time.time()
    # bubble_sort(a)
    # print(a)
    # t1 = time.time()
    # a = [0, 4, 3, 2, 44, 56, 33, 4, 2, 66, 4, 7, 8, 9]
    # short_bubble_sort(a)
    # print(a)
    # t2 = time.time()
    # print((t1-t0, t2-t1))
    # alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # shell_sort(alist)
    b = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(b)
    print(b)