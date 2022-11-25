"""
    This is a Object Oriented Program to send OTP to the given email id using python smtplib

    Author: umairkarel
"""
import random
import smtplib
from re import fullmatch
from os import environ as env
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class OTPSender:
    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

    def sendMail(self, receiver):
        msg = '\n\nThe One Time Password(OTP) is: ' + self.OTP
        self.smtp.sendmail(self.email, receiver, msg)

    def initiateSMTP(self):
        self.smtp.starttls()
        self.smtp.login(self.email, self.passwd)

    def quitSMTP(self):
        self.smtp.quit()

    def generateOTP(self, length):
        digits = "0123456789"
        otp = random.sample(digits, length)
        self.OTP = "".join(otp)

    def isValidOTP(self, otp):
        return self.OTP == otp



if __name__ == "__main__":
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    EMAIL = env.get('EMAIL')
    EMAIL_PASSWD = env.get('PASSWORD')
    LENGTH = int(env.get("OTP_LENGTH"))

    otpSender = OTPSender(EMAIL, EMAIL_PASSWD)


    # Taking Input
    print("Please Enter your Email to receive OTP")
    receiver_email = input("Email: ")

    while fullmatch(regex, receiver_email) == None:
        print("Please enter a valid email address")
        receiver_email = input("Email: ")


    otpSender.generateOTP(LENGTH)
    otpSender.initiateSMTP()
    otpSender.sendMail(receiver_email)


    print()
    print("OTP is sent to the given email address")
    print()
    print("Please enter the OTP to proceed")
    otp = input("OTP: ")

    if otpSender.isValidOTP(otp):
        print("Given OTP was correct")
    else:
        print("Given OTP was incorrect")


    otpSender.quitSMTP()
