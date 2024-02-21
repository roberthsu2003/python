import pyinputplus as pyip
from tools import getStudents,save_to_csv


if __name__ == "__main__":
    s_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
    students:list[dict] = getStudents(s_nums)
    fileName:str = pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名稱):")
    save_to_csv(students,fileName)
    