from app.database import SessionLocal
from app.models.report import Report

with SessionLocal.begin() as session:  # automatic commit
    report = Report(
        title="Car accident",
        description="Two cars collided in the center of Warsaw",
        latitude=52.2297,
        longitude=21.0122,
        category="accident",
    )
    session.add(report)
