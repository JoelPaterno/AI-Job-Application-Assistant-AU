import jinja2
import pdfkit
from datetime import datetime
import json
import sys
sys.path.insert(0, 'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU')
from llm import llm_handler


def generate_cover_letter(job_description, company_name, job_title):
    """
    This function takes data to be passed to the llm handler and generates a cover letter.:
    - all the resume data as json
    - all of the job data in a string
    """
    with open('pdf_generator/resume_data.json') as f:
            resume_data = json.load(f)

    with open('pdf_generator/cover_letter_data.json') as f:
            cover_letter_data = json.load(f)

    resume_data_str = json.dumps(resume_data)
    cover_letter = llm_handler.generate_cover_letter(job_description, resume_data_str)
    today_date = datetime.today().strftime('%d/%m/%Y')

    cover_letter_data["intro"] = cover_letter["intro"]
    cover_letter_data["lead_in"] = cover_letter["lead_in"]
    cover_letter_data["points"] = cover_letter["points"]
    cover_letter_data["outro"] = cover_letter["outro"]
    
    content = cover_letter_data
    content["current_date"] = today_date

    template_loader = jinja2.FileSystemLoader('C:\\Users\\joelp\\AI-Job-Application-Assistant-AU\\pdf_generator\\templates')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('cover_letter_template_1.html')
    output_text = template.render(content)

    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_string(
        output_text, f'.\\files\\cover_letters\\{job_title} {company_name} Cover Letter.pdf', 
        configuration=config, 
        css="C:\\Users\\joelp\\AI-Job-Application-Assistant-AU\\pdf_generator\\styles\\cover_letter_template_1_styles.css"
        )
