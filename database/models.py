from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from .database import Base

class JobPost(Base):
    __tablename__ = "job_posts"

    id = Column(Integer, primary_key=True, index=True)
    site = Column(String)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    job_type = Column(String)
    description = Column(String)
    job_url = Column(String)
    job_url_direct = Column(String)
    date_posted = Column(DateTime)

    @classmethod
    def add_job(cls, db: Session, site, title, company, location, job_type, description, job_url, job_url_direct, date_posted):
        existing_job = db.query(cls).filter(
            cls.title == title,
            cls.site == site,
            cls.date_posted == date_posted
        ).first()

        if existing_job is None:
            new_job = cls(
                site=site,
                title=title,
                company=company,
                location=location,
                job_type=job_type,
                description=description,
                job_url=job_url,
                job_url_direct=job_url_direct,
                date_posted=date_posted
            )
            db.add(new_job)
            db.commit()
            db.refresh(new_job)
            return new_job

    @classmethod
    def get_all_jobs(cls, db: Session) -> list:
        return db.query(cls).all()