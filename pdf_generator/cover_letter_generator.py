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

    resume_data_str = json.dumps(resume_data)
    cover_letter = llm_handler.generate_cover_letter(job_description, resume_data_str)
    today_date = datetime.today().strftime('%d %m %Y')

    with open('pdf_generator/cover_letter_data.json') as f:
            cover_letter_data = json.load(f)
    
    content = cover_letter_data
    content["current_date"] = today_date
    content["content"] = cover_letter

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
    
testdescription = """
TECHNICAL IT SUPPORT OFFICER - WORK FROM HOME

POSITION DESCRIPTION

The Offer:

Podium IT is seeking a full-time IT Support Technician with over one year of Managed Service Provider (MSP) experience to join our dynamic team. As an established IT support company with a diverse client base across various industries and sizes, we offer an exciting opportunity to work alongside experienced technicians. You will support our largest clients by providing both onsite and remote IT assistance as needed.

Our Commitment:

At Podium IT, we are dedicated to offering you unique exposure to the latest technologies. You will be involved in developing and integrating critical IT infrastructure projects both internally and externally. With the majority of our clients operating in the healthcare sector—a niche market—you will gain exclusive experience with specialized software suites.

As part of the Podium IT team, you will join a tight-knit, energetic workforce that emphasizes learning and growth. We are committed to fostering your future at Podium IT through an open workplace culture and flexible working conditions. Flexible options include the ability to work from home, provided you can demonstrate the skills required to work autonomously.

The Role:

As one of the first points of contact for our clients, you will assist them as they raise IT issues, primarily over the phone but also through emails and other communication channels.

You will excel in this role if you have expert troubleshooting skills, a highly professional client service etiquette, and a passion for IT support. Previous MSP experience of more than one year is required. We are seeking a candidate with an understanding of the basics of small business IT networks. The following skills will be highly regarded:

Previous MSP experience (preferably more than 1 year)
Experience with medical software like Medical Director and Best Practice
Experience with Atera RMM and PSA
Proficiency with Windows Server 2008–2022 (Domain, Workgroup, RDP)
Familiarity with Windows 7–11
Knowledge of IP addressing
Understanding of DNS, DHCP, WAN, WLAN, VPN, and LAN
Experience with network switches and routers
Server hardware configuration skills
Ability to manage printer settings
Knowledge of cloud infrastructure (AWS/Azure)
Experience with 3CX Phone Systems
Familiarity with cPanel web hosting
The role encompasses two main areas of responsibility:

1. Podium IT Remote Support Technician

As a Technical Support Officer, you will be required to respond to all client inquiries promptly and professionally.

Core Responsibilities:

Being available to answer incoming client inquiries from Monday to Friday, 8:30 AM – 5:00 PM, unless otherwise stated.
Creating and resolving tickets from all incoming client inquiries, with guidance on escalating outstanding tickets.
Continuously improving internal processes where needed, such as the complete ticket cycle and client experiences.
Maintaining the client site visit calendar.
Handling software and hardware procurement.
Quoting for software and hardware supply and installation.
Participating in the rotating on-call roster.
Engaging in regular operations and team meetings with the Director to present findings and suggest solutions for improved business health.
Key KPI: Correctly create and resolve most of your tickets and client inquiries, successfully manage other technicians’ onsite calendar, maintain a professional manner and positive attitude when communicating with clients, and enjoy your job while assisting Podium IT with its mission—"The Best IT Support... Ever..."

2. Podium IT Onsite Support Technician

An integral part of the role is executing onsite IT support as required. To perform onsite support effectively, you are required to complete all pending tasks and professionally respond to any client requests during your visit.

As the company expands, your requirement for onsite support will increase. There are also opportunities for you to progress into a team leader position and organize the day-to-day activities of other technicians.

Key KPI: Demonstrate competence in the activities required during onsite IT support, show initiative, and always represent Podium IT to the highest standard.

Remuneration:

We are committed to offering a salary package of $70,000–$75,000 per annum pro rata, exclusive of superannuation and a car allowance, which is paid as a reimbursement. The salary is negotiable based on experience and skill and includes a six-month probation period. A salary review can be conducted following this probation period. During probation, you will use your own car if required and will be issued a travel allowance to compensate.

Upskilling and Certification Support:

We encourage our staff to continuously upskill. Podium IT is committed to supporting your studies and helping you obtain industry certifications.

Company Culture and Growth:

Our team thrives on remote collaboration, emphasizing outcome-driven work over micromanagement. You'll have the autonomy to manage your tasks while contributing to our mission of company growth through innovative marketing strategies and enhancing client service levels.

Benefits and Perks:

Enjoy travel allowances and the privilege to work from home, fostering a perfect balance between professional and personal life. Podium IT will invest in your learning and assist you with upskilling your CV.

Employer questions
Your application will include the following questions:
How many years' experience do you have as an Information Technology Support Technician?
Which of the following statements best describes your right to work in Australia?
Do you have a current Australian driver's licence?
What's your expected annual base salary?
Are you available to work outside your usual hours when required? (e.g. weekends, evenings, public holidays)
Do you own or have regular access to a car?
"""
#generate_cover_letter(testdescription, "testcompany", "testtitle")