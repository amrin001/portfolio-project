from pathlib import Path

import pywhatkit as kit
import pandas as pd
import time

"""
Ensure you have downloaded the following libraries:

pywhatkit
pandas
openpyxl

if not, install using the following commands:
pip install pywhatkit
pip install pandas
pip install openpyxl
"""


def send_whatsapp_messages(file_path):
    """
    Sends WhatsApp messages to numbers and messages provided in an Excel file.

    Args:
        file_path (str): The path to the Excel file containing phone numbers and messages.
    """
    try:
        # Check if the file exists
        file_path = Path(file_path)
        if not file_path.is_file():
            print(f"Error: The file '{file_path}' does not exist. Please provide a valid file path.")
            return
        # Load the Excel file
        data = pd.read_excel(file_path)

        # Ensure the Excel file has 'Phone' and 'Message' columns
        if 'Phone' not in data.columns or 'Message' not in data.columns:
            print("Error: Excel file must have 'Phone' and 'Message' columns.")
            return

        for index, row in data.iterrows():
            phone = str(row['Phone'])  # Ensure phone number is a string
            message = row['Message']

            print(f"Sending {message} to {phone}...")

            # Send the message (scheduled 1 minute from now)
            # kit.sendwhatmsg(phone_no=f"+{phone}",
            #                 message=message,
            #                 time_hour=time.localtime().tm_hour,
            #                 time_min=(time.localtime().tm_min + 1) % 60,
            #                 wait_time=10,  # Specify wait_time explicitly
            #                 tab_close=True,  # Close the tab after sending
            #                 close_time=2
            #                 )

            kit.sendwhatmsg_instantly(phone_no=f"+{phone}",
                                      message=message,
                                      wait_time=5,
                                      tab_close=True,
                                      close_time=2)

            print(f"Message sent to {phone}")
            time.sleep(10)  # Delay to avoid overwhelming WhatsApp Web

    except Exception as e:
        print(f"An error occurred: {e}")


# Provide the path to your Excel file here
file_path = "../contacts.xlsx"
send_whatsapp_messages(file_path)
