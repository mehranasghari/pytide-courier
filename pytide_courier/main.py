from pytide_courier.mail import send_mail
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    EMAIL_USER = os.getenv('EMAIL_USER')
    DEFAULT_SUBJECT = os.getenv('DEFAULT_SUBJECT')
    DEFAULT_MESSAGE = os.getenv('DEFAULT_MESSAGE')
    send_mail(EMAIL_USER, DEFAULT_SUBJECT, DEFAULT_MESSAGE)

if __name__ == '__main__':
    main()