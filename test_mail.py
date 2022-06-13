import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = "Mehed Alex"
email['to'] = "alex.mehedinteanu.95@gmail.com"
email['subject'] = "you won $1000000 "

email.set_content("sjfkbgkberibfebjhebfebfejbfejbgebgrjbg")
with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test.qwerty440@gmail.com", "p0o9i8u7y!")
    smtp.send_message(email)

print('email sent successfully')
    
