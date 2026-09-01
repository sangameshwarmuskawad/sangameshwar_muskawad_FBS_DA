# take input
num = int(input('enter number:'))
temp = num
rev_num = 0

# check condition
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 + d
if(rev_num == num):
    print('the number is pallindrome.')
else:
    print('the number is not pallindrome') 
           