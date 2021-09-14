'''Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Examples:

iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd'''

import unittest
import numpy as np

# Tried to limit the number of operations by doing if counts[0]
def iq_test(numbers):
    numbers = [int(item) for item in numbers.split(' ')]
    counts = [0,0] # [even, odd]
    ind = [0,0] # [even, odd]

    for i, num in enumerate(numbers):
        if (num%2) == 0:
            if counts[0]:
                counts[0] = counts[0] + 1
                ind[0] = i
        else:
            if counts[1]:
                counts[1] = counts[1] + 1
                ind[1] = i 
    index = ind[np.argmin(counts)]+1
    return index

# After refactoring

def iq_test2(numbers):
    counts = [0,0] # [even, odd]
    ind = [0,0] # [even, odd]

    for i, num in enumerate([int(item) for item in numbers.split(' ')]):
        odd = num%2
        if counts[odd] <= 1:
            counts[odd] = counts[odd] + 1
            ind[odd] = i
    index = ind[np.argmin(counts)]+1
    return index

'''A suggested solution with an early stop'''
def iq_test3(numbers):
    poss = [0, 0]
    for i, num in enumerate(numbers.split()):
        c = int(num) % 2
        if poss[c]:
            if poss[1 - c]:
                return poss[1 - c]
        else:
            poss[c] = i + 1
    return i + 1

# iq_test3("2 4 7 8 10")

class TestKataMethods(unittest.TestCase):
    def test_find_even_index(self,arr,solution,message = None):
        self.assertEqual(iq_test(arr), solution, message)



test_kata = TestKataMethods()
test_kata.test_find_even_index("2 4 7 8 10",3)
test_kata.test_find_even_index("1 2 2",1)

print('Done')
