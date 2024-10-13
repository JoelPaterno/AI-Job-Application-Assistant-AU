import streamlit as st
import pandas as pd
import time
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
    called when the "Add new role" button is clicked in the sidebar.
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

        jobs_found = run_jobspy_search(role)
            
        #st.write(f"Job Search Complete for {role} role.")
        print(f"Found {len(jobs_found)} jobs")

        
        jobs_to_display = pd.DataFrame(data=jobs_found, columns=['site', 'job_url', 'job_url_direct', 'title', 'company', 'location', 'job_type', 'date_posted', 'emails', 'description',])
        jobs_to_display.to_dict()
        #print(jobs_to_display['title'][0])
        #st.dataframe(jobs_to_display)

        for job in range(len(jobs_to_display)):
            with st.expander(jobs_to_display['title'][job]):
                st.write(jobs_to_display['company'][job])
                st.write(jobs_to_display['date_posted'][job])
                st.write(jobs_to_display['location'][job])
                st.write(jobs_to_display['description'][job])
                st.write(jobs_to_display['job_url'][job])
                st.write(jobs_to_display['job_url_direct'][job])

st.button("Run Job Search", on_click=run_job_search(st.session_state.Roles))



#Side Bar

st.sidebar.file_uploader("Upload your resume", type=["pdf"])