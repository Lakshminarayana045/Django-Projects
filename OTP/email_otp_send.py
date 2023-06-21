import smtplib
import ssl
import random


# start setup port number and server name

smtp_port = 587                     # standard secure SMTP port
smtp_server = "smtp.gmail.com"      # Google SMTP Server

# end setup port number and server name



# Sending mail
email_form = 'ukirankumar617@gmail.com'
# sending mail password
password = "abenvrcqaxomjkqn"


# receiver mail
email_to = 'amrutakulkarni2698@gmail.com'

# otp in random number
otp = ''.join([str(random.randint(0, 9)) for i in range(6)])


# content of message
message = " Your login OTP is  "+ otp


simple_email_context = ssl.create_default_context()
try:
    #print("connecting to server...")

    # smtp server
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)

    # server login
    TIE_server.login(email_form, password)

    #print("Connected to server :-)")

    print()
    print(f"Sending email to -{email_to}")
    TIE_server.sendmail(email_form, email_to, message)
    print(f"Email successfully sent to -{email_to}")

except Exception as e:
    print(e)

finally:
    TIE_server.quit()
