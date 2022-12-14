"""
Problem Statement 2 :
- How do you send an email using Python code?
- Which method is used for sending an email in Python?
- Write a final program to sending a Birthday wish Email to emails present in csv file.
- Import suitable libraries/module as project requirement.
- You can run this program live/free by https://www.pythonanywhere.com/
- PythonAnywhere: Host, run, and code Python in the cloud.
-  Use birthdays.csv and letter_templates and change as per your requirement.
"""
# Please refer README.md file for  steps by step solution of this project.

from datetime import datetime
import pandas
import random
import smtplib
MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "jdrpcofruavgyswd"
today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", f"{birthday_person['name']}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
