import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

class EmailDriver():
  def __init__(self):
    currentEnv = os.getenv('RUNNING_ENVIRONMENT')

    if currentEnv != 'production':
      self.email = os.getenv("EMAIL_SENDER")
      self.password = os.getenv("EMAIL_PASSWORD")
    pass

  def basicSend(self, to, subject, text):
    msg = MIMEMultipart()
    msg['From'] = self.email
    msg['To'] = to
    msg['Subject'] = subject
    html_body = f"""
    <html>
    <body>
      <div>{text}</div>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_body, 'html'))
    try:
      with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server:
        server.starttls()
        server.login(self.email, self.password) 
        server.sendmail(self.email, to, msg.as_string())
        print("HTML email sent successfully!")
    except smtplib.SMTPException as e:
      print(f"Error: {e}")
    except Exception as e:
      print(f"Unexpected Error: {e}")