from flask import Blueprint,render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

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

#Loto(日期=datetime.now(),num1=23, num2=45, num3=13, num4=25, num5=42, num6=3, 特別號=8)
engine = create_engine("sqlite:///sqlViews/data.db", echo=True)
Base.metadata.create_all(engine)

@sqlApp.route('/sqlalchemy')
@sqlApp.route('/sqlalchemy/loto')
def loto():
    return render_template('loto.html',name='loto')