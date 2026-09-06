# take input
houres = int(input('enter houres:'))
minutes = int(input('enter minutes:'))
seconds = int(input('enter seconds:'))


# perform operation
seconds1 =  houres * 3600
seconds2 = minutes * 60
seconds3 = 60

# display result
print('seconds_total',seconds1 + seconds2 + seconds3)
