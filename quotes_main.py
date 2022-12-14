"""
Problem Statement 1 :
- How do you send an email using Python code?
- Which method is used for sending an email in Python?
- Write a final program to sending a quotes randomly on every `Monday`.
- Import suitable libraries/module as project requirement
"""

# Please refer README.md file for  steps by step solution of this project.

import smtplib
from datetime import datetime
import random


my_email = "<youremail@gmail.com>"
my_password = "jdrpcofruavgyswd"
time_now = datetime.now()
weekday = time_now.weekday()

if weekday == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        send_quote = random.choice(all_quotes)

    print(send_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="<senderemail@mail.com>",
                            msg=f"Subject: Monday Motivation \n\n{send_quote}"
                            )