from .mysql_db import db, cursor

class JobPost():
    site =""
    title =""
    company =""
    location =""
    jobType =""
    description =""
    job_url =""
    job_url_direct =""
    date_posted =""

    def __init__(self, site="", title="", company="", location="", jobType="", description="", job_url="", job_url_direct="", date_posted=""):
        self.site = site
        self.title = title
        self.company = company
        self.location = location
        self.jobType = jobType
        self.description = description
        self.job_url = job_url
        self.job_url_direct = job_url_direct
        self.date_posted = date_posted    
    def add_job(self, site, title, company, location, jobType, description, job_url, job_url_direct, date_posted):
        self.site = site
        self.title = title
        self.company = company
        self.location = location
        self.jobType = jobType
        self.description = description
        self.job_url = job_url
        self.job_url_direct = job_url_direct
        self.date_posted = date_posted

        cursor.execute("""
                       INSERT INTO JobPost(
                       site, 
                       title, 
                       company, 
                       location, 
                       jobType, 
                       description, 
                       job_url, 
                       job_url_direct, 
                       date_posted
                       ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                       """, (site, title, company, location, jobType, description, job_url, job_url_direct, date_posted))
        db.commit()
    def get_all_jobs() -> list:
        results = []
        cursor.execute("SELECT * FROM JobPost")
        rows = cursor.fetchall()
        for jobpost in rows:
            site = jobpost[1]
            title = jobpost[2]
            company = jobpost[3]
            location = jobpost[4]
            jobType = jobpost[5]
            description = jobpost[6]
            job_url = jobpost[7]
            job_url_direct = jobpost[8]
            date_posted = jobpost[9]
            job = JobPost()
            job.add_job(site, title, company, location, jobType, description, job_url, job_url_direct, date_posted)
            results.append(job)
        return results