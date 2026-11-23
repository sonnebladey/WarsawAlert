from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column 
from app.models.base import Base

class Report(Base):
    __tablename__ = "reports"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(100), nullable=False)
    description:Mapped[str] = mapped_column(String(500), nullable=False)
    category:Mapped[str] = mapped_column(String(50), nullable=False)
    latitude:Mapped[float] = mapped_column(Float, nullable=False)
    longitude:Mapped[float] = mapped_column(Float, nullable=False)
    status:Mapped[str] = mapped_column(String(20),default="pending")
    
     