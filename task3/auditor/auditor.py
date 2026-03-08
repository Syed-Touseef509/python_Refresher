import os
from datetime import datetime,timedelta

def scan_directory(folder_path):
    file_data=[]
    current_time=datetime.now()
    for filename in os.listdir(folder_path):
        full_path=os.path.join(folder_path,filename)
        if os.path.isfile(full_path):
            size=os.path.getsize(full_path)
            modified_timestamp=os.path.getmtime(full_path)
            modified_date=datetime.fromtimestamp(modified_timestamp)
            file_type=filename.split(".")[-1]
            days_old=(current_time-modified_date).days
            
            if days_old>= 30:
                status="OLD"
            else:
                status="OK"
            file_data.append({
                "name": filename,
                "size":size,
                "type":file_type,
                "modified":modified_date,
                "status":status
            })
    return file_data