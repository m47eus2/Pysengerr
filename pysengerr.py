import os
from datetime import datetime

def textMod(text, r, g, b, bold):
    style = '\033[1m' if bold else ''
    return f"{style}\033[38;2;{r};{g};{b}m{text}\033[0m"

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
        self.databasePath = '/home/raspberrypi/.pysengerrDatabase.txt'
        #self.databasePath = 'pysengerrDatabase.txt' #For testing
        self.running = True
        self.start()

    def start(self):
        os.system('clear')
        print(self.logo)
        self.username = input("Podaj nazwę użytkownika: ")
        self.run()

    def printMessages(self):
        file = open(self.databasePath, mode='r')
        data = file.read()
        print(data)
        file.close()

    def addMessage(self, message):
        now = datetime.now()
        now_formated = now.strftime("%d.%m.%Y-%H:%M")
        file = open(self.databasePath, mode='a')
        wrappedMessage = f"{textMod(self.username,28,220,154,1)}{textMod("@"+now_formated,28,220,154,0)}:{textMod('~ $ ',61,173,232,1)}{message}\n"
        file.write(wrappedMessage)
        file.close()

    def run(self):
        while self.running==True:
            os.system('clear')
            self.printMessages()
            print()
            message = input(textMod('Napisz wiadomość: ',197,134,192,1))
            if(message == ':q'):
                self.running=False
                break
            self.addMessage(message)


app = App()