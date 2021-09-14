
# import test
import unittest
import numpy as np


def find_it(seq):
    seq_values, seq_counts = np.unique(seq, return_counts = True)
    for num,coun in zip(seq_values,seq_counts):
        if (coun % 2) != 0:
            odd = num
            break
    return odd

# This solution was approximately O(n^2) as it transverses two lists.

# A suggested solution that will be O(n) is using the XOR operation
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1
# x ^ x == 0 for any pair of occurrences of x
# x ^ x ^ x == x for any odd occurrences of x
# As the xor operation is both comutative and associative, so the order of the numbers/operations doesn't matter.

# Thus, every number that appear in pairs are set to zero and the single number with odd occurrences remains with its bits set.
def find_it2(seq):
    odd = 0
    for num in seq:
        odd ^= num
    return odd


class TestKataMethods(unittest.TestCase):
    def test_find_even_index(self,arr,solution,message = None):
        self.assertEqual(find_it(arr), solution, message)

seq = [2,2,2,3,2,2,2]
find_it2(seq)

test_kata = TestKataMethods()
test_kata.test_find_even_index(np.array([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]),5)
test_kata.test_find_even_index(np.array([1,1,2,-2,5,2,4,4,-1,-2,5]),-1)
test_kata.test_find_even_index(np.array([20,1,1,2,2,3,3,5,5,4,20,4,5]),5)
test_kata.test_find_even_index(np.array([1,1,1,1,1,1,10,1,1,1,1]),10)
test_kata.test_find_even_index(np.array([10, 10, 10]),10)

print('END')