'''Exercise from https://code.golf/seven-segment#python
Code Golf: The idea is to try to solve the problem in the least amount of characters

Using pipes and underscores print the argument as if it were displayed on a seven segment display.

For example the number 0123456789 should be displayed as:

 _     _  _     _  _  _  _  _
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|


'''


# 536 char
import sys
u='_'
l='|'
t='   '
s=' '
d={'0':{'a':s+u+s,'b':l+s+l,'c':l+u+l},
'1':{'a':t,'b':s+s+l,'c':s+s+l},
'2':{'a':s+u+s,'b':s+u+l,'c':l+u+s},
'3':{'a':s+u+s,'b':s+u+l,'c':s+u+l},
'4':{'a':t,'b':l+u+l,'c':s+s+l},
'5':{'a':s+u+s,'b':l+u+s,'c':s+u+l},
'6':{'a':s+u+s,'b':l+u+s,'c':l+u+l},
'7':{'a':s+u+s,'b':s+s+l,'c':s+s+l},
'8':{'a':s+u+s,'b':l+u+l,'c':l+u+l},
'9':{'a':s+u+s,'b':l+u+l,'c':s+u+l}}
a,b,c='','',''
for arg in sys.argv[1:]:
	for i in arg:
		a=a+d[i]['a']
		b=b+d[i]['b']
		c=c+d[i]['c']
print('\n'.join([a,b,c]))
    
