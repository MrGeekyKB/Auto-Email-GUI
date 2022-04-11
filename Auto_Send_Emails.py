import smtplib
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP_Email = simpledialog.askstring(title="Emails",
                                  prompt="Enter Emails Seprated by ' , ':")


gmail_user = 'kbiotics@gmail.com'
gmail_password = 'krbharne'
reciver=USER_INP_Email
new_reciver= reciver.split(',')
sent_from = gmail_user
to = new_reciver
subject = 'Welcome to Python Email'
body = 'Hello We are Working Together using GUI Single mail also works & Multiple Emails'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
    messagebox.showinfo("Sent", "All Emails Sent Sucessfully...")
except Exception as ex:
    print ("Something went wrong….",ex)
