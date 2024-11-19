from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

FName = "Parth"

LName = "Jain"

"""
Dont modify template_dir and parent_dir unless you know what you are doing
"""
template_dir = "templates" #place where the template files and folders are stored
parent_dir = "roles" #place where the files will be created

'''
Specify the role and the path of the template files and a name for the role 
'''
roleMap = { 
        "Role1":f"{template_dir}/Backend",
        "Role2":f"{template_dir}/Data_Analysis",
        "Role3":f"{template_dir}/Machine_Learning"
}


class rolePath(Enum):
        """
        Enum class representing the role paths. 
        Select abreviation for the role 
        """
        Role1 = "BE"
        Role2 = "DS"
        Role3 = "ML"
        
        def __str__(self):
                return self.value

"""
Dont modify the below code
unless you know what you are doing
"""
challenge_prompt = """
Act as an experienced career coach. Analyze the job description to uncover the primary challenges 
someone in this role would face daily. Identify the root causes of these challenges. 
Here is the job description: ```{jd}```.
"""

intro_prompt = """
Act as an experienced career coach. Write an engaging hook for my cover letter, highlighting my 
experience and qualifications to show empathy and capability in addressing the challenges: ```{challenges}```. 
Use specific examples from my resume to demonstrate past success with similar challenges. 
Keep the hook within 70 words. 
My resume: ```{resume}```. 
Job description: ```{jd}```. 
Company: ```{company}```. 
Provide only the hook, no extra text.
"""

body_prompt = """
Using the first hook: ```{hook1}```, write the next paragraph of my cover letter. Expand on relevant 
experiences from my resume to show alignment with the job description. Include specific results, achievements, 
leadership examples, innovations, technical skills, and key strengths. 
Keep the paragraph concise, up to 70 words. 
My resume: ```{resume}```. 
Job description: ```{jd}```. 
Company: ```{company}```.
"""

conclusion_prompt = """
Using the first hook: ```{hook1}``` and second hook: ```{hook2}```, write a closing paragraph for the 
cover letter. Reiterate my strong interest in the role and keep it within 50 words.
"""


get_match_prompt = """You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of 
        ATS functionality, your task is to evaluate the resume against this job description ```{jd}```. 
        give me the percentage of match if the resume matches the job description. First the output all the keywords in job description
        and then job description keywords missing in resume , and then percentage match of keyword found vs keyword total. Here is the Resume ```{resume}```"""

eval_prompt = """Be really concise and avoid generic statements, Specify How the resume bullet points
                which bullets points can be modified to tailor the resume best to the job descripion. 
                List all the points one by one. Just suggest changes in expierience and project section. 
                Be strict and tell will resume pass the screnning test. Suggest changes that are 
                related to the Job description and align with resume.
                Write the skills to be included in the resume and are missing.
                Here is resume ```{resume}``` and here is the job description ```{jd}```
                """
        