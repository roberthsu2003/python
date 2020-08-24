import re
str1 = "Birds   fly  high in    the   sky for ever"
splitList = re.split(r'\s+',str1)
print(splitList)
print("-".join(splitList))