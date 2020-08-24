import re
emails = input('請輸入多筆email:')
allList = re.findall(r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',emails)
print("取出的email有")
for email in allList:
    print(email)