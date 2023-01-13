''' Exercise from https://code.golf/fibonacci#python The idea is to try to solve the problem in the least amount of characters
The Fibonacci numbers are a numerical sequence in which each number is the sum of the two preceding numbers: 0, 1, 1, 2, 3, 5, 8, 13…

Print the first 31 Fibonacci numbers from F0 = 0 to F30 = 832040 (inclusive), each on a separate line.

'''
# Solution with 158 char
a = [0,1]
def f(n):
    if n < len(a):
        return a[n]
    else:       
        a.append(f(n - 1) + f(n - 2))
        return a[n]
f(30)
print(*a,sep='\n')

# Solution with 102 char
def f(a,b):
	return a+b
a = [0,1]
for i in range(2,31):
	a.append(f(a[i-1],a[i-2]))
print(*a,sep='\n')

# Solution with 85 Char
a = [0,1]
def f(c):
	a.append(a[-1]+a[-2])
_=[*map(f,range(2,31))]
print(*a,sep='\n')

# Solution with 55 char
def f(i,j):
	print(i)
	if i < 832040:
		f(j,i+j)
f(0,1)

# Solution with 52 char
def f(i,j):
	print(i)
	if i < 832040:f(j,i+j)
f(0,1)

# Solution with 48 characters
a,b,n=0,1,31
while n:
	print(a)
	a,b,n=b,a+b,n-1

