import smtplib
import ssl

class EmailOutput:
    port = 465
    smtp_server = 'smtp.gmail.com'

    @staticmethod
    def email_output(info: str, sender_email: str, sender_password: str, receiver_email: str) -> None:

        message = f'''\
            Subject: Info about files with logs from Analysis log service.

            {info}'''

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(EmailOutput.smtp_server, EmailOutput.port, context=context) as server:
            try:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message)
                print('Message sent successfully!')
            except Exception as e:
                print('An error occurred:', str(e))
