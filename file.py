import smtplib

# Email Sender Details
Email_sender = 'sender@gmail.com'
App_password = '**** **** **** ****'

# Email Receiver Details
Email_receiver = 'receiver@gmail.com'

# Mail Details
subject = 'Testing Message Bruh'
body = 'Hello\n\n\nThis is Testing Message.'

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(Email_sender, App_password) # Login using details

    message = f"Subject : {subject}\n\n{body}"

    # Send Email
    server.sendmail(Email_sender, Email_receiver, message)
    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print(f"Error : {e}")
