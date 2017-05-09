import requests
from flask import current_app as app
from config import key


def send_simple_message():
    return requests.post(
        app.config['SEND_EMAIL_URL'],
        auth=("api", key.email_key),
        data={"from": app.config['SEND_EMAIL_FROM'],
              "to": ["test@somemail.com"],
              "subject": "Welcome",
              "text": "Testing some Mailgun awesomness!"})


def send(email, subject, body):
    return requests.post(
        app.config['SEND_EMAIL_URL'],
        auth=("api", key.email_key),
        data={"from": app.config['SEND_EMAIL_FROM'],
              "to": [email],
              "subject": subject,
              "text": body})
