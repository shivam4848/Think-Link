from flask_mail import Mail, Message

from app.main import create_app

app = create_app()


def sendEmail(subject, prepared_message, sender, recipients):
    mail = Mail(app)
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = prepared_message
    mail.send(msg)
    return True
