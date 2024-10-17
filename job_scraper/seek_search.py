import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.insert(0, 'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU')

from database.models import JobPost
from database.database import get_db

def extract_job_id(url):
    # Use regex to find the job ID
    match = re.search(r'/job/(\d+)\?', url)
    
    if match:
        print(match.group(1))
        return match.group(1)
    else:
        return None

def get_job_from_url(url: str) -> JobPost:
    job_id = extract_job_id(url)
    try:
        response = requests.get(f"https://www.seek.com.au/job/{job_id}")

        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        parsed_html = soup.prettify()
        
        site ="seek"
        title = soup.find('h1', {'data-automation': 'job-detail-title'}).text.strip()
        company = soup.find('span', {'data-automation': 'advertiser-name'}).text.strip()
        location = soup.find('span', {'data-automation': 'job-detail-location'}).text.strip()
        jobType = soup.find('span', {'data-automation': 'job-detail-work-type'}).text.strip()
        description_div = soup.find('div', {'data-automation': 'jobAdDetails'})
        description = description_div.get_text(separator='\n', strip=True)
        job_url = url
        job_url_direct = "url"
        date_posted=None
        print(title, company, location, jobType, description, job_url, job_url_direct, date_posted)
        
        db=next(get_db())
        #Add job to database
        job = JobPost()
        job.add_job(db,site, title, company, location, jobType, description, job_url, job_url_direct, date_posted)

        return job
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

    