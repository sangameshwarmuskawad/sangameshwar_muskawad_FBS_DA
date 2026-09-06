# take input
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))


# perform operation
x = (b**2) - (4*a*c)
root1 = (- b - ((x)**0.5)) / (2 * a)
root2 = (- b + ((x)**0.5)) / (2 * a)

# display result
print('root',root1)
print('root2',root2)
