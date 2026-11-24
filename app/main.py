from fastapi import FastAPI, HTTPException, Depends #deepend gives endpoint ready db session 
from app.schemas.report import ReportCreate, ReportResponse, ReportUpdate 
from sqlalchemy.orm import Session 
from app.database import get_db 
from app.models.report import Report 
from sqlalchemy import select

app = FastAPI(title="Warsaw Alert API.")


@app.get("/health")
def get_health():
    return {"status": "ok"}


@app.get("/version")
def get_version():
    return {"version": "0.1.0"}


@app.post("/reports", response_model=ReportResponse, status_code=201)
def post_report(report: ReportCreate, db:Session=Depends(get_db)):
    new_report = Report(**report.model_dump()) #convert from pydantic-data into asgumets 
    #sqlalchemy constuctors-models (from dictionery into normal code)
     
    db.add(new_report)
    db.commit()
    db.refresh(new_report) #reloads the object from the db (adds indexes after commit)
    return new_report

@app.get("/reports", response_model=list[ReportResponse])#return a list of reports 
def get_reports(db: Session = Depends(get_db)):
    statement = select(Report)
    reports = db.scalars(statement).all()
    return reports 

@app.get("/reports/{report_id}", response_model=ReportResponse)
def get_post(report_id: int, db: Session = Depends(get_db)):
    report = db.get(Report, report_id) # find by key and can use object which is already in identity map
    #without sending the additional sql request 
    
    if report is None: 
        raise HTTPException(
            status_code=404, 
            detail="Report not found"
        )
    return report

@app.delete("/reports/{report_id}", status_code=204)
def delete_report(report_id: int, db: Session = Depends(get_db)):
    report = db.get(Report, report_id)
    
    if report is None: 
        raise HTTPException(
            status_code=404, 
            detail = "Report not found"
        )
    db.delete(report)
    db.commit()
    
@app.patch("/reports/{report_id}", response_model=ReportResponse)
def update_report(
    report_id: int, 
    data: ReportUpdate,
    db: Session = Depends(get_db)
):
    report = db.get(Report, report_id)
    
    if report is None: 
        raise HTTPException(
            status_code=404, 
            detail="Report not found"
        )
        
    if data.status is not None: 
        report.status = data.status
        
    db.commit()
    db.refresh(report)
    
    return report 
