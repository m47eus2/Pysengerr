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
        print(textMod(self.logo,28,220,154,1)+'\n')

        self.name=input('Podaj nazwę urzytkownika: ')

        os.system('clear')
        print(textMod(self.logo,28,220,154,1)+'\n')

        #Username color choose
        print('1. ', textMod(self.name, 255, 0, 0, 1))
        print('2. ', textMod(self.name, 255, 127, 0, 1))
        print('3. ', textMod(self.name, 255, 225, 0, 1))
        print('4. ', textMod(self.name, 0, 255, 0, 1))
        print('5. ', textMod(self.name, 0, 255, 255, 1))
        print('6. ', textMod(self.name, 0, 0, 255, 1))
        print('7. ', textMod(self.name, 127, 0, 255, 1))
        print('8. ', textMod(self.name, 255, 0, 255, 1))
        self.nickColor = input('Wybierz kolor swojego nicku: ')

        if self.nickColor=='1':
            self.r = 255
            self.g = 0
            self.b = 0
        if self.nickColor=='2':
            self.r = 255
            self.g = 127
            self.b = 0
        if self.nickColor=='3':
            self.r = 255
            self.g = 255
            self.b = 0
        if self.nickColor=='4':
            self.r = 0
            self.g = 255
            self.b = 0
        if self.nickColor=='5':
            self.r = 0
            self.g = 255
            self.b = 255
        if self.nickColor=='6':
            self.r = 0
            self.g = 0
            self.b = 255
        if self.nickColor=='7':
            self.r = 127
            self.g = 0
            self.b = 255
        if self.nickColor=='8':
            self.r = 255
            self.g = 0
            self.b = 255

        self.username = textMod(self.name, self.r, self.g, self.b, 1)

        self.run()

    def printMessages(self):
        file = open(self.databasePath, mode='r')
        data = file.read()
        print(data)
        file.close()

    def addMessage(self, message):
        now = datetime.now()
        now_formated = now.strftime("%d.%m.%Y-%H:%M")
        usernameMod = textMod(self.username,self.r,self.g,self.b,1)
        dateMod = textMod("@"+now_formated,28,220,154,0)
        endMod = textMod('~ $ ',61,173,232,1)
        file = open(self.databasePath, mode='a')
        wrappedMessage = f"{usernameMod}{dateMod}:{endMod}{message}\n"
        file.write(wrappedMessage)
        file.close()

    def run(self):
        while self.running==True:
            os.system('clear')
            self.printMessages()
            print()
            message = input(textMod('Napisz wiadomość: ',self.r,self.g,self.b,1))
            if(message == ':q'):
                self.running=False
                break
            self.addMessage(message)


app = App()