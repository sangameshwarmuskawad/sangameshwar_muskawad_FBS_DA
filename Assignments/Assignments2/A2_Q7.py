# take input
number = int(input('enter number:'))


# perform operation
a = (number // 100)
b = (number //10 % 10)
c = (number % 10)
sum_three_digit = a + b + c


# display result
print('sum_three_digit',sum_three_digit)
