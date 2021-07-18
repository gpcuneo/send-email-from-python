import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

smtpServer = 'smtp.server.com'
port = 25
login = 'smtpUser'
password = 'smtpPassword'

imgEncode = base64.b64encode(open("imageToSend.jpg", "rb").read()).decode()

msg = MIMEMultipart("alternative")
msg['From'] = "from@example.com"
msg['To'] = "addressee@example.com"
msg['Subject'] = "Send test email"

bodyText = "here declarate one alternative text in case of the client not renderize html format"

bodyHtml = f"""\
<html>
  <body>
    <h1> Title </h1>
    <p> Texto to send in body <p>
    <img src="data:image/jpg;base64,{imgEncode}">
  </body>
</html> """

part1 = MIMEText(bodyText, "plain") 
part2 = MIMEText(bodyHtml, "html") 
msg.attach(part1) 
msg.attach(part2)

# if you smtp server use SSL use smtplib.SMTP_SSL
with smtplib.SMTP(smtpServer, port) as server: 
    server.login(login, password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
