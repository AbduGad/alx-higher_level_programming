#!/usr/bin/python3
""" my list"""


class MyList(list):
    """extended version of list
    """
    def print_sorted(self):
        """prints the list in ascending order
        """
        copy = self[:]
        copy.sort()
        print(copy)
