#!/usr/bin/python
from django.core.mail import send_mail, BadHeaderError
smtp = 'smtp.gmail.com'

password = 'nn'
company="digitalprizm.net"
email = 'nspna@gmai.com.'
country="india"
phone="7875"
name="mahesh"
EMAIL_HOST = smtp
EMAIL_HOST_PASSWORD = password
EMAIL_HOST_USER = email
EMAIL_PORT = 465
EMAIL_USE_SSL = True
message="sent mail"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
fullname =   "NAME:" + " " + name
fullemail = "\n " "NAME:" + " " + name + "\n " "EMAIL:" + " " + email + "\n " "Company:" + " " + company + " \n " "Country:" + " " + country + ""  "\n " "Phone:" + " " + phone + "" "\n " "Message:" + " " + message + ""
send_mail(fullname,fullemail,"maheangote1@gmail.com",["maheangote1@gmail.com"])