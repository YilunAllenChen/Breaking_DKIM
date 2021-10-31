import smtplib
import ssl
import dotenv
import os

class Environment():
    """
    Class to handle environment variables
    """
    def __init__(self, env_file):
        dotenv.load_dotenv(env_file)
        self.smtp_server = os.environ.get('smtp_server')
        self.smtp_port = os.environ.get('smtp_port')
        self.sender = os.environ.get('sender_email') 
        self.password = os.environ.get('sender_password') 
        self.receiver = os.environ.get('receiver') 

    def send(self, msg, use_ssl=True):
        if not use_ssl:
            print("bypassing ssl")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.receiver, msg)
                return
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, msg)
