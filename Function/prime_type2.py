def prime(num):
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                print(num, "false")
                break
        else:
            print(num, "true ")
    else:
        print(num, "false")

num = int(input("Enter a number: ")) 
prime(num)
