from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")



FName = "Parth"

LName = "Jain"

parent_dir = "/Users/parthjain/Desktop/jobs/newS"


roleMap = { 
        "Role1":"/Users/parthjain/Desktop/jobs/templates/backend",
        "Role2":"/Users/parthjain/Desktop/jobs/templates/Dataanalysis",
        "Role3":"/Users/parthjain/Desktop/jobs/templates/machine leanring"
}

class rolePath(Enum):
        Role1 = "BE"
        Role2 = "DS"
        Role3 = "ML"
        def __str__(self):
                return self.value






