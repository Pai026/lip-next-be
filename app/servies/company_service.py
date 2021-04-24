from sqlalchemy.orm import Session
from ..schemas.CompanySchema import (Company, InternshipKeywords, Categories, Keywords)
def get_all_companies(db: Session,start,end):
    return db.query(Company).offset(start).limit(end).all()
    
def get_company_by_id(db: Session,id):
    return db.query(Company).filter(Company.internship_id == id).first()

def get_company_by_category_id(db: Session,id):
    return db.query(Company).filter(Company.category_id == id).all()

def get_company_by_occupation_or_keyword(db: Session,oid,kid):
    occupation_list = db.query(Company).filter(Company.category_id == oid).all()
    keyword_list = db.query(InternshipKeywords).filter(InternshipKeywords.keyword_id == kid).all()
    if(kid==0) and (oid==0):
        return db.query(Company).all()
    if(kid==0):
        return occupation_list
    elif(oid==0):
        return db.query(Company).join(InternshipKeywords,Company.keywords).filter(InternshipKeywords.keyword_id == kid).all()
    else:
        return db.query(Company).join(InternshipKeywords,Company.keywords).filter(Company.category_id == oid,InternshipKeywords.keyword_id == kid).all()

def get_all_category_ids(db: Session):
    return db.query(Categories).all()

def get_all_keywords(db: Session):
    return db.query(Keywords).all()
def get_keywords_of_company(db: Session,iid):
    return db.query(Keywords).join(InternshipKeywords,Keywords.keywords).filter(InternshipKeywords.internship_id == iid).all()
