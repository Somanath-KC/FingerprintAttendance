from pymongo import MongoClient
from random import randint
from datetime import datetime
import os

# MongoDB Connection
client = MongoClient("mongodb://pythonclient:password@localhost:27017/")
db = client['attendance']

# MongoDB Collections
Students = db['Students']
Faculty = db['Faculty']
Biometrics = db['Biometrics']
AttendanceLog = db['AttendanceLog']
AttendanceSessions = db['AttendanceSessions']


def add_student(s_id, name, year, branch, section):
    try:
        Students.insert_one({"_id": s_id, 
                         "NAME": name,
                         "YEAR": year,
                         "BRANCH": branch,
                         "SECTION": section})
        return True
    except Exception as e:
        print(e)
        return False


def add_faculty(f_id, name, branch):
    try:
        Faculty.insert_one({"_id": f_id, 
                         "NAME": name,
                         "BRANCH": branch
                         })
        return True
    except Exception as e:
        print(e)
        return False


def add_biometric(role, id, card_num, bio1, bio2):
    Biometrics.insert_one({"_id": id,
                           "card_num": card_num,
                           "role": role,
                           "bio1": bio1,
                           "bio2": bio2})

def delete_biometric(id):
    return Biometrics.delete_one({"_id": id}).acknowledged


def check_if_student_exists(s_id):
    data = Students.find_one({"_id": s_id})
    return bool(data)


def check_if_faculty_exists(s_id):
    data = Faculty.find_one({"_id": s_id})
    return bool(data)


def check_person_in_biometrics(p_id):
    data = Biometrics.find_one({"_id": p_id})
    return bool(data)


def check_if_card_exists(card_num):
    data = Biometrics.find_one({"card_num": card_num})
    return bool(data)


def set_session(s_id):
    AttendanceSessions.insert_one({'SESSION_ID': s_id, 'SESSION_START_AT': datetime.now()})


def set_session_end_time():
    AttendanceSessions.update_one({"SESSION_ID": os.environ['SESSION_ID']}, {"$set": {'SESSION_END_AT': datetime.now()}})


def generate_attendance_session_id():
    rand_num = ''.join(["{}".format(randint(0, 9)) for num in range(0, 12)])
    if AttendanceSessions.find_one({"SESSION_ID": rand_num}):
        return generate_attendance_session_id()
    else:
        return rand_num


def get_card_details(card_num):
    data = Biometrics.find_one({"card_num": card_num})
    return data


def log_attendance(card_num, id, role):
    try:
        AttendanceLog.insert_one({ 'CARD_NUMBER': card_num, 
                                   'ID': id, 
                                   'ROLE': role,
                                   'DATE_TIME': datetime.now(), 
                                   'SESSION_ID': os.environ['SESSION_ID']
                                 })
    except Exception as e:
        print("Exception ", e)


def get_session_details():
    res = AttendanceSessions.find_one({'SESSION_ID': os.environ['SESSION_ID']})
    return res


def get_present_people_with_session_id():
    res = [i for i in AttendanceLog.find({'SESSION_ID': os.environ['SESSION_ID'], "ROLE": "student"})]
    return [i['ID'] for i in res]


def get_absent_people_with_session_id():
    res1 = [i for i in AttendanceLog.find({'SESSION_ID': os.environ['SESSION_ID'], "ROLE": "student"})]
    res2  = [i for i in Students.find({})]
    
    res = set([i['_id'] for i in res2]) - set([i['ID'] for i in res1])
    
    if len(res) == 0:
        return ["ALL WERE PRESENT"]
    else:
        return res

def get_present_faculty_with_session_id():
    res = [i for i in AttendanceLog.find({'SESSION_ID': os.environ['SESSION_ID'], "ROLE": "faculty"})]
    return [i['ID'] for i in res]


def get_absent_faculty_with_session_id():
    res1 = [i for i in AttendanceLog.find({'SESSION_ID': os.environ['SESSION_ID'], "ROLE": "faculty"})]
    res2  = [i for i in Faculty.find({})]
    
    res = set([i['_id'] for i in res2]) - set([i['ID'] for i in res1])
    
    if len(res) == 0:
        return ["ALL WERE PRESENT"]
    else:
        return res