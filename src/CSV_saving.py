import pandas as pd
import datetime
import sys
sys.path.append('..')

def save_to_file(company_name, jd, role):
    # Load the existing CSV file into a DataFrame
    df = pd.read_csv("assets/Job Tracker.csv")
    # Create a new DataFrame for the new row
    new_row_df = pd.DataFrame({
        'COMPANY': [company_name],
        'JOB TITLE': [role],
        'APP SUBMITTED DATE': [datetime.date.today()],
        'JOB DESCRIPTION LINK': [jd]
    })

    # Append the new row DataFrame to the existing DataFrame
    updated_df = pd.concat([df, new_row_df], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    updated_df.to_csv("assets/Job Tracker.csv", index=False)


# # Example usage
# save_to_file('Example Company', 'http://example.com/job_description', 'Software Engineer')