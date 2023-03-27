def sayHello(name) -> None:
  print(f'您好{name}')
  
  
sayHello("robert")

def greeting(name) -> str:
  return f"'您好{name}'"


greet = greeting("robert")
print(greet)
