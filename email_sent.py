from email import message
from email.message import EmailMessage
import smtplib

def email_send(senders_email,password1,msg_sub,msgcontent,contact_list):
    senderemail = str(senders_email)

    password = password1

    contacts = list(contact_list)

    msg_body = str(msgcontent)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(senderemail, password)

        for i in range(0, len(contacts)):
            msg = EmailMessage()
            msg['Subject'] =str(msg_sub)
            msg['From'] = senderemail
            msg['To'] = contacts[i]
            msg.set_content(msg_body)
            smtp.send_message(msg)
            print(f"done for {contacts[i]}")