from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_html_email(subject, to_email, template_name, context):
    html_message = render_to_string(template_name, context)
    email = EmailMessage(
        subject=subject,
        body=html_message,
        to=[to_email],
    )
    email.content_subtype = 'html'  # Set the email type to HTML
    email.send()