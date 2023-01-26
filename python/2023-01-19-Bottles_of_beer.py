''' Exercise from https://code.golf/99-bottles-of-beer#python
The idea is to try to solve the problem in the least amount of characters

Print the lyrics to the song 99 Bottles of Beer:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.

…

1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
'''

# Solution with 628 char:
for i in range(0,99):
	j=99-i
	if i<97:
		print(f'{j} bottles of beer on the wall, {99-i} bottles of beer.\nTake one down and pass it around, {j-1} bottles of beer on the wall.\n')
	elif i==97:
		print(f'{j} bottles of beer on the wall, {99-i} bottles of beer.\nTake one down and pass it around, {j-1} bottle of beer on the wall.\n')
	elif i==98:
		print(f'{j} bottle of beer on the wall, {99-i} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n')
		print('No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')


# Solution with 408 char 
for i in range(0,99):
	j=99-i
	s='s' if i<98 else ''
	c='' if i==97 else 's'
	n=j-1 if i<98 else 'no more'
	b=f'{j} bottle{s} of beer on the wall, {j} bottle{s} of beer.\nTake one down and pass it around, {n} bottle{c} of beer on the wall.\n'
	print(b) if i<98 else print(b,'\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.')

# Solution 376 char
for i in range(0,99):
	j=99-i
	s='s' if i<98 else ''
	c='' if i==97 else 's'
	n=j-1 if i<98 else 'no more'
	w=' of beer on the wall'
	b=f'{j} bottle{s}{w}, {j} bottle{s} of beer.\nTake one down and pass it around, {n} bottle{c}{w}.\n'
	print(b) if i<98 else print(b,f'\nNo more bottles{w}, no more bottles of beer.\nGo to the store and buy some more, 99 bottles{w}.')

# Solution with 356 char
i=99
while i >0:
	s='s' if i>1 else ''
	c='' if i==2 else 's'
	n=i-1 if i>1 else 'no more'
	w=' of beer on the wall'
	b=f'{i} bottle{s}{w}, {i} bottle{s} of beer.\nTake one down and pass it around, {n} bottle{c}{w}.\n'
	i-=1
	print(b) if i>0 else print(b,f'\nNo more bottles{w}, no more bottles of beer.\nGo to the store and buy some more, 99 bottles{w}.')

# Solution with 345 char
i=99
while i >0:
	s='s' if i>1 else ''
	c='' if i==2 else 's'
	n=i-1 if i>1 else 'no more'
	e=' of beer'
	t=' bottle'
	w=f'{e} on the wall'
	b=f'{i}{t+s+w}, {i}{t+s+e}.\nTake one down and pass it around, {n}{t+c+w}.\n'
	i-=1
	print(b) if i>0 else print(b,f'\nNo more{t+"s"+w}, no more{t+"s"+e}.\nGo to the store and buy some more, 99{t+"s"+w}.')


i=99
while i >0:
	s='s' if i>1 else ''
	c='' if i==2 else 's'
	e=' of beer'
	t=' bottle'
	w=f'{e} on the wall'
	m=' more'
	n=i-1 if i>1 else f'no{m}'
	b=f'{i}{t+s+w}, {i}{t+s+e}.\nTake one down and pass it around, {n}{t+c+w}.\n'
	i-=1
	p=b if i>0 else b+f'\nNo{m+t+"s"+w}, no{m+t+"s"+e}.\nGo to the store and buy some{m}, 99{t+"s"+w}.'
	print(p)
