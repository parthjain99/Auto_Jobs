import os
from config import (roleMap, FName, LName, parent_dir, rolePath, template_dir)

if __name__ == "__main__":
    os.mkdir(parent_dir)
    os.mkdir(template_dir)
    for k,v in roleMap.items():  
        x = v.split("/")[-1]  
        os.mkdir(f"templates/{x}")
        with open(f"templates/{x}/{FName}_{LName}_cover_letter.docx", 'a'):
            pass
        with open(f"templates/{x}/{FName}_{LName}_resume.pdf", 'a'):
            pass
        with open(f"templates/{x}/{FName}_{LName}_resume.pages", 'a'):
            pass


    