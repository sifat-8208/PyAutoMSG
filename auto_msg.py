from time import sleep
from pyautogui import typewrite, press

class AutoMessageSender:
    def __init__(self):
        self.message = ""
        self.num_messages = 0

    def get_message_for_send_split(self):
        self.message = input("Type your message--> ").split()

    def send_message_split(self):
        self.get_message_for_send_split()
        sleep(5)
        for word in self.message:
            typewrite(word)
            sleep(0.2)
            press("enter")

    def get_message(self):
        self.message = input("Type your message--> ")

    def get_number_of_messages(self):
        while True:
            try:
                self.num_messages = int(input("How many messages do you want to send--> "))
                break
            except ValueError:
                print("ERROR: Please input a valid number!")

    def send_messages(self):
        sleep(6)
        for _ in range(self.num_messages):
            typewrite(self.message)
            sleep(0.2)
            press("enter")

    def user_choose(self):
        while True:
            try:
                choice = int(input("What do you want?\n===================\n1. Send and repeat a message.\n2. Send a long message word by word\n-->"))
                if choice in [1, 2]:
                    return choice
                else:
                    print("ERROR: Please enter 1 or 2!")
            except ValueError:
                print("ERROR: Please enter a valid number!")

    def run(self):
        choice = self.user_choose()
        if choice == 1:
            self.get_message()
            self.get_number_of_messages()
            self.send_messages()
        else:
            self.send_message_split()

if __name__ == "__main__":
    auto_msg_sender = AutoMessageSender()
    auto_msg_sender.run()
