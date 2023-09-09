#!/usr/bin/env python3
def no_c(my_string):
    ##return (my_string.replace("cC", " "))
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] not in "cC":
            new_string += my_string[i]
    return new_string
