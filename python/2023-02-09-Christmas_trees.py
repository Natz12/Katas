"""Exercise from https://code.golf/christmas-trees#python
Code Golf: The idea is to try to solve the problem in the least amount of characters

Draw a size ascending range of Christmas trees using asterisks, ranging from size 3 to size 9, each tree separated by a blank line.

A size 3 tree should look like this, with a single centered asterisk for the trunk:

   *
  ***
 *****
   *
With the largest size 9 tree looking like this:

         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
         *


"""



# 118 chars
for i in range(6,20,2):
	for j in range(1,i,2):
		h=(i-j)//2
		s=' '*h
		print(s,'*'*(j))
	print(' '*((i-1)//2),'*\n')



# 98 char
r=range
p=print
for i in r(3,10):
	for j in r(1,i+1):
		p(' '*(i-j+1)+'*'*(2*j-1))
	p(' '*i+'*\n')






# 95 char
p,i=print,3
while i<10:
	h,j=i,1
	while h:
		p(' '*h+'*'*j)
		j+=2
		h-=1
	p(' '*i+'*\n')
	i+=1
	
		
# 94 char
r=range
p=print
for i in r(2,9):
	for j in r(1,i+2):p(' '*(i-j+1),'*'*(2*j-1))
	p(' '*i,'*\n')
		


# 110 char (created after the 94 char solution)
r=range
p=print
for i in r(3,10):
	p('\n'.join([(' '*(i-j+1)+'*'*(2*j-1)) for j in r(1,i+1)]))
	p(' '*i+'*\n')

# 106 char (created after the 94 char solution)
r=range
p=print
for i in r(3,10):p('\n'.join([(' '*(i-j+1)+'*'*(2*j-1)) for j in r(1,i+1)]+[' '*i+'*\n']))
