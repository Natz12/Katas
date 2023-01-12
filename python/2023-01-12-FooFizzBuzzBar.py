''' Exercise from https://code.golf/foo-fizz-buzz-bar#python The idea is to try to solve the problem in the least amount of characters

FooFizzBuzzBar

Print the numbers from 1 to 1,000 inclusive, each on their own line.

If, however, the number is a multiple of two then print Foo instead, if the number is a multiple of three then print Fizz, if the number is a multiple of five then print Buzz, and if the number is a multiple of seven then print Bar.

If multiple conditions hold true then all replacements should be printed, for example 15 should print FizzBuzz.


'''

# Solution with 120 Char
print(*map(lambda i: 'Foo'*(not(i%2))+'Fizz'*(not(i%3))+'Buzz'*(not(i%5))+'Bar'*(not(i%7)) or i,range(1,1001)),sep='\n')