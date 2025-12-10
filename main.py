import pandas as pd 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

sender = ''
appPassword = ''
newHire = pd.read_excel('./NewHireEmail.xlsx')
print(newHire)
#newHire = newHire.fillna("")
#newHire = newHire.astype(str)

for user, newHires in newHire.iterrows():
    msg = MIMEMultipart()
    msg['Subject'] = 'Login SAP'
    message = f"Hi {newHires['nome']}, \nthis is your SAP UserID and E-mail: \n {newHires['infos']}."
    msg['From'] = sender
    msg['To'] = newHires['email']
    msg.attach(MIMEText(message, 'plain'))


    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login(sender, appPassword)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()