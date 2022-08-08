express = input("請輸入運算式")
answer = eval(input(f"{express}="))
print(f"您的答案是{answer}")
print(f"正確答案是:{eval(express)}")
