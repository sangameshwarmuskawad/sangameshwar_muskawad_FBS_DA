def palindrome(num):
    temp = num
    rev_num = 0

    while (temp > 0):
        d = temp % 10
        temp = temp // 10
        rev_num = rev_num * 10 + d

    if (rev_num == num):
        return True
    else:
        return False

num = int(input("Enter a number: "))
res = palindrome(num)
print(res)
