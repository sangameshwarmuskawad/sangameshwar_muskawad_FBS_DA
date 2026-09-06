import random
Userid = 'admin'
Password = '12345'

# take input
userid = input('enter user id:')
password = input('enter password:')

# check condition
if(userid == Userid and password == Password):
    captcha = random.randint(1000, 9999)
    print('captcha:',captcha)
    user_input = int(input('enter captcha:'))

    if(user_input == captcha):
        print('login successfil')
    else:
        print('incorrect captcha.')    

else:
    print('invalid userid or password.')
    