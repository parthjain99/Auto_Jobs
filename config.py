from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

eval_prompt = """Be really concise and avoid generic statements, Specify How the resume bullet points
                which bullets points can be modified to tailor the reusme best to the job descripion. 
                List all the points one by one. Just suggest changes in expierience and project section. 
                Be strict and tell will resume pass the screnning test. Suggest point changes that are 
                related to the Job description, Avoid in general fixes."""

get_match_prompt = """You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of 
        ATS functionality, your task is to evaluate the resume against the provided job description. 
        give me the percentage of match if the resume matches the job description. First the output all the keywords and
        then keywords missing, and then percentage match."""

FName = "Parth"

LName = "Jain"

parent_dir = "/Users/parthjain/Desktop/jobs/newS"


class rolePath(Enum):
        BE = "/Users/parthjain/Desktop/jobs/templates/backend"
        DS = "/Users/parthjain/Desktop/jobs/templates/Dataanalysis"
        ML = "/Users/parthjain/Desktop/jobs/templates/machine leanring"

