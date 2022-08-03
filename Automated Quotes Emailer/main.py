import smtplib
import datetime as dt
import random

My_Email = "your@email.com"
My_Password = "Y0urP@$$w0rd"

now = dt.datetime.now()
weekday = now.weekday()
# Sending Quotes on Monday only change weekday==0 to weekday==1 for tuesday 2 for wednesday and so on
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(My_Email, My_Password)
            connection.sendmail(
                from_addr=My_Email,
                to_addrs=My_Email,
                msg=f"Subject:Todays Motivation Demo\n\n{quote}"
            )