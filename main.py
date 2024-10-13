import streamlit as st
import pandas as pd
from database.models import JobPost
import sys
sys.path.insert(0, 'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU')
from job_scraper.jobspy_search import run_jobspy_search

st.title("AI Job Application Assistant AU")
st.write("Welcome to AI Job Application Assistant AU")

#Main Section 
if 'Roles' not in st.session_state:
    st.session_state.Roles = []

radio = st.radio(
    "Role's to look for:", 
    (role for role in st.session_state.Roles)
)

side_new_role = st.text_input("Enter new role: ", key="new_role")


def add_role():
    """
    Add a new role to the list of roles to look for. This function is
    called when the "Add new role" button is clicked.
    """
    if st.session_state.new_role:
        st.session_state.Roles.append(st.session_state.new_role)
        st.session_state.new_role = ""

side_button = st.button("Add new role", on_click=add_role)

def run_job_search(roles_to_search : list[str]):
    """
    The function is called when the "Run Job Search" button is clicked.
    """
    for role in roles_to_search:
        #st.write(f"Job Search Starting for {role} role...")

        #Run linkedin, indeed and glassdoor search

        with st.spinner('Searching...'):
            jobs_found = run_jobspy_search(role)
        st.success("Done!")
            
        #st.write(f"Job Search Complete for {role} role.")
        print(f"Found {len(jobs_found)} jobs")

        
        jobs_to_display = pd.DataFrame(data=jobs_found, columns=['site', 'job_url', 'job_url_direct', 'title', 'company', 'location', 'job_type', 'date_posted', 'emails', 'description',])
        jobs_to_display.to_dict()
        #print(jobs_to_display['title'][0])
        #st.dataframe(jobs_to_display)

        def add_job_for_application(site, title, company, location, jobType, description, job_url, job_url_direct, date_posted):
            job = JobPost()
            job.add_job(site, title, company, location, jobType, description, job_url, job_url_direct, date_posted)

        for job in range(len(jobs_to_display)):
            site = jobs_to_display['site'][job]
            title=jobs_to_display['title'][job]
            company=jobs_to_display['company'][job]
            location=jobs_to_display['location'][job]
            jobType=jobs_to_display['job_type'][job]
            description=jobs_to_display['description'][job]
            job_url=jobs_to_display['job_url'][job]
            job_url_direct=jobs_to_display['job_url_direct'][job]
            date_posted=jobs_to_display['date_posted'][job]
            with st.expander(title):
                st.write(site)
                st.write(company)
                st.write(date_posted)
                st.write(location)
                st.write(jobType)
                st.write(description)
                st.write(job_url)
                st.write(job_url_direct)
                st.button("Prepare Application", key=f"addJob{job}",on_click=add_job_for_application(site, title, company, location, jobType, description, job_url, job_url_direct, date_posted))

st.button("Run Job Search", on_click=run_job_search(st.session_state.Roles))



#Side Bar

st.sidebar.file_uploader("Upload your resume", type=["pdf"])