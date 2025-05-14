import os
from datetime import datetime

class App():
    def __init__(self):
        self.logo = r"""
 /$$$$$$$
| $$__  $$
| $$  \ $$ /$$   /$$  /$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$
| $$$$$$$/| $$  | $$ /$$_____/ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$____/ | $$  | $$|  $$$$$$ | $$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/| $$  \__/
| $$      | $$  | $$ \____  $$| $$_____/| $$  | $$| $$  | $$| $$_____/| $$      | $$
| $$      |  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      | $$
|__/       \____  $$|_______/  \_______/|__/  |__/ \____  $$ \_______/|__/      |__/
           /$$  | $$                               /$$  \ $$
          |  $$$$$$/                              |  $$$$$$/
           \______/                                \______/
        """
        self.running = True
        self.start()

    def start(self):
        os.system('clear')
        print("\033[38;5;45m"+self.logo+"\033[0m")
        self.username = input("Podaj nazwę użytkownika: ")
        self.run()

    def printMessages(self):
        file = open('/home/raspberrypi/.pysengerrDatabase.txt', mode='r')
        data = file.read()
        print(data)
        file.close

    def addMessage(self, message):
        now = datetime.now()
        now_formated = now.strftime("%d.%m.%Y-%H:%M")

        file = open('/home/raspberrypi/.pysengerrDatabase.txt', mode='a')
        file.write('\n')
        file.write("\033[38;5;40m"+self.username+'@'+now_formated+':~ $ '+"\033[0m"+message)
        file.close

    def run(self):
        while self.running==True:
            os.system('clear')
            self.printMessages()
            print()
            message = input('Napisz wiadomość: ')
            if(message == ':q'):
                self.running=False
                break
            self.addMessage(message)


app = App()