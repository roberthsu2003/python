#最大公因數
def greatest_common_factor():
    print("==========最大公因數=============")
    value1, value2= eval(input("請輸入2數:(數值,數值)"))
    min_value = min(value1,value2)
    for i in range(min_value,0,-1):
        if value1 % i == 0 and value2 % i == 0:
            print(f"最大公因數是:{i}")
            break

def main():
    greatest_common_factor()

if __name__ == "__main__":
    main()