""" Exercise from https://code.golf/evil-numbers#python
The idea is to try to solve the problem in the least amount of characters
    An evil number is a non-negative number that has an even number of 1s in its binary expansion.

Print all the evil numbers from 0 to 50 inclusive, each on their own line.
"""

# 85 chars:
for n in range(50):
	e=True
	for i in bin(n):
		if i=='1':
			e=not e
	if e:print(n)

# 62 char
for n in range(50):
	e=bin(n).count('1')%2
	if not e:print(n)

# 57 char
for n in range(50):
	e=n.bit_count()%2
	if not e:print(n)


# 52 char
[print(i) for i in range(50) if not i.bit_count()%2]