#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mul += True
        else:
            mul += False
    return mul