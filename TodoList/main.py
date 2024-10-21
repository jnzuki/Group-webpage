# Import statements
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


# Initialize a new FastAPI application
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)


db_dependency = Annotated[Session, Depends(get_db)]


