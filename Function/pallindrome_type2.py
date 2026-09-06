def palindrome(num):
    temp = num
    rev_num = 0

    while (temp > 0):
        d = temp % 10
        temp = temp // 10
        rev_num = rev_num * 10 + d

    if(rev_num == num):
        print(num, "true")
    else:
        print(num, "false")

num = int(input("Enter a number: "))
palindrome(num)
