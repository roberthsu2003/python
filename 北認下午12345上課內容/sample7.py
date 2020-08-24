import re

str = "Hello Python Programming"
searchObject = re.search(r"programming$", str, re.I)
if not searchObject:
    print("文字內沒有搜尋到任何相同內容")
else:
    print("文字內搜尋到%s" % searchObject.group())
