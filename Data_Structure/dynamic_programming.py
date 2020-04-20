# coding: utf-8
import time


def recMC(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    for i in [c for c in coin_value_list if c <= change]:
        num_coins = 1 + recMC(coin_value_list, change-i)
        if num_coins < change:
            min_coins = num_coins
    return min_coins


def recDC(coin_value_list, change, known_values):
    min_coins = change
    if change in coin_value_list:
        known_values[change] = 1
        return 1
    if known_values[change] > 0:
        return known_values[change]
    for i in [c for c in coin_value_list if c <= change]:
        num_coins = 1 + recDC(coin_value_list, change-i, known_values)
        if num_coins < change:
            min_coins = num_coins
            known_values[change] = min_coins
    return min_coins


def dp_make_change(coin_value_list, change, min_coins):
    for cent in range(change+1):
        coin_count = cent
        for j in [c for c in coin_value_list if c <= cent]:
            if min_coins[cent - j] + 1 < coin_count:
                coin_count = min_coins[cent - j] + 1
        min_coins[cent] = coin_count
    return min_coins[change]


def dp_make_change_modified(coin_value_list, change, min_coins, coin_used):
    for cent in range(change+1):
        coin_count = cent
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cent]:
            if min_coins[cent - j] + 1 < coin_count:
                coin_count = min_coins[cent - j] + 1
                new_coin = j
        min_coins[cent] = coin_count
        coin_used[cent] = new_coin
    return min_coins[change]


def print_coins(coin_used, change):
    coin = change
    while coin > 0:
        print(coin_used[coin])
        coin -= coin_used[coin]


if __name__ == "__main__":
    t0 = time.time()
    print(recMC([1, 5, 10, 25], 63))
    t1 = time.time()
    print(recDC([1, 5, 10, 25], 63, [0]*63))
    t2 = time.time()
    print(t2-t1, t1-t0)
