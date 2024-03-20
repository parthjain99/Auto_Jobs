# *Automated Application Tracker for Candidates* with AI cover letter generator and new Company folder creation.

*This project is an automated application tracker for candidates.
It provides features such as generating cover letters with AI and
tracking job applications, it also helps with customizing your Resume
as it creates a separate folder for each company.*

## *Getting Started*

*To get started, follow these steps:*

1. *Make sure you have Python 3 installed on your system.*
2. *Install the project dependencies:*

   - *Run the command: `make install`*
3. *Set up the configuration file:*

   - *Configure the necessary settings in the `config.py` file. **IMPORTANT***
4. *Run the setup script:*

   - *Run the command: `make setup`* *Dont skip step 4*
5. *Place the desired resume templates in the templates directory:*

   - *For each role type  you have added in the config file, add a resume for the same in both docx and pdf formats.*
6. *To generate a cover letter and create a folder for a specific role and company, run the following command:*

   - *Run the command: `make run r="<role abreviation>" c="<Company name>"`*
   - *It will ask for the job description, provide that and then press `Ctrl + D`.*
   - *Your cover letter and folder will be created, along with suggestions to improve your resume and tailor it.*

*Once the setup is complete, you can start using the application to track your job applications and generate cover letters with AI.*

***Note:** Make sure to have Python 3 installed on your system before proceeding with the setup.*
