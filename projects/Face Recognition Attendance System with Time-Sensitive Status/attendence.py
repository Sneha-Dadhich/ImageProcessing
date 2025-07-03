#############################################################
####################### backend #############################

from datetime import datetime

def add_data(row):
    # Open the file in append mode ('a') – this creates the file if it doesn't exist
    with open("attendance_log.txt", "a") as file:
        # Append data to the file
        file.write(f"{row}\n")


def check_attendance():
    # Get the current date and time
    current_datetime = datetime.now()
    # Extract the time part
    current_time = current_datetime.time()

    # Print the current time
    print(f"current_datetime :  {current_datetime}")
    print(f"Current time: {current_time}")

    # Alternatively, you can format the time as a string
    formatted_time = current_datetime.strftime("%H:%M:%S")
    print(f"Current time (formatted): {formatted_time}")

    print(f"formatted_time[:2] : {formatted_time[:2]}")
    hour = int(formatted_time[:2])
    minute = int(formatted_time[3:5])

    # if the person comes between 14:00 p.m and 14:30 p.m. , 
    # the person is present. If the person logins after 14:30 
    # p.m. but before 16:00 p.m. then the perso is simply late
    # Atlast if the login is done after 16:00 p.m. or simple 
    # not login the person is absent.

    current_time = hour * 60 + minute
    start_time = 14 * 60       # 14:00 → 840
    present_limit = 14 * 60 + 30  # 14:30 → 870
    late_limit = 15 * 60 + 5      # 16:00 → 960

    status = "Absent"
    if start_time <= current_time < present_limit:
        status = "Prsent"
        print(f"{'.' * 5} Present {'.' * 5}")
    elif present_limit <= current_time < late_limit:
        status = "Late"
        print(f"{'.' * 5} Late {'.' * 5}")
    else:
        print(f"{'.' * 5} Absent {'.' * 5}")
    
    login_time = formatted_time
    return login_time, current_datetime.date(), status  

import csv
import pandas as pd

def add_data(id, row, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
    
    registration_data = pd.read_csv(r"DRDO\codes\Face Recognition Attendance System with Time-Sensitive Status\user_registration.csv")
    attendance_log_data = pd.read_csv(filename)

    print(f"Registration Data  : \n{registration_data}")
    print(f"\n\nAttendance Data : \n{attendance_log_data}")

    # Count number of days the user was Present (based on unique dates)
    attended_days = attendance_log_data.loc[
        (attendance_log_data["Id"] == id) & (attendance_log_data["status"] == "Present")
        ].nunique()
    
    print(f"Attended Days : {attended_days}")

    partial_attended = attendance_log_data.loc[
        (attendance_log_data["Id"] == id) & (attendance_log_data["status"] == "Late") 
        ]["login_date"].nunique()
    
    paid_holidays_day = 5
    if partial_attended < paid_holidays_day:
        attended_days += partial_attended

    # Assign to registration_data
    # if id in registration_data['ID'].values:
    registration_data.loc[registration_data['ID'] == str(id), 'Attended_days'] = attended_days
    print(f"Attended Date : { registration_data.loc[registration_data['ID'] == id]['Attended_days'].values }")
    # else:
    print(f"id : {type(id)}")
    print(f"ID {id} not found in registration data.")
    print(f"Attended Date : { registration_data.loc[registration_data['ID'] == id]['Attended_days'] }")

    registration_file = r"DRDO\codes\Face Recognition Attendance System with Time-Sensitive Status\user_registration.csv"
    attendance_log_data_file = r"DRDO\codes\Face Recognition Attendance System with Time-Sensitive Status\Attendence_log.csv"

    attendance_log_data.to_csv(attendance_log_data_file, index=False, columns=["Id","name","login_date","login_time","status"])
    registration_data.to_csv(registration_file, index=False, columns=["ID","Name","Attended_days","Total_login"])

    attendance_log_data = pd.read_csv( attendance_log_data_file ) 
    registration_data = pd.read_csv( registration_file )

    print(f"{'.' * 5} After Editing {'.' * 5}")
    print(f"Registration Data  : \n{registration_data}")
    print(f"\n\nAttendance Data : \n{attendance_log_data}")

add_data("1" ,["1", "Sneha", "14:49:45", "2025-07-01", "Present"],r"DRDO\codes\Face Recognition Attendance System with Time-Sensitive Status\Attendence_log.csv")