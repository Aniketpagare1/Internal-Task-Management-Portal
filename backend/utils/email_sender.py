import smtplib
from email.mime.text import MIMEText
from config import Config

def send_task_email(to_email, task_title, deadline):
    msg = MIMEText(f"You have been assigned a new task: {task_title}.\nDeadline: {deadline}")
    msg['Subject'] = 'New Task Assigned'
    msg['From'] = Config.EMAIL_USER
    msg['To'] = to_email

    try:
        with smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(Config.EMAIL_USER, Config.EMAIL_PASS)
            smtp.send_message(msg)
    except Exception as e:
        print(f"Email error: {e}")
