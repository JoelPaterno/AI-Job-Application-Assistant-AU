summarize_prompt_template = """
As a seasoned HR expert, your task is to identify and outline the key skills and requirements necessary for the position of this job. Use the provided job description as input to extract all relevant information. This will involve conducting a thorough analysis of the job's responsibilities and the industry standards. You should consider both the technical and soft skills needed to excel in this role. Additionally, specify any educational qualifications, certifications, or experiences that are essential. Your analysis should also reflect on the evolving nature of this role, considering future trends and how they might affect the required competencies.

Rules:
Remove boilerplate text
Include only relevant information to match the job description against the resume

# Analysis Requirements
Your analysis should include the following sections:
Technical Skills: List all the specific technical skills required for the role based on the responsibilities described in the job description.
Soft Skills: Identify the necessary soft skills, such as communication abilities, problem-solving, time management, etc.
Educational Qualifications and Certifications: Specify the essential educational qualifications and certifications for the role.
Professional Experience: Describe the relevant work experiences that are required or preferred.
Role Evolution: Analyze how the role might evolve in the future, considering industry trends and how these might influence the required skills.

# Final Result:
Your analysis should be structured in a clear and organized document with distinct sections for each of the points listed above. Each section should contain:
This comprehensive overview will serve as a guideline for the recruitment process, ensuring the identification of the most qualified candidates.

# Job Description:
```
```

---

# Job Description Summary"""

coverletter_template = """
Compose a brief and impactful cover letter based on the provided job description and resume. The letter should be no longer than three paragraphs and should be written in a professional, yet conversational tone. Avoid using any placeholders, and ensure that the letter flows naturally and is tailored to the job.

Analyze the job description to identify key qualifications and requirements. Introduce the candidate succinctly, aligning their career objectives with the role. Highlight relevant skills and experiences from the resume that directly match the job’s demands, using specific examples to illustrate these qualifications. Reference notable aspects of the company, such as its mission or values, that resonate with the candidate’s professional goals. Conclude with a strong statement of why the candidate is a good fit for the position, expressing a desire to discuss further.

Please write the cover letter in a way that directly addresses the job role and the company’s characteristics, ensuring it remains concise and engaging without unnecessary embellishments. The letter should be formatted into paragraphs and should not include a greeting or signature.

## Rules:
- Provide only the text of the cover letter.
- Do not include any introductions, explanations, or additional information.
- The letter should be formatted into paragraph.

## Job Description:
```
{job_description}
```
## My resume:
```
{resume}
```
"""

