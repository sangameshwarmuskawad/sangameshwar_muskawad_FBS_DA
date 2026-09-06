# take input
number = int(input('enter number:'))


# perform operation
a = (number // 100)
b = ((number // 10) % 10 )
c = (number % 10)
reversed_number = (number % 10) * 100 + ((number // 10)) % 10 * 10 + (number // 100)


# display result
print('reversed_number',reversed_number)
