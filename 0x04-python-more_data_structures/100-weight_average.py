#!/usr/bin/pyhton3
def weight_avergae(my_list=[]):
    if not my_list:
        return 0

    prod = []
    denom = 0

    for i, j in my_list:
        prod.append(i * j)
        denom += j

        avg = sum(ptod) / denom
        return avg
