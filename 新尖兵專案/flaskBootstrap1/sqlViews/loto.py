from flask import Blueprint,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc

sqlApp = Blueprint("sql",__name__)

Base = declarative_base()
class Loto(Base):
    __tablename__ = 'loto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    日期 = Column(DateTime,nullable=False)
    num1 = Column(Integer,nullable=False)
    num2 = Column(Integer, nullable=False)
    num3 = Column(Integer, nullable=False)
    num4 = Column(Integer, nullable=False)
    num5 = Column(Integer, nullable=False)
    num6 = Column(Integer, nullable=False)
    特別號 = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<(日期='{self.日期}', num1={self.num1}, num2={self.num2},num3={self.num3},num4={self.num4},num5={self.num5},num6={self.num6},特別號={self.特別號})>"


engine = create_engine("sqlite:///sqlViews/data.db", echo=True)
Base.metadata.create_all(engine)



@sqlApp.route('/sqlalchemy')
@sqlApp.route('/sqlalchemy/loto',methods=['GET', 'POST'])
def loto():
    session = Session(engine)
    if request.method == 'POST':
        #新增資料
        valueList =list(request.form.values());
        loto=Loto(日期=datetime.now(),num1=valueList[0], num2=valueList[1], num3=valueList[2], num4=valueList[3], num5=valueList[4], num6=valueList[5], 特別號=valueList[6])
        session.add(loto)
        session.commit()

    '''
    #取出資料
    for instance in session.query(Loto).order_by(Loto.id):
        print(instance.__class__)
        print(instance.日期.__class__)
        print(instance.特別號.__class__)
    '''
    data = list(session.query(Loto).order_by(desc(Loto.id)))

    return render_template('loto.html',name='loto',data=data)