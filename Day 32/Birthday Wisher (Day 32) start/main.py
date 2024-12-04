import smtplib

my_email = "dejaj33209@jonespal.com"

connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()
connection.login(user=my_email)
connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com", msg="Hello")
connection.close()