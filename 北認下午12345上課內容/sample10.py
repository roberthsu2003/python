import re
taiwanId = input("請輸入身份證字號:")
matchObject = re.match(r'^[A-Z]\d{9}$',taiwanId,re.I)
if matchObject:
    print(matchObject.group(), "正確")
else:
    print(taiwanId, "不正確")