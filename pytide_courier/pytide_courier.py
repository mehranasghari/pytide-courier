import click
from dotenv import load_dotenv
import os
from mail import send_mail

load_dotenv()
EMAIL_USER = os.getenv('EMAIL_USER')
DEFAULT_SUBJECT = os.getenv('DEFAULT_SUBJECT')
DEFAULT_MESSAGE = os.getenv('DEFAULT_MESSAGE')

@click.group(context_settings=dict(max_content_width=120))
def pytide_courier():
    """ A cli tool for sending emails"""
    pass

@pytide_courier.command
@click.argument('email_address', metavar='<email_address>')
@click.argument('subject', metavar='<subject>')
@click.argument('message', metavar='<message>')
def send_email(email_address, subject, message):
    """
    Send an email\n
    <address> is the recipient's email address.\n
    <subject> is the subject of the email.\n
    <message> is the body of the email\n
    Example:\n
    \tpython pytide_courier send-email example@example.com "subject" "message"
    """
    send_mail(email_address, subject, message)

if __name__ == '__main__':
    pytide_courier()
