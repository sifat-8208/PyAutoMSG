from time import sleep
from pyautogui import typewrite, press

def get_message():
    return input("Type your message--> ")

def get_number_of_messages():
    while True:
        try:
            return int(input("How many messages do you want to send--> "))
        except ValueError:
            print("ERROR: Please input a valid number!")

def send_messages(msg, num):
    sleep(6)
    for i in range(num):
        typewrite(msg)
        sleep(0.2)
        press("enter")

def main():
    msg = get_message()
    num = get_number_of_messages()
    send_messages(msg, num)

if __name__ == "__main__":
    main()
