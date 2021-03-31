#主程式
import report
if __name__ == "__main__":
    description = report.get_description()
    print("今天的天氣是"+description)
    print("module report內的a是",report.a)
    print("module report內的b是", report.b)
    print("module report內的c是", report.c)