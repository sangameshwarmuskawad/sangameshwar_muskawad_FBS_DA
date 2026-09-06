def perfect(num):
    temp = num
    sum = 0

    for i in range(1, num):
        if (num % i == 0):
            sum = sum + i

    if (sum == num):
        return True
    else:
        return False

num = int(input("Enter a number: "))
res = perfect(num)
print(res)
