#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum_mul = sum(num1 * num2 for num1, num2 in my_list)
        total = sum(tup[1] for tup in my_list)
        return sum_mul/total
    return 0
