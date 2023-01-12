''' Exercise from https://code.golf/fizz-buzz#python The idea is to try to solve the problem in the least amount of characters

# FIZZBUZZ
Print the numbers from 1 to 100 inclusive, each on their own line.

If, however, the number is a multiple of three then print Fizz instead, and if the number is a multiple of five then print Buzz.

If multiple conditions hold true then all replacements should be printed, for example 15 should print FizzBuzz.
'''
# Solution with 117 characters
for i in range(1,101):
	s=''
	if i%3==0:
		s=s+'Fizz'
	if i%5==0:
		s=s+'Buzz'
	if i%3!=0 and i%5!=0:
		s=i
	print(s)


# Solution with 109 characters
for i in range(1,101):
	s=''
	if i%3==0:
		s+='Fizz'
	if i%5==0:
		s+='Buzz'
	if i%3 and i%5:
		s=i
	print(s)

# Solution with 83 characters
print(*map(lambda i:'Fizz'*(not i%3)+'Buzz'*(not i%5) or i,range(1,101)),sep='\n')


