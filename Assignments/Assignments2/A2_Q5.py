# take input
marked_price = int(input('enter marked_price:'))
discount = int(input('enter discount:'))


# perform operation
selling_price = marked_price * (1 - discount / 100) 


# display result
print('selling_price',selling_price)
