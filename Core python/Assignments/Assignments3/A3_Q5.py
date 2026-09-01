# take input
a = int(input('enter side:'))
b = int(input('enter side:'))
c = int(input('enter side:'))

# check condition
if((a + b > c) and (a + c > b) and (b + c > a)):
    if(a == b == c):
        print('triangle is equilateral.')
    elif(a == b or a == c or b == c):
        print('triangle is isosceles.')
    else:
        print('triangle is scalene.')
               