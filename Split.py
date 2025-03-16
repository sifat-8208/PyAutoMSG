from time import sleep
from pyautogui import typewrite, press

def get_message():
    msg = input("Type your message--> ").split()
    return msg

def send_message():
    msg = get_message()
    sleep(5)
    for i in msg:
        typewrite(i)
        sleep(.2)
        press("enter")

def main():
    return send_message()

if __name__ == "__main__":
    main()
