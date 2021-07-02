from src.mongo import get_session_details, get_present_people_with_session_id, get_absent_people_with_session_id
from src.mongo import get_present_faculty_with_session_id, get_absent_faculty_with_session_id
import yagmail
import os

# Gmail SMPT Connection Settings
username = 'rpi.server.rfid@gmail.com'
password = 'nrjlrvfmyhxuitod'
server = 'smtp.gmail.com'

# Establishing Connection with SMTP Server
yag = yagmail.SMTP(user=username, password=password, host=server)


def build_email_report_data():
    res = get_session_details()
    res['STUDENTS_PRESENT'] = get_present_people_with_session_id()
    res['STUDENTS_ABSENT'] = get_absent_people_with_session_id()
    res['FACULTY_PRESENT'] = get_present_faculty_with_session_id()
    res['FACULTY_ABSENT'] = get_absent_faculty_with_session_id()

    return res


def send_email_report():
    data = build_email_report_data()
    send_to = "somanath.kommareddi@gmail.com"
    email_subject = "Dt:{} RFID Attendace Report".format(data['SESSION_START_AT'].strftime("%d-%b-%Y"))
    body = ["RFID Attendance Report",
            "\n",
            "Session Details",
            " > Session ID: {}".format(data['SESSION_ID']),
            " > Date: {}".format(data['SESSION_START_AT'].strftime("%d-%b-%Y")),
            " > Start time: {}".format(data['SESSION_START_AT'].strftime("%I:%M %p")),
            " > End Time: {}".format(data['SESSION_END_AT'].strftime("%I:%M %p")),
            "\n",
            "ID's of Attended Students"
            ] + [" > {}".format(i) for i in data['STUDENTS_PRESENT']] + [
            "\n",
            "ID's of Absentees Students"
            ] + [" > {}".format(i) for i in data['STUDENTS_ABSENT']] + [
            "\n",
            "ID's of Attended Faculty"
            ] + [" > {}".format(i) for i in data['FACULTY_PRESENT']] + [
            "\n",
            "ID's of Absentees Faculty"
            ] + [" > {}".format(i) for i in data['FACULTY_ABSENT']]
    yag.send(subject=email_subject, contents=body)
