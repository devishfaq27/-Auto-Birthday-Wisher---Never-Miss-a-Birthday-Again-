import smtplib
from datetime import datetime
import pandas
import random

MY_GMAIL = "dsfhasj@gmail.com"
MY_PASSWORD = "fdgshdjasfk23"


today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as latter_file:
        content = latter_file.read()
        message = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birth Day\n\n{message}")

