"""Exercise from https://code.golf/morse-decoder#python
Code Golf: The idea is to try to solve the problem in the least amount of characters

Using ▄ (U+2584 Lower Half Block) to represent a dot, decode the argument from International Morse Code to alphanumeric.

1.The length of a dot is one unit.
2.A dash is three units.
3.The space between parts of the same letter is one unit.
4.The space between letters is three units.
5.The space between words is ten units.

"""


# 719 char
import sys
l='▄'
t=l*3
s=' '
z=s+l
y=l+s
m={"A":y+t,"B":t+z+z+z, "C":t+z+s+t+z,
"D":t+z+z,"E":l,"F":l+z+s+t+z,
"G":t+s+t+z,"H":l+z+z+z,"I":l+z,
"J":y+t+s+t+s+t,"K":t+z+s+t,"L":y+t+z+z,
"M":t+s+t,"N":t+z,"O":t+s+t+s+t,
"P":y+t+s+t+z,"Q":t+s+t+z+s+t,"R":y+t+z,
"S":l+z+z,"T":t,"U":l+z+s+t,
"V":l+z+z+s+t,"W":y+t+s+t,"X":t+z+z+s+t,
"Y":t+z+s+t+s+t,"Z":t+s+t+z+z,"1":y+t+s+t+s+t+s+t,
"2":l+z+s+t+s+t+s+t,"3":l+z+z+s+t+s+t,"4":l+z+z+z+s+t,
"5":l+z+z+z+z,"6":t+z+z+z+z,"7":t+s+t+z+z+z,
"8":t+s+t+s+t+z+z,"9":t+s+t+s+t+s+t+z,"0":t+s+t+s+t+s+t+s+t
}
i={v:k for k, v in m.items()}
# Accessing arguments
for a in sys.argv[1:]:
	b=a.split(' '*10)
	w=''
	for c in b:
		d=c.split('   ')
		for e in d:
			w=w+i[e]
		w=w+' '
	print(w)



t+z=19
z+z=16
t+s=27
y+z=7
z+s=11
s+t=38




# 649 char
import sys
l='▄'
t=l*3
s=' '
z=s+l
y=l+s
x=s+t
m={"A":y+t,"B":t+z+z+z, "C":t+z+x+z,
"D":t+z+z,"E":l,"F":l+z+x+z,
"G":t+x+z,"H":l+z+z+z,"I":l+z,
"J":y+t+x+x,"K":t+z+x,"L":y+t+z+z,
"M":t+x,"N":t+z,"O":t+x+x,
"P":y+t+x+z,"Q":t+x+z+x,"R":y+t+z,
"S":l+z+z,"T":t,"U":l+z+x,
"V":l+z+z+x,"W":y+t+x,"X":t+z+z+x,
"Y":t+z+x+x,"Z":t+x+z+z,"1":y+t+x+x+x,
"2":l+z+x+x+x,"3":l+z+z+x+x,"4":l+z+z+z+x,
"5":l+z+z+z+z,"6":t+z+z+z+z,"7":t+x+z+z+z,
"8":t+x+x+z+z,"9":t+x+x+x+z,"0":t+x+x+x+x
}
i={v:k for k, v in m.items()}
# Accessing arguments
for a in sys.argv[1:]:
	b=a.split(' '*10)
	w=''
	for c in b:
		d=c.split('   ')
		for e in d:
			w=w+i[e]
		w=w+' '
	print(w)



x+x=10
z+z=16
x+z=9
t+z=10
z+x=10






# 623 char
import sys
l='▄'
t=l*3
s=' '
z=s+l
y=l+s
x=s+t
v=z*2
m={"A":y+t,"B":t+v+z, "C":t+z+x+z,
"D":t+v,"E":l,"F":l+z+x+z,
"G":t+x+z,"H":l+v+z,"I":l+z,
"J":y+t+x+x,"K":t+z+x,"L":y+t+v,
"M":t+x,"N":t+z,"O":t+x+x,
"P":y+t+x+z,"Q":t+x+z+x,"R":y+t+z,
"S":l+v,"T":t,"U":l+z+x,
"V":l+v+x,"W":y+t+x,"X":t+v+x,
"Y":t+z+x+x,"Z":t+x+v,"1":y+t+x+x+x,
"2":l+z+x+x+x,"3":l+v+x+x,"4":l+z*3+x,
"5":l+z*4,"6":t+z*4,"7":t+x+z*3,
"8":t+x+x+v,"9":t+x+x+x+z,"0":t+x+x+x+x
}
i={v:k for k, v in m.items()}
# Accessing arguments
for a in sys.argv[1:]:
	b=a.split(' '*10)
	w=''
	for c in b:
		d=c.split('   ')
		for e in d:
			w=w+i[e]
		w=w+' '
	print(w)





"\u2584"

print('a')