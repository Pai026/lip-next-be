from typing import List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from .routes.company_route import router as CompanyRouter

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(CompanyRouter, tags=["Company"], prefix="/api/v1/company")


@app.get("/")
def read_root():
    return {"Message": "Welcome to Lip-Next Backend End !!!"}
