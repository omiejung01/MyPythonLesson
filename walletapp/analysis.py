import random
from time import time

def find_max1():
    num = 2000000
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0, 10))
        i += 1

    #print(my_list)

    # FIND_MAX1
    max1 = 0
    for x in my_list:
        if x > max1:
            max1 = x

    print('Max is ', max1)

def find_max2():
    num = 2000000
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0, 10))
        i += 1

    #print(my_list)
    max2 = 0
    score_list = [10,9,8,7,6,5,4,3,2,1,0]
    for s in score_list:
        if my_list.count(s) > 0: # s is in the my_list or not
            max2 = s
            break
    print("(2)Max is ", max2)


def run():
    print(fact(8))
"""
    start_time = time()  # record the starting time
    find_max1()
    end_time = time()  # record the ending time
    elapsed_time = end_time - start_time
    print(elapsed_time)

    start_time2 = time()  # record the starting time
    find_max2()
    end_time2 = time()  # record the ending time
    elapsed_time2 = end_time2 - start_time2
    print(elapsed_time2)
"""

def sum1(num):
    # return 1 + 2 + 3 + ... + n
    num_set = range(1, num+1)
    total = 0
    for x in num_set:
        total += x

    return total


def sum2(num):
    # return 1 + 2 + 3 + ... + n
    if num == 0:
        return 0
    elif num ==1:
        return 1
    else:
        return num+sum2(num-1)


def fact(num):
    # return factorial(n)
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * fact(num - 1)



