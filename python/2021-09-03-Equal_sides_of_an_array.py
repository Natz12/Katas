# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

# For example:

# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

# import test
import unittest
import numpy as np
# unittest.TestCase
def find_even_index(arr):
    #your code here
    even_index = None
    for i in range(arr.shape[0]):
        if sum(arr[:i]) == sum(arr[i+1:]):
            even_index = i
            break
    if even_index == None:
        even_index = -1
    return even_index
# This solution was O(n^2) as it sums the list over and over again.
# A suggested solution that will be O(n) is 

def find_even_index_best(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1

# Another O(n) solution

import numpy as np
def find_even_index_best2(arr):
    cs = np.cumsum(arr)
    for i in range(len(arr)):
        if cs[i] == cs[-1] - (cs[i-1] if i>0 else 0):
            return i
    return -1


class TestKataMethods(unittest.TestCase):
    def test_find_even_index(self,arr,solution,message = None):
        self.assertEqual(find_even_index(arr), solution, message)


test_kata = TestKataMethods()
test_kata.test_find_even_index(np.array([1,100,50,-51,1,1]),1)

test_kata.test_find_even_index(np.array([1,2,3,4,3,2,1]),3)
test_kata.test_find_even_index(np.array([1,100,50,-51,1,1]),1,)
test_kata.test_find_even_index(np.array([1,2,3,4,5,6]),-1)
test_kata.test_find_even_index(np.array([20,10,30,10,10,15,35]),3)
test_kata.test_find_even_index(np.array([20,10,-80,10,10,15,35]),0)
test_kata.test_find_even_index(np.array([10,-80,10,10,15,35,20]),6)
test_kata.test_find_even_index(np.array(list(range(1,100))),-1)
test_kata.test_find_even_index(np.array([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
test_kata.test_find_even_index(np.array([-1,-2,-3,-4,-3,-2,-1]),3)
test_kata.test_find_even_index(np.array(list(range(-100,-1))),-1)