# coding: utf-8


def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        found = False
        index = (first + last) // 2
        if alist[index] == item:
            found = index
            break
        elif alist[index] < item:
            first = index + 1
        else:
            last = index - 1
    return found


def binary_search_recursion(alist, item):
    if len(alist) == 0:
        return False
    index = (len(alist) - 1) // 2
    if alist[index] == item:
        return True
    elif alist[index] < item:
        return binary_search_recursion(alist[index+1:], item)
    else:
        return binary_search_recursion(alist[:index], item)


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hashfunc(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                self.slots[next_slot] = key
                self.data[next_slot] = data

    def hashfunc(self, key, size):
        return key % size

    def rehash(self, key, size):
        return (key + 1) % size

    def get(self, key):
        startslot = self.hashfunc(key, len(self.slots))
        position = startslot
        data = None
        while self.slots[position] is not None:
            if self.slots[position] == key:
                data = self.data[position]
                break
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    break
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == "__main__":
    # print(binary_search([0, 2, 5, 6, 8, 11, 24, 55, 78, 120, 155], 9))
    # print(binary_search_recursion([0, 2, 5, 6, 8, 11, 24, 55, 78, 120, 155], 9))

    h = HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[20] = 'chicken'
    h[17] = 'tiger'
    print(h.slots)
    print(h.data)
    print(h[20])
    print(h[17])
    h[20] = 'duck'
    print(h[20])
    print(h.data)
    print(h[99])

