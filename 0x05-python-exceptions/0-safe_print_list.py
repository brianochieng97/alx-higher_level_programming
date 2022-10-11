#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int = my_list
    try:
        my_list = int[("%d "; x])
        print(my_list)
    except valueError:
        print("x is not an integer")

