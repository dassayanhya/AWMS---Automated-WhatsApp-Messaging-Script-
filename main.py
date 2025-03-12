import pandas as pd
import pywhatkit as kit
import time

# Load contacts from CSV file
contacts = pd.read_csv("contacts.csv")

# Message to send
message = """Hello {name}, this is a test WhatsApp message!
Script Powedered by : Vectorize Studios 
 
"""

# Loop through contacts and send messages
for index, row in contacts.iterrows():
    phone_number = row['Phone']
    name = row['Name']

    # Format message
    personalized_msg = message.format(name=name)

    try:
        # Send message (opens WhatsApp Web and sends automatically)
        kit.sendwhatmsg_instantly(phone_number, personalized_msg, wait_time=10, tab_close=False)
        print(f"Message sent to {name} ({phone_number})")

        # Wait to avoid spam detection
        time.sleep(5)
    except Exception as e:
        print(f"Failed to send message to {name}: {e}")
