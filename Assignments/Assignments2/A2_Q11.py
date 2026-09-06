# take input
amount = int(input('enter amount:'))


# perform operation
notes2000 = amount // 2000
amount = amount % 2000

notes500 = amount // 500
amount = amount % 500

notes200 = amount // 200
amount = amount % 200

notes100 = amount // 100
amount = amount % 100

notes50 = amount // 50
amount = amount % 50

notes20 = amount // 20
amount = amount % 20

notes10 = amount // 10
amount = amount % 10


# desplay result
print('notes2000',notes2000)
print('notes500',notes500)
print('notes200',notes200)
print('notes100',notes100)
print('notes50',notes50)
print('notes20',notes20)
print('notes10',notes10)
