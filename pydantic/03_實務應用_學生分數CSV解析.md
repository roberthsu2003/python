```python
import csv
from pydantic import RootModel,BaseModel,Field
from pprint import pprint


class Student(BaseModel):
    姓名: str
    國文: int = Field(alias='科目1')
    英文: int = Field(alias='科目2')
    數學: int = Field(alias='科目3')
    地理: int = Field(alias='科目4')
    歷史: int = Field(alias='科目5')
    社會: int = Field(alias='科目6')
    品德: int = Field(alias='科目7')

    def total(self) -> int:
        return self.國文 + self.英文 + self.數學 + self.地理 + self.歷史 + self.社會 + self.品德
    
    @property
    def sum(self) -> int:
        return self.國文 + self.英文 + self.數學 + self.地理 + self.歷史 + self.社會 + self.品德

class Students(RootModel):
    root:list[Student]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self,item):
        return self.root[item]

with open('學生分數.csv',encoding='utf8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #for row in reader:
    #    print(row)
    students = Students(reader)

for student in students:
    print(student.total())
    print(student.sum)


```

    597
    597
    463
    463
    569
    569
    534
    534
    467
    467
    476
    476
    503
    503
    515
    515
    470
    470
    512
    512
    495
    495
    490
    490
    498
    498
    486
    486
    558
    558
    478
    478
    509
    509
    475
    475
    506
    506
    499
    499
    524
    524
    510
    510
    499
    499
    527
    527
    465
    465
    527
    527
    465
    465
    519
    519
    404
    404
    531
    531
    531
    531
    490
    490
    527
    527
    475
    475
    560
    560
    434
    434
    507
    507
    512
    512
    538
    538
    533
    533
    501
    501
    515
    515
    453
    453
    534
    534
    542
    542
    475
    475
    500
    500
    491
    491
    406
    406
    500
    500

