def prime():
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                return False
        return True
    else:
        return False

num = int(input("Enter a number: "))
res = prime()
print(res)
