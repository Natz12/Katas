""" Exercise from https://code.golf/happy-numbers#python
Code Golf: The idea is to try to solve the problem in the least amount of characters

A happy number is defined by the following Sequence: Starting with any positive integer, replace the number by the sum of the squares of its digits in base-ten, and repeat the process until the number either equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are sad numbers.

For example, 19 is happy, as the associated Sequence is:

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1.
Print all the happy numbers from 1 to 200 inclusive, each on their own line.

"""
# char 207
def h(n):
	w=0
	c=n//100
	t=n//10
	d=(n-c*100-(n-t*10))//10
	o=n-t*10
	w=c**2+d**2+o**2
	if w==1:
		return True
	elif(w==4):
		return False
	else:
		a=h(w)
		return a
[print(i) for i in range(1,200) if h(i)]


# 169 char
def h(n):
	w = n
	while (w!=1)and(w!=4):
		w=sum([int(i)**2 for i in str(w)])
	if w==1:
		return True
	elif w==4:
		return False
[print(i) for i in range(1,200) if h(i)]

# 164 char
def h(n):
	w=sum([int(i)**2 for i in str(n)])
	if w==1:
		return True
	elif w==4:
		return False
	else:
		a=h(w)
		return a
[print(i) for i in range(1,200) if h(i)]




# def h(n):
# 	w=[int(i)**2 for i in str(n)][0]
# 	if w==1:
# 		return True
# 	elif w==4:
# 		return False
# 	else:
# 		a=h(w)
# 		return a





# def h(n):
# 	w=[n**2 for i in str(n)][0]
# 	if w==1:
# 		return True
# 	elif(w==4):
# 		return False
# 	else:
# 		a=h(w)
# 		return a
# # [print(i) for i in range(1,200) if h(i)]
# # for i in range(1,200): h(i)
# # i=7
# # if h(i):
# # 	print(i)
# n=7
# w=[n**2 for i in str(n)][0]


# def h(n):
# 	w=0
# 	for i in str(n):
# 		w+=int(i)**2
# for i in range(200):
    



# def h(n):
# 	w=0
# 	w=sum([w+int(n)**2 for i in str(n)])
# 	print(w)
# 	if w==1:
# 		return True
# 	elif (w==4)or(w==3):
# 		return False
# 	else:
# 		return h(w)
# # [print(i) for i in range(200) if h(i)]
# for i in range(200): print(h(i))