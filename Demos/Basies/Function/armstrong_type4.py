def armstrong(num):
    temp = num
    count = 0
    while(temp > 0):
        count = count + 1
        temp = temp // 10

    temp = num
    sum = 0
    while (temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)

    if (sum == num):
        return True
    else:
        return False

num = int(input('enter number:'))
res = armstrong(num)
print(res)
