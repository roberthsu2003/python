#主程式
#import report as rp
from tools.report import get_description
from tools.report import a
from tools.report import b
from tools.report import c

if __name__ == "__main__":
    description = get_description()
    print("今天的天氣是"+description)
    print("module report內的a是",a)
    print("module report內的b是", b)
    print("module report內的c是", c)