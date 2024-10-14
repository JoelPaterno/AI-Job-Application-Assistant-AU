from dotenv import load_dotenv
import os
import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from . import strings

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4")

def generate_cover_letter(job_description, resume):
    cover_letter_template = strings.coverletter_template
    #takes {job_description} for a job description and {resume} for a resume

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", cover_letter_template)]
    )

    parser = StrOutputParser()

    chain = prompt_template | model | parser

    response = chain.invoke({"job_description": job_description, "resume": resume})
    print(response)
    return response
