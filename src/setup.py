import os
import sys
sys.path.append("..")
from config.config import (roleMap, FName, LName, parent_dir, template_dir)
import shutil

if __name__ == "__main__":
    os.mkdir(parent_dir)
    os.mkdir(template_dir)
    for k, v in roleMap.items():
        role = v.split("/")[-1]  
        os.mkdir(f"templates/{role}")
        shutil.copy(f"assets/cover_letter.docx", f"templates/{role}/{FName}_{LName}_cover_letter.docx")
        with open(f"templates/{role}/{FName}_{LName}_resume.pdf", 'a'):
            pass
        with open(f"templates/{role}/{FName}_{LName}_resume.docx", 'a'):
            pass
        


    