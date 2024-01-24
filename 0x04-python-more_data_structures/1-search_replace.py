#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mn_list = my_list.copy()
    for i in range(len(my_list)):
        if mn_list[i] is search:
            mn_list.pop(i)
            mn_list.insert(i, replace)
            return mn_list
