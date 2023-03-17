"""Exercise from https://code.golf/roman-to-arabic#python

Code Golf: The idea is to try to solve the problem in the least amount of characters

For each numeric argument in Roman numerals, print the same number in Arabic numerals.

The numbers range from 1 to 3999 inclusive.

Arabic	1	5	10	50	100	500	1000
Roman	Ⅰ	Ⅴ	Ⅹ	Ⅼ	Ⅽ	Ⅾ	Ⅿ
"""

# Arg 202
import sys
d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
for arg in sys.argv[1:]:
	p=arg[0]
	s=d[p]
	for i in arg[1:]:
		j=d[i]
		q=d[p]
		if j>q:
			s=s-2*q+j
		else:
			s=s+j	
		p=i
	print(s)
	

# 186 char
import sys
d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
for a in sys.argv[1:]:
	p=a[0]
	s=d[p]
	for i in a[1:]:
		j,q=d[i],d[p]
		if j>q:s=s-2*q+j
		else:s=s+j	
		p=i
	print(s)