test_job_description = """
We Are Carlisle

Carlisle Homes is a proud, Australian-owned business with a mission to make lives better. The pride in our brand comes from the impact that we have in building homes for Australian families. What we do is special; building homes, strengthening communities, and being part of creating a new Victoria is something we wear with pride.

The opportunity we have to enrich the lives of our customers resonates deeply with our people and is a responsibility that we do not take lightly. Our focus on 'quality over quantity has provided Carlisle with strong foundations to reach the heights of success that the company is well respected for today; both within our industry and as a reputable employer on the national stage.

Carlisle Homes has been awarded the highest accolade in the housing industry - the HIA Professional Major Builder award - and has been recognised as a Best Employer, twice! Our pride doesn't stop there though… our highly valued customers consistently rate us in the top percentile on Australia's leading customer review website ProductReview.com.au.

The role:

In your new role as an IT Service Delivery Specialist, you will join a dynamic team who pride themselves on their exceptional problem-solving skills, their ability to build great relationships and provide excellent customer service across our business. Reporting into the Service Delivery Lead, you will provide frontline support across our multi-site operation.

Working within Carlisle's prestige Service Centre you will be granted exposure to an entire stack of applications with opportunities for future growth and development. You will be equipped to act as the first point of contact for all incidents and service requests whilst continuously seeking innovative ways to improve development practices and processes.

When not working from our highly acclaimed, brand new modern place of work, you will have the opportunity to travel across our remote sites, where you will build strong relationships across all departments, cementing your business partnering abilities and further collaboration across the business.

We are seeking a Service Delivery Specialist to provide a high-level of 1st and 2nd level IT support and customer service to Carlisle staff across Victoria.

The skills we're looking for:

Experience working as an IT Help Desk Support Technician (or similar)
Experience working in a ITIL environment
Well-developed problem-solving skills and experience in supporting a multi-site operation.
Excellent customer/stakeholder engagement and interpersonal skills.
Excellent Communication and organisation skills.
Carlisle perks!

As a named Best Employer (not once, but twice!) our commitment to making life better for our people speaks for itself. Here's a snapshot of our perks…

An industry first, Family Friendly Program to support parents at all stages of the parenting journey including up to 18 week paid parental leave and a $250 baby bonus
Exciting programs to support financial confidence, mental health and physical wellbeing including a virtual speaker series, Flu vaccinations, skin checks, EAP, wellbeing sessions and so many more!
Ongoing learning and development opportunities to help you reach your full potential - whether through our highly engaging and interactive e-learning platform or formally recognised courses, where here to encourage your long-term growth
Loyalty days for every year of service equating to one whole weeks extra annual leave after 5 years
Building discounts, supplier / trade discounts, and retail discounts with 400+ big name brands through our Carlisle Rewards platform
Parties, award nights, mid-year/end of year events, Family Fun Day… you name it, we celebrate it! At Carlisle we believe that celebrations are a time where true connection happens, bringing even more camaraderie to our team.
Brand new office featuring state of the art workspaces, gaming rooms, massage chairs and a rooftop sports court!
If you're seeking a challenging environment, focused on excelling as an individual and working in a vibrant team then this could be the role for you!
"""

test_resume = """
0438 219 671
joelpaterno1@gmail.com
Melbourne, VIC
cONTACT
Summary
Skills
Work Experience
Customer Service, Email Inbox Management, Phone Call Handling, in-person Support, Hardware and Software Troubleshooting, Ticketing System, Cross Team Collaborating, Strong Communication Skills, Microsoft 365, Windows, GSuite, networking fundamentals, Office Suite, Apple.
Customer Service Agent/Salesforce Project Lead
Household Capital | National Fintech | Melbourne
Customer Service Agent/Salesforce Project Lead with experience in Salesforce Email-to-Case implementation, process automation, and technical research. Led end-to-end projects, developed training resources, and collaborated with cross-functional teams to enhance customer service efficiency and business operations

Salesforce Implementation: Researched, designed, and implemented Salesforce Email-to-Case for streamlined ticketing and group inbox management, enhancing customer service efficiency.
Project Management: Led the end-to-end project lifecycle, from planning and testing to deployment and user adoption, ensuring successful execution.
Technical Research & Analysis: Conducted thorough research to evaluate different technical solutions, ensuring the chosen implementation met the company’s specific needs.
Training & Documentation: Created comprehensive training resources and documentation to support employee onboarding and ongoing use of the new system. 
Collaboration & Communication: Worked closely with cross-functional teams to align technical solutions with business objectives, ensuring a smooth transition to the new system.
March 2022 - July 2024
Computer Science graduate with a background in Biomedical and Computer Science at Monash University. Experienced in troubleshooting, IT and delivering excellent customer service. Passionate about technology and eager to start a career in IT with experience in support and providing timely and effective solutions.
Joel Paterno
Graduate Certificate of Computer Science
Monash University
Completed foundational subjects in Programming, Networking, Architecture, Algorithms and Databases. The capstone project in the software engineering subject involved designing and implementing a job posting desktop application.
February  2022 - November 2022
Salesforce
AWS
Salesforce Certified Associate  
March 2024 - August 2024
Salesforce Certified Administrator
March 2024 - Current
Salesforce Platform Developer
August 2024 - Current
AWS Certified Cloud Practitioner
August 2024 - Current
Certifications
joelpaterno.tech
Available on Request
Education
Bachelor of Biomedical Science
Monash University
Studied subjects in Biochemistry, Physics, Molecular Biology, Bioinformatics, Statistics and completed team research projects.
February  2016 - November 2018
References
"""