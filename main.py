import streamlit as st
import pandas as pd
from database.models import JobPost
from pdf_generator.cover_letter_generator import generate_cover_letter
from pdf_generator.resume_generator import generate_resume
from job_scraper.jobspy_search import run_jobspy_search
import json
import sys


sys.path.insert(0, 'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU')


#Main Section 
def init_session_state():
    """
    Initialize the session state by setting the default values for the Roles list and
    the job_search_results dictionary. This function is called at the beginning of the
    app, and is used to ensure that the session state is in a valid state before the
    app starts running.

    Returns:
        None
    """
    if 'Roles' not in st.session_state:
        st.session_state.Roles = []
    if 'job_search_results' not in st.session_state:
        st.session_state.job_search_results = {}

def add_role():
    """
    Add a new role to the list of roles to look for. This function is
    called when the "Add new role" button is clicked.
    """
    if st.session_state.new_role:
        st.session_state.Roles.append(st.session_state.new_role)
        st.session_state.new_role = ""

def run_job_search(roles_to_search : list[str]):
    """
    The function is called when the "Run Job Search" button is clicked.
    """
    for role in roles_to_search:
        if role not in st.session_state.job_search_results:
            with st.spinner(f'Searching for {role}...'):
                jobs_found = run_jobspy_search(role)
                job_results = pd.DataFrame(data=jobs_found, columns=['site', 'job_url', 'job_url_direct', 'title', 'company', 'location', 'job_type', 'date_posted', 'emails', 'description',])
                job_results.to_dict()
            st.success(f"Found {len(jobs_found)} jobs for {role}")
            st.session_state.job_search_results[role] = job_results

        

def add_job_for_application(site, title, company, location, jobType, description, job_url, job_url_direct, date_posted):
    job = JobPost()
    job.add_job(site, title, company, location, jobType, description, job_url, job_url_direct, date_posted)

        

def main():

    st.title("AI Job Application Assistant AU")
    st.write("Welcome to AI Job Application Assistant AU")
    init_session_state()
    #Side Bar

    st.sidebar.file_uploader("Upload your resume", type=["pdf"])

    #Main Section

    for role in st.session_state.Roles:
        st.checkbox(role, key=role)

    new_role = st.text_input("Enter new role: ", key="new_role")
    new_role_button = st.button("Add new role", on_click=add_role)

    st.button("Run Job Search", on_click=run_job_search(st.session_state.Roles))

    #Display Job Search Results

    for role, jobs in st.session_state.job_search_results.items():
            st.subheader(f"Results for {role}")
            for i, job in enumerate(jobs):
                site = jobs['site'][i]
                title=jobs['title'][i]
                company=jobs['company'][i]
                location=jobs['location'][i]
                jobType=jobs['job_type'][i]
                description=jobs['description'][i]
                job_url=jobs['job_url'][i]
                job_url_direct=jobs['job_url_direct'][i]
                date_posted=jobs['date_posted'][i]
                if pd.isna(site):
                    site = None
                if pd.isna(title):
                    title = None
                if pd.isna(company):
                    company = None
                if pd.isna(location):
                    location = None
                if pd.isna(jobType):
                    jobType = "Unknown"
                if pd.isna(description):
                    description = None
                if pd.isna(job_url):
                    job_url = None
                if pd.isna(job_url_direct):
                    job_url_direct = None
                if pd.isna(date_posted):
                    date_posted = None
                with st.expander(title):
                    st.write(site)
                    st.write(company)
                    st.write(date_posted)
                    st.write(location)
                    st.write(jobType)
                    st.write(description)
                    st.write(job_url)
                    st.write(job_url_direct)
                    if st.button("Prepare Application", key=f"{title} {company}"):
                        add_job_for_application(site, title, company, location, jobType, description, job_url, job_url_direct, date_posted)
                        job_data = f"title: {title}, company: {company}, location: {location}, jobType: {jobType}, description: {description}"
                        with open('pdf_generator/resume_data.json') as f:
                            resume_data = json.load(f)
                        generate_cover_letter(job_description=job_data, company_name=company, job_title=title)
                        generate_resume(title, company)

if __name__ == "__main__":
    main()