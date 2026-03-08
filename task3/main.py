import auditor.auditor as ad
from datetime import datetime

def generate_report(folder):
    date=ad.scan_directory(folder)
    report_name="audit_report"+datetime.now().strftime("%Y%m%d_%H%M%S")+".txt"
    with open(report_name,"w") as file:
        file.write("Project Audit Report\n")
        file.write("====================\n\n")
        
        for item in date:
            line=f"Name:{item['name']},Size:{item['size']}Bytes,Type:{item['type']},Modified:{item['modified']},Status:{item['status']}\n"
            file.write(line)
    print("report generated",report_name)
if __name__=="__main__":
    folder_path="test_folder"
    generate_report(folder_path) 
    
