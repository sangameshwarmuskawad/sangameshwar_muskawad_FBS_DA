# take input
mark1 = int(input('enter mark 1:'))
mark2 = int(input('enter mark 2:'))
mark3 = int(input('enter mark 3:'))
mark4 = int(input('enter mark 4:'))
mark5 = int(input('enter mark 5:'))


# perform operation
totalmark = mark1+mark2+mark3+mark4+mark5

percentage = totalmark/500*100


# display result
print('mark:'+str(totalmark))
print('percentage:'+str(percentage))
