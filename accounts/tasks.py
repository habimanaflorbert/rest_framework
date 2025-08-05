import time
from django.utils import timezone
from celery import shared_task

from home.utils import send_html_email

@shared_task
def send_welcome_email(email):
    time.sleep(5)  # simulate delay
    print(f"Email sent to {email}")
    return f"Welcome email sent to {email}"

@shared_task
def send_welcome_email_task(fname,lname,email):
    context = {
    'first_name':fname,
    'last_name': lname,
    'current_year': timezone.now().year,  # or datetime.now().year
    }
    send_html_email(
        subject="Welcome to Our Platform!",
        to_email=email,
        template_name='emails/welcome_email.html',
        context=context
    )


