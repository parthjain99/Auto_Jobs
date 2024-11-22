import asyncio
import streamlit as st
from src.google_smart import *

# Title of the app
st.title('Resume AI')

# Upload resume file
resume_file = st.file_uploader('Upload your resume', type=['pdf'])
if resume_file:
    # Read uploaded file as bytes
    resume_file_bytes = resume_file.read()

    # Process resume file (ensure input_pdf_setup works properly)
    txt = input_pdf_setup(resume_file_bytes)

# Input for job description
jd = st.text_area("Enter job description")
company = st.text_input("Enter Company name")

analyze_resume =st.button("Analyze Resume based on Job description")
ats_match =st.button("ATS Match")
cv = st.button("Generate Cover Letter")

if analyze_resume:
    if not resume_file or not jd or not company:
        st.warning("Please upload a resume, enter a job description and company name before submitting.")
            # Run concurrent tasks
    with st.spinner("Analyzing resume..."):
        try:
            eval_file = get_eval(jd, txt)

        except Exception as e:
            st.error(f"The service is in high demand. Please try again later.")
    st.subheader("Suggested Improvements")
    st.markdown(eval_file)

if ats_match:
    if not resume_file or not jd or not company:
        st.warning("Please upload a resume, enter a job description and company name before submitting.")
    with st.spinner("Getting resume match scores..."):
        try:
            job_match = get_match_score(jd, txt)
        except Exception as e:
            st.error(f"The service is in high demand. Please try again later.")

        # Display evaluation result
    st.subheader("Evaluation Result")
    st.markdown(job_match)

if cv:
    if not resume_file or not jd or not company:
        st.warning("Please upload a resume, enter a job description and company name before submitting.")

    with st.spinner("Generating Cover letter..."):
        try:
            cv, file = cover_letter_unified_prompt(jd, txt, company)
        except Exception as e:
            st.error(f"The service is in high demand. Please try again later.")

    # Display Cover Letter and Download Button
    st.subheader("Cover Letter")
    st.text_area(label ="Cover Letter", value = cv, height = 500)
    st.download_button(
        label='Download Cover letter as .docx file',
        data=file,
        file_name="company.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
