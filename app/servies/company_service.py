from sqlalchemy.orm import Session
from ..schemas.CompanySchema import (Company, InternshipKeywords, Categories, Keywords)
def get_all_companies(db: Session,start,end):
    keywords=[]
    data=db.query(Company,Categories).join(Company,Categories.company).offset(start).limit(end).all()
    return push_keyword_into_company_class(data,db)
   
def push_keyword_into_company_class(data,db):
    for company,i in data:
        company.__init__()
        keyword=get_keywords_of_company(db, company.internship_id)
        if(keyword==[]):
            company.keyword="NULL"
        else:
            company.keyword=keyword
    return data



def get_company_by_id(db: Session,id):
    data = db.query(Company,Categories).join(Company,Categories.company).filter(Company.internship_id == id).first()
    return push_keyword_into_company_class(data,db)

def get_company_by_category_id(db: Session,id):
    return db.query(Company).filter(Company.category_id == id).all()

def get_company_by_occupation_or_keyword(db: Session,oid,kid):
    data = db.query(Company,Categories).join(Company,Categories.company).filter(Company.category_id == oid).all()
    if(kid==0) and (oid==0):
        data=db.query(Company,Categories).join(Company,Categories.company).all()
        return push_keyword_into_company_class(data,db)
    if(kid==0):
        return push_keyword_into_company_class(data,db)
    elif(oid==0):
        data= db.query(Company,Categories).join(Company,Categories.company).join(InternshipKeywords,Company.keywords).filter(InternshipKeywords.keyword_id == kid).all()
        return push_keyword_into_company_class(data,db)
    else:
        data= db.query(Company,Categories).join(Company,Categories.company).join(InternshipKeywords,Company.keywords).filter(Company.category_id == oid,InternshipKeywords.keyword_id == kid).all()
        return push_keyword_into_company_class(data,db)

def get_all_category_ids(db: Session):
    return db.query(Categories).all()

def get_all_keywords(db: Session):
    return db.query(Keywords).all()
def get_keywords_of_company(db: Session,iid):
    return [keyword_name for keyword_name in db.query(Keywords.keyword_name).join(InternshipKeywords,Keywords.keywords).filter(InternshipKeywords.internship_id == iid).distinct()]
