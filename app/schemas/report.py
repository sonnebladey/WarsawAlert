from pydantic import BaseModel, Field


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
    status: str | None = None 
    