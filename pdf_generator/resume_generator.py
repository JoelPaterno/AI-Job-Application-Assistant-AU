import jinja2
import pdfkit
import json
from datetime import datetime
import sys
sys.path.insert(0, 'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU')
from llm.llm_handler import generate_resume_skills

def generate_resume(job_description,title, company):
    today_date = datetime.today().strftime('%d %b, %Y')
    with open('pdf_generator/resume_data.json') as f:
            resume_data = json.load(f)

    content = resume_data

    #update skills with chat gpt call
    skills = generate_resume_skills(job_description, resume_data)
    content["skills"] = skills

    template_loader = jinja2.FileSystemLoader('C:\\Users\\joelp\\AI-Job-Application-Assistant-AU\\pdf_generator\\templates')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('resume_template_1.html')
    output_text = template.render(content)

    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_string(
        output_text, f'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU\\files\\resumes\\{title} {company} Resume.pdf', 
        configuration=config,
        css="C:\\Users\\joelp\\AI-Job-Application-Assistant-AU\\pdf_generator\\styles\\resume_template_1_style.css",
        )
