#!usr/bin/env python
# Projet Euler Problem 6
def diff(limit):
    sum_of_sq = 0
    sq_of_sum = 0
    diff = 0
    for i in range(1,limit+1):
        sum_of_sq += (i**2)
        sq_of_sum += i
    sq_of_sum **= 2
    diff = sq_of_sum - sum_of_sq
    return diff
print diff(100)
