from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey, PickleType
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableList


class Company(Base):
    __tablename__ = 'internships'

    internship_id = Column(Integer, primary_key=True)
    company_name = Column(String)
    company_url = Column(String)
    internship_outline = Column(String)
    internship_tittle = Column(String)
    internship_detail_top = Column(String)
    internship_proposal = Column(String)
    company_logo = Column(String)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    internship_detail_1 = Column(String)
    internship_detail_2 = Column(String)
    internship_image_1 = Column(String)
    internship_image_2 = Column(String)
    keywords = relationship("InternshipKeywords")

    def __init__(self):
        self.keyword = []


class InternshipKeywords(Base):
    __tablename__ = 'internships_keywords'

    id = Column(Integer, primary_key=True)
    internship_id = Column(Integer, ForeignKey('internships.internship_id'))
    keyword_id = Column(Integer, ForeignKey('keywords.keyword_id'))


class Categories(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
    category_icon = Column(String)
    company = relationship("Company")


class Keywords(Base):
    __tablename__ = 'keywords'

    keyword_id = Column(Integer, primary_key=True)
    keyword_name = Column(String)
    keywords = relationship("InternshipKeywords")
