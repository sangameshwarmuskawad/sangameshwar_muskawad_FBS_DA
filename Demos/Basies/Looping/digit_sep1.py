num = int(input('enter number:'))

sum = 0
while(num > 0):
    d = num % 10
    print(d)
    sum += d    #sum = sum + d
    num = num // 10
print('sum',sum)
