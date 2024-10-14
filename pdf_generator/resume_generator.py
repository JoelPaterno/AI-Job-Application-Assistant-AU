import jinja2
import pdfkit
import json
from datetime import datetime

def generate_resume(title, company):
    today_date = datetime.today().strftime('%d %b, %Y')
    with open('pdf_generator/resume_data.json') as f:
            resume_data = json.load(f)

    content = resume_data

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

#generate_resume("testtitle", "testcompany")
