# *Automated Application Tracker for Candidates* with AI cover letter generator and new Company folder creation.

*This project is an automated Command line tool tracker for candidates.
It provides features such as generating cover letters with AI and
tracking job applications; it also helps with customizing your Resume
as it creates a separate folder for each company.*

## Demo


<iframe width="560" height="315" src="https://www.youtube.com/embed/uD15hxrJPgU?si=Q-ThaGRdF-kPOuXk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## *Getting Started*

*To get started, follow these steps:*

1. *Make sure you have Python 3 installed on your system.*
2. make sure to create a .env file like in .env.example and add the API keys
3. *Install the project dependencies:*

   - *Run the command: ```make install```*
4. *Set up the configuration file:*
      
   - *Configure the necessary settings in the `config.py` file. **IMPORTANT***
   - Also update the information in assets/cover_letter.docx
     
5. *Run the setup script:*

   - *Run the command: `make setup`* *Dont skip step 4*
6. *Place the desired resume templates in the templates directory:*

   - *For each role type  you have added in the config file, add a resume in both docx and pdf formats.* find them in templates 
7. *To generate a cover letter and create a folder for a specific role and company, run the following command:*

   - *Run the command: `make run r="<role abreviation>" c="<Company name>"`*
   - *It will ask for the job description; provide that and then press `Ctrl + D.`*
   - *Your cover letter and folder will be created, along with suggestions to improve your resume and tailor it.*

*Once the setup is complete, you can start using the application to track your job applications and generate cover letters with AI.*

***Note:** If you want to contribute, fork this GitHub repository, make changes, and create a pull request.*

*We appreciate your contributions and look forward to your pull requests!*
