# take input
cost_price = int(input('enter cost price:'))
selling_price = int(input('enter selling price:'))

# check condition
if(selling_price > cost_price):
    profit = selling_price - cost_price
    print('profit =',profit)
elif(cost_price > selling_price):
    loss = cost_price - selling_price
    print('loss =',loss)
else:
    print('no profit , no loss')
        