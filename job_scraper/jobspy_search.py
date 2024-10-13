from jobspy import scrape_jobs

#Run linkedin, indeed and glassdoor search
def run_jobspy_search(role : str):
    try:
        jobs_found = scrape_jobs(
            site_name=["indeed", "linkedin", "glassdoor"],
            search_term=role,
            location="Melbourne, VIC",
            results_wanted=10, 
            country_indeed='Australia',  # only needed for indeed / glassdoor
            #linkedin_fetch_description=True, # get more info such as full description, direct job url for linkedin (slower)
        )
        return jobs_found
    except Exception as e:
        return e