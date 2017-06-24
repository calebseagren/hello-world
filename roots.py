#caleb Seagren
import math

a = int(input("Enter the coefficient of a: "))
b = int(input('Enter the coefficient of b: '))
c = int(input('Enter the coefficient of c: '))

d=b**2-(4*a*c)
print d
if d<0:
	print 'Error: this has complex roots'
elif d == 0:
	x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
	print "This equation has only one solution: ", x1
else:
	x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
	x2=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
	print 'The solution to this equation is ',x1, 'or', x2
