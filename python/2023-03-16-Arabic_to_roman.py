"""Exercise from https://code.golf/arabic-to-roman#python

Code Golf: The idea is to try to solve the problem in the least amount of characters

For each numeric argument in Arabic numerals, print the same number in Roman numerals.

You may use either ASCII or UTF-8 (U+2160 to U+2188) for Roman numerals.

The numbers range from 1 to 3999 inclusive.

Arabic	1	5	10	50	100	500	1000
Roman	Ⅰ	Ⅴ	Ⅹ	Ⅼ	Ⅽ	Ⅾ	Ⅿ

"""


# 231 char
import sys
i=(1000,900,500,400,100,90,50,40,10,9,5,4,1)
n=('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
for a in sys.argv[1:]:
	a=int(a)
	s=''
	for j in range(len(i)):
		c=int(a/i[j])
		s+=n[j]*c
		a-=i[j]*c
	print(s)


# import sys
# d=[(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
# for arg in sys.argv[1:]:
# 	print(arg)
# 	s=''
# 	for i,j in d:
# 		c=arg//j
# 		arg=arg-c
# 		s=s+j*(c)
# 	print(s)

