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
challenge_prompt = """Assume the role of a expierienced career coach.
    I want to stand out from other job seekers by reverse engineering the job descripion to uncover what the company is exactly lookin for.
    Analyze the job description and identify biggest challenge someone in this role would face. day to day. 
    Give me root cause of the problem. Now here is the job description ```{jd}```"""

intro_prompt = """Assume the role of a expierienced career coach. 
    Now your task is to write an attention-grabbing hook for my cover letter that highlights my 
    experience and qualifications in a way that shows I empathize and can successfully take on the 
    challenges mentioned ```{challenges}``` in the job description. Consider incorporating specific examples of how I've 
    tackled these challenges in my past work, and explore creative ways to express my enthusiasm for 
    the opportunity. Keep my hook within 70 words.
    And just give me hook nothing else no other text/header.
    I will share my resume with you here it is ```{resume}```
    Now here is the job description ```{jd}```.
    Company name is ```{company}```."""

body_prompt = """ here is the first hook {hook1}. Now, your task is to write 
    the next paragraph of my cover letter by expanding on experiences from all roles 
    from my resume that most relates to the cover letter and job description and to highlight the 
    reasons I MATCH the job description.
    Incorporate small paragraphs of specific results and achievements within the positions held by me.
    Some examples:-
        Leadership experience.
        Specific improvements or goals I met.
        State innovations/ideas where I provided value to the business.
        List technical skills & abilities.
        State one or two key strengths.

    Keep small paragraphs 70 words.
    My resume here it is ```{resume}```,
    Now here is the job description ```{jd}```.
    Company name is ```{company}```
    """

conclusion_prompt = """ here is the first hook {hook1} and the second hook {hook2}.
    Now your task is to close out the cover letter with a final paragraph reiterating my strong interest in the role.
    Be concise and keep it within 50 words."""

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
        