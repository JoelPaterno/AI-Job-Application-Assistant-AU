import jinja2
import pdfkit
from datetime import datetime
import sys
sys.path.insert(0, 'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU')
from llm import llm_handler



name = "John Doe"
cover_letter = llm_handler.generate_cover_letter()
today_date = datetime.today().strftime('%d %b, %Y')

content = {
    "name": name,
    "cover_letter": cover_letter
    }

template_loader = jinja2.FileSystemLoader('.\\templates')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('cover_letter_template_1.html')
output_text = template.render(content)

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_string(
    output_text, f'C:\\Users\\joelp\\AI-Job-Application-Assistant-AU\\files\\cover_letters\\{today_date} Cover Letter.pdf', 
    configuration=config, 
    )