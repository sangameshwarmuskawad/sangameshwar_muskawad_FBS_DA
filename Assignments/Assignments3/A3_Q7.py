Userid = 'admin'
Password = '12345'

# take input
userid = input('enter user id:')
password = input('enter password:')

# check condition
if(userid == Userid and password == Password):
    print('login successful.')
else:
    print('invalid user id or password.')
