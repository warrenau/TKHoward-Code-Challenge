# script for Dr. Howard's code challenge
# Austin Warren
# January 2023

import numpy as np

# function to add multiples of a or b less than n (includes n)
# sum multiples of a, sum multiples of b, subtract duplicates (multiples of a and b)
def sum_multiple_multiples(a,b,n):
    x = np.floor(n/a)
    y = np.floor(n/b)
    z = np.floor(n/(a*b))

    sum = 0.5* ((a*x*(x+1))+(b*y*(y+1))-(a*b*z*(z+1)))
    return sum


# test with 10:
sum_10 = sum_multiple_multiples(3,5,9)
print(sum_10)

# now for 1000:
sum_1000 = sum_multiple_multiples(3,5,999)
print(sum_1000)
