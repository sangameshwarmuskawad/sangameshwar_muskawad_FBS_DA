# take input
feet = int(input('enter feet:'))
inches = int(input('enter inches:'))


# perform operation 
meters = (feet * 0.3048) + (inches * 0.0254)
centimeters = (feet * 30.48) + (inches * 2.54)


# display result 
print('meters',meters)
print('centimeters',centimeters)
