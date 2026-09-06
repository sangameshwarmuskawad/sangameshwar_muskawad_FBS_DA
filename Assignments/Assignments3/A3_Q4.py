# take input
a = int(input('enter side:'))
b = int(input('enter side:'))
c = int(input('enter side:'))

# check condition
if((a + b > c) and (a + c > b) and (b + c > a)):
    print('triangle is valid.')
else:
    print('triangle is not valid.')
        