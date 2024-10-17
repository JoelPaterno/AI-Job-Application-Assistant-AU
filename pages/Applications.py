import streamlit as st
from database.models import JobPost
from database.database import get_db
from job_scraper.seek_search import get_job_from_url
from pdf_generator.cover_letter_generator import generate_cover_letter
from pdf_generator.resume_generator import generate_resume
import json



def init_session_state():
     if 'seek_url' not in st.session_state:
            st.session_state.urls = []

def prepare_seek_application(seek_link):
    """ 
    1. Validate the link
    2. extract the job id from the link
    3. get job details from job_scrpaer.seek_search 
    4. add job to the database
    5. call pdf_generator.generate_resume and pdf_generator.generate_cover_letter
    """
    db = get_db()
    job = get_job_from_url(seek_link)
    job_data = f"title: {job.title}, company: {job.company}, location: {job.location}, jobType: {job.job_type}, description: {job.description}"
    with open('pdf_generator/resume_data.json') as f:
        resume_data = json.load(f)
    generate_cover_letter(job_description=job_data, company_name=job.company, job_title=job.title)
    generate_resume(job_description=job_data, title=job.title, company=job.company)

def main():
    st.markdown("# Applied Jobs Tracker")
    st.sidebar.markdown("# Applied Jobs Tracker")

    init_session_state()
    db = next(get_db())

    seek_link = st.text_input("Enter seek link: ", key="seek_link_input")
    seek_btn = st.button("Apply", on_click=lambda: prepare_seek_application(seek_link))

    jobs_to_display = JobPost.get_all_jobs(db)

    for job in jobs_to_display:
        with st.expander(f"{job.title} - {job.company}"):
            st.write(job.site)
            st.write(job.company)
            st.write(job.date_posted)
            st.write(job.location)
            st.write(job.description)
            st.write(job.job_url)
            st.write(job.job_url_direct)
            with open(f".\\files\\cover_letters\\{job.title} {job.company} Cover Letter.pdf", "rb") as file:
                btn = st.download_button(
                    label="Download Cover Letter",
                    data=file,
                    file_name=f"{job.title} {job.company} Cover Letter.pdf",
                    mime="application/pdf",
                )
            with open(f".\\files\\resumes\\{job.title} {job.company} Resume.pdf", "rb") as file:
                btn = st.download_button(
                    label="Download Resume",
                    data=file,
                    file_name=f"{job.title} {job.company} Resume.pdf",
                    mime="application/pdf",
                )

if __name__ == "__main__":
    main()