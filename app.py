import asyncio
import streamlit as st
from src.google_smart import *

# Title of the app
st.title('Resume Evaluation and Cover Letter generation')

# Upload resume file
resume_file = st.file_uploader('Upload your resume', type=['pdf', 'docx'])
if resume_file:
    # Read uploaded file as bytes
    resume_file_bytes = resume_file.read()

    # Process resume file (ensure input_pdf_setup works properly)
    txt = input_pdf_setup(resume_file_bytes)

# Input for job description
jd = st.text_area("Enter job description")
company = st.text_input("Enter Company name")

# Submit button
if st.button("SUBMIT"):
    if not resume_file or not jd or not company:
        st.warning("Please upload a resume, enter a job description and company name before submitting.")
    else:
        # Run concurrent tasks
        eval_file = get_eval(jd, txt)
        cv, file = cover_letter(jd, txt, company)

        # Display evaluation result
        st.subheader("Evaluation Result")
        st.markdown(eval_file)

        # Display Cover Letter and Download Button
        st.subheader("Cover Letter")
        st.text_area(label ="Cover Letter", value = cv, height = 500)
        st.download_button(
            label='Download file',
            data=file,
            file_name="company.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
