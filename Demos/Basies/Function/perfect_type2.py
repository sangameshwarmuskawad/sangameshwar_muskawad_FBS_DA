def perfect(num):
    temp = num
    sum = 0

    for i in range(1, num):
        if (num % i == 0):
            sum = sum + i

    if (sum == num):
        print(num, "true")
    else:
        print(num, "false")

num = int(input('enter number:'))
perfect(num)
