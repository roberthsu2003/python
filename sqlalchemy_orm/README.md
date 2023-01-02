# SQLAlchemy ORM
- [官方說明書](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)
- python 物件導向方法操控資料庫
- 使用python程式操控SQL Database
- 可建立,讀取,寫入,更新,刪除的運算
- 建立class 代表建立table
- 建立class Attributes 代表table的欄位

### 建立一個學生資料表(student)
- id 欄位
- name 欄位
- age 欄位
- grade 欄位

```python
class Student(Base):
	__tablename__ = 'student'
	id =  Column(Integer,primary_key=True)
	name  = Column(String(50))
	age = Column(Integer)
	grade = Columns(String(50))
```

### 安裝sqlalchemy

```python
$ pip install sqlalchemy
```

### 建立資料表流程
- 建立engine
- 建立session
- 建立table
- 建立Migrate

#### 操控不同資料庫連結語法
- [官方語法](https://docs.sqlalchemy.org/en/14/core/engines.html#backend-specific-urls)

```python
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#建立engine
engine = create_engine('sqlite:///student.db',echo=True, future=True)

#建立session
Session = sessionmaker(bind=engine)
session = Session()

#建立要繼承的base
Base = declarative_base()

#建立自訂表格的class
class Student(Base):
    __tablename__ = 'student'
    
    id =  Column(Integer,primary_key=True)
    name = Column(String(50))
    age  =  Column(Integer)
    grade =  Column(String(50))

#執行matadata內資訊,table的建立(Migrate)
Base.metadata.create_all(engine)

```

## Insert Data
- 建立table class的實體
- 將資料加入至session內
- commit

```python
student1 = Student(name="Jerin", age=27, grade="Fifth")
session.add(student1)

student2 = Student(name="Anita", age=24, grade="Fourth")
student3 = Student(name="Jefin", age=21, grade="Third")
session.add_all([student2, student3])
session.commit()
```

## Read Data
- 取得表格內所有資料
- 排序所有資料
- 過濾資料
- 計算資料筆數

```python
#get all data
students = session.query(Student)

for student in students:
    print(student.name, student.age, student.grade)
    
#結果:======================
Jerin 27 Fifth
Anita 24 Fourth
Jefin 21 Third

#get data in order
students = session.query(Student).order_by(Student.name)
for student in students:
    print(student.name, student.age, student.grade)
    
#結果:======================
Anita 24 Fourth
Jefin 21 Third
Jerin 27 Fifth

#get data by filtering

student = session.query(Student).filter(Student.name=="Jerin").first()
print(student.name, student.age, student.grade)

#結果:=========================
Jerin 27 Fifth

from sqlalchemy import or_

students = session.query(Student).filter(or_(Student.name=="Jerin",Student.name=="Anita"))
for student in students:
    print(student.name, student.age, student.grade)
    
#結果:=======================
Jerin 27 Fifth
Anita 24 Fourth

#count the number of results
students_count = session.query(Student).filter(or_(Student.name=="Jerin",Student.name=="Anita")).count()

print(students_count)

#結果:=======================
2

```

## Update Data
- 取得Record
- 改變資料
- commit 改變的資料

```python
student = session.query(Student).filter(Student.name == 'Jerin').first()
student.name = "Kevin"
session.commit()

student = session.query(Student).filter(Student.name == 'Kevin').first()
print(student.name)

#結果:=======================
Kevin
```

## Delete Data
- 取得Record
- 刪除資料
- commit 刪除的資料

```python
student = session.query(Student).filter(Student.name=="Kevin").first()
session.delete(student)
session.commit()
```
