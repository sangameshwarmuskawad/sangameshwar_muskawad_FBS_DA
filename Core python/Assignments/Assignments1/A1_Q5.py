# take input
p = int(input('p:'))
r = int(input('r:'))
t = int(input('t:'))


# perform operation
CI = p *((1-r/100)**t)


# display result
print('CI:',CI)
