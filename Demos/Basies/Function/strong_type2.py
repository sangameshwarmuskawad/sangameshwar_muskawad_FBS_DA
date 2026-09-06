def strong(num):             
    temp = num
    sum = 0

    while (temp > 0):
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1, d + 1):
            fact = fact * i
        sum = sum + fact

    if (sum == num):
        print(num, "true")
    else:
        print(num, "false")

num = int(input("Enter a number: "))
strong(num)
