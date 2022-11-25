"""
    This is a simple program to send OTP to the given email id using python smtplib

    Author: umairkarel
"""
from dotenv import load_dotenv, find_dotenv
from os import environ as env
import random
from re import fullmatch
import smtplib
load_dotenv(find_dotenv())


# Create a file named ".env" in the sample floder where this file is stored and save the keys as below
# EMAIL=your_email
# PASSWORD=email_password (app password)

SENDER_EMAIL = env.get('EMAIL')
SENDER_EMAIL_PASSWD = env.get('PASSWORD')
OTP_LENGTH = 4

# regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'



def sendMail(msg, receiver):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(SENDER_EMAIL, SENDER_EMAIL_PASSWD)
    s.sendmail(SENDER_EMAIL, receiver, msg)
    s.quit()


def generateOTP(length):
    digits = "0123456789"
    otp = random.sample(digits, length)

    return "".join(otp)


def validateEmail(email):
    return fullmatch(regex, email) != None


def getInput():
    print("Please Enter your Email to receive OTP")
    email = input("Email: ")

    while not validateEmail(email):
        print("Please enter a valid email address")
        email = input("Email: ")

    return email


def validateOTP(org_otp):
    print()
    print("OTP is sent to the given email address")
    print()
    print("Please enter the OTP to proceed")
    otp = input("OTP: ")

    if otp.strip() == org_otp:
        print("Given OTP was correct")
    else:
        print("Given OTP was incorrect")


receiver = getInput()
OTP = generateOTP(OTP_LENGTH)

msg = '\n\nThe One Time Password(OTP) is: ' + str(OTP)

sendMail(msg, receiver)
validateOTP(OTP)

