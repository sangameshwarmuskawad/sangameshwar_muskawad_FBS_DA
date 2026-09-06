# take input
day = int(input('day:'))


# perform operation
year = day // 365
day = day % 365

week = day // 7
day = day % 7


# display result
print('year',year)
print('week',week)
print('day',day)
