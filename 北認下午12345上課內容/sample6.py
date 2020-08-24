import re

strText = "Hello Python Programming"
matchObjec = re.match(r"Hello", strText, flags=0)
if matchObjec is None:
    print("文字最前面沒有搜尋到")
else:
    print("文字最前面搜尋到%s" % matchObjec.group())