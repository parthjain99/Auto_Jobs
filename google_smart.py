import os

import google.generativeai as genai
from docx import Document
import PyPDF2
from docx.shared import Pt
from docx.shared import RGBColor
from config import (
    GOOGLE_API_KEY
)

genai.configure(api_key=GOOGLE_API_KEY)


def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        # creating a pdf file object
        pdfFileObj = open(uploaded_file, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        # printing number of pages in pdf file
        print(len(pdfReader.pages))

        # creating a page object
        pageObj = pdfReader.pages[0]
        txt = pageObj.extract_text()
        pdfFileObj.close()
        #extracting text from page
        return txt


def get_eval(jd, uploaded_file):
    if uploaded_file is not None:
        # pdf_content = input_pdf_setup(uploaded_file)
        eval_prompt = f"""Be really concise and avoid generic statements, Specify How the resume bullet points
                which bullets points can be modified to tailor the resume best to the job descripion. 
                List all the points one by one. Just suggest changes in expierience and project section. 
                Be strict and tell will resume pass the screnning test. Suggest changes that are 
                related to the Job description and align with resume, Avoid in general fixes.
                Here is resume ```{uploaded_file}``` and here is the job description ```{jd}```
                """
        response = get_gemini_response(eval_prompt)
        print(response)
    else:
        print("Please uplaod the resume")


def get_match_score(jd, resume):
    if resume is not None:
        # pdf_content = input_pdf_setup(uploaded_file)
        get_match_prompt = f"""You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of 
        ATS functionality, your task is to evaluate the resume against this job description ```{jd}```. 
        give me the percentage of match if the resume matches the job description. First the output all the keywords in job description
        and then job description keywords missing in resume , and then percentage match of keyword found vs keyword total. Here is the Resume ```{resume}```"""
        response = get_gemini_response(get_match_prompt)
        print(response)
    else:
        print("Please upload the resume")


def cover_letter(jd, resume, company):
    cv_hook1_prompt = f"""Assume the role of a expierienced career coach.
    I want to stand out from other job seekers by reverse engineering the job descripion to uncover what the company is exactly lookin for.
    Analyze the job description and identify biggest challenge someone in this role would face. day to day. 
    Give me root cause of the problem. Now here is the job description ```{jd}```. 
    """
    challenges = get_gemini_response(cv_hook1_prompt)


    input_prompt_6 =f"""
    Assume the role of a expierienced career coach. 
    Now your task is to write an attention-grabbing hook for my cover letter that highlights my 
    experience and qualifications in a way that shows I empathize and can successfully take on the 
    challenges mentioned ```{challenges}``` in the job description. Consider incorporating specific examples of how I've 
    tackled these challenges in my past work, and explore creative ways to express my enthusiasm for 
    the opportunity. Keep my hook within 70 words.
    And just give me hook nothing else no other text/header.
    I will share my resume with you here it is ```{resume}```
    Now here is the job description ```{jd}```.
    Company name is ```{company}```.
    """
    hook1 = get_gemini_response(input_prompt_6)


    input_prompt_7 = f""" here is the first hook {hook1}. Now, your task is to write 
    the next paragraph of my cover letter by expanding on experiences from all roles 
    from my resume that most relates to the cover letter and job description and to highlight the 
    reasons I MATCH the job description.
    Incorporate bulleted list of specific results and achievements within the positions held by me.
    Some examples:-
        Examples of leadership experience.
        Specific improvements or goals you met.
        State innovations/ideas where you provided value to the business.
        List your technical skills & abilities.
        State one or two key strengths.

    Keep it bullet points and within 50 words.
    My resume here it is ```{resume}```,
    Now here is the job description ```{jd}```.
    Company name is ```{company}```
    """
    hook2 = get_gemini_response(input_prompt_7)

    input_prompt_8 = f""" here is the first hook {hook1} and the second hook {hook2}.
    Now your task is to close out the cover letter with a final paragraph reiterating my strong interest in the role.
    Be concise and keep it within 50 words.
    """

    hook3 = get_gemini_response(input_prompt_8)
    cv = f"""Hello Hiring team at {company},\n\n {hook1} \n\n {hook2} \n\n {hook3} \n\n Thank you for the opportunity, \n Parth Jain"""
    return cv

if __name__ == "__main__":
    jd = """Contract negotiation is the most time-consuming, costly, and difficult component of the contract 
    lifecycle, and is barely any easier now than when lawyers were using fax machines. 
    
    Large language models have unlocked the ability to solve many contract negotiation problems at scale. If you join 
    us, you will be working with a small team to build a category-defining product that is rapidly embedding itself 
    into the lives of its users. 
    
    Latch has raised from leading investors in an unannounced funding round. We can share more details with 
    candidates who go through our interview process. 
    
    What would you be doing?
    
    We are looking for motivated and curious Software Engineers who can help us make our users’ lives better.
    
    You will have a unique opportunity to be an early member of this team, helping shape how we impact customers at scale.
    
    Our tech stack includes:
    
    React / Redux / Next.js / Node.js / Typescript
    
    OpenAI / LangChain
    
    Firebase
    
    Azure
    
    Latch might be a good fit for you if you:
    
    Have a "do what it takes" attitude. You're willing to dive into problems and solve them yourself — as one of our first engineers, you won't have anyone to delegate to.
    
    Would describe yourself as being relentlessly resourceful.
    
    Move quickly. You have a bias towards doing things *today*, rather than tomorrow.
    
    Experience working in a startup environment is preferred but not required.
    
    Are excited about the adventure of building a company!
    """
    file = "/Users/parthjain/Desktop/jobs/templates/backend/Parth_jain_resume.pdf"
    cover ="/Users/parthjain/Desktop/jobs/templates/backend/Parth Jain_cover_letter.docx"
    doc = Document(cover)
    resume = input_pdf_setup(file)
    doc.tables[0].rows[1].cells[1].text = cover_letter(jd, resume, "Latch")
    style = doc.styles.add_style('NewStyle', 1)
    style.font.name = 'Calibri'
    style.font.color.rgb = RGBColor(0,0,0)
    style.font.size = Pt(12)
    # Apply the new style to each paragraph
    for paragraph in doc.tables[0].rows[1].cells[1].paragraphs:
        paragraph.style = doc.styles['NewStyle']
    doc.save('/Users/parthjain/Desktop/jobs/templates/backend/Parth Jain_cover_letter1.docx')

