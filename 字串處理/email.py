#!usr/bin/python3

'''
#email.py
# r'^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]+$'
請輸入多筆email:bogusemail123@sillymail.com, robert@gmail.com ,,,roberthsu2003@gmail.com
取出的email有:
bogusemail123@sillymail.com
robert@gmail.com
roberthsu2003@gmail.com
'''

import re
emails = input('請輸入多筆email:')
print(emails)
getEmails = re.findall(r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',emails)
print('取出的email有:')
for email in getEmails:
    print(email)

