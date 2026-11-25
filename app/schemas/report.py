from pydantic import BaseModel, Field
from enum import Enum


class ReportStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class ReportCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=10, max_length=500)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    category: str

class ReportResponse(ReportCreate):
    id:int
    status:str 


class ReportUpdate(BaseModel):
    status: ReportStatus | None = None 
