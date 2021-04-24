from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = 'internships'

    internship_id = Column(Integer,primary_key=True)
    company_name = Column(String)
    company_url = Column(String)
    internship_outline = Column(String)
    internship_tittle = Column(String)
    internship_detail_top = Column(String)
    internship_proposal = Column(String)
    company_logo = Column(String)
    category_id = Column(Integer)
    internship_detail_1 = Column(String)
    internship_detail_2 = Column(String)
    internship_image_1 = Column(String)
    internship_image_2 = Column(String)
    keywords=relationship("InternshipKeywords")

class InternshipKeywords(Base):
    __tablename__ = 'internships_keywords'

    id = Column(Integer, primary_key=True)
    internship_id = Column(Integer,ForeignKey('internships.internship_id'))
    keyword_id = Column(Integer)

class Categories(Base):
    __tablename__ = 'categories'
    
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
    category_icon = Column(String)
