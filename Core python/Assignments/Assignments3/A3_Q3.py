# take input
angle1 = int(input('enter first angle:'))
angle2 = int(input('enter second angle:'))
angle3 = int(input('entet third angle:'))

# check condition
if(angle1 > 0 and angle2 > 0 and angle3 > 0):
    if(angle1 + angle2 + angle3 == 180):
        print('triangle is valid.')
else:
    print('triangle is not valid.')
