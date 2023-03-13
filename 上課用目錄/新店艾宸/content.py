#沒有參數,沒有傳出值的function
def say_hello() -> None:
  print("Hello!")


say_hello()





#1個參數,沒有傳出值的function
def say_greeting(name) -> None:
  print(f"{name}您好")


say_greeting("robert")



#2個參數,一個傳出的值
def add(a,b) -> float:
  return a + b

value = add(5,7)
print(value)
