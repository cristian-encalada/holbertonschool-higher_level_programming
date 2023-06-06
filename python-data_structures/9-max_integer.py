#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range(len(my_list)):
        if i == 0 or my_list[i] > max_num:
            max_num = my_list[i]
    return max_num if my_list else None
