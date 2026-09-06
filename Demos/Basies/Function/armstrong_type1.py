def armstrong():
    num = int(input("Enter a number: "))
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
        print(num, "true")
    else:
        print(num, "false")
armstrong()
