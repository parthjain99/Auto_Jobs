from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

FName = "Parth"

LName = "Jain"


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






