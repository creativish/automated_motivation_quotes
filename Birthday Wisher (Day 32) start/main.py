import datetime as dt
import smtplib
import random

My_email = "vs92717@gmail.com"
My_password = "Imlooser12@"
Frnd_email = "vish1010@gmail.com"

now = dt.datetime.now()
day = now.weekday()

#  for thursday motivation quote
if day == 3:
    with open("quotes.txt", "r") as quote:
        all_quotes = quote.readlines()
        quotes = random.choice(all_quotes)
        print(quotes)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(My_email, My_password)
connection.sendmail(from_addr=My_email, to_addrs=Frnd_email, msg=f"Subject: motivation\n\n {quotes}")

