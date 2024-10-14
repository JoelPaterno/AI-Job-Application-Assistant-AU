import streamlit as st
from database.models import JobPost

st.markdown("# Applied Jobs Tracker")
st.sidebar.markdown("# Applied Jobs Tracker")

jobs_to_display = JobPost.get_all_jobs()

for job in jobs_to_display:
    with st.expander(job.title):
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
