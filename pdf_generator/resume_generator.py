import jinja2
import pdfkit
from datetime import datetime

name = "John Doe"
email = "john.doe@email.com"
phone = "(123) 456-7890"
address = "123 Main St, Anytown, ST 12345"
summary = "Experienced software developer with a passion for creating efficient and scalable applications."
title = "Senior Software Developer"
today_date = datetime.today().strftime('%d %b, %Y')

content = {
    "name": name,
    "email": email,
    "phone": phone,
    "address": address,
    "summary": summary,
    "title": title
    }

template_loader = jinja2.FileSystemLoader('.\\templates')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('resume_template_1.html')
output_text = template.render(content)
print(output_text)

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_string(output_text, f'{today_date} Resume.pdf', configuration=config)


