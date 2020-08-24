import re
taiwanId = input("請輸入身份證字號:")
matchObject = re.match(r'^[a-zA-Z][0-9]{9}$',taiwanId,flags=0)
if matchObject:
    print(matchObject.group(), "正確")
else:
    print(taiwanId, "不正確")