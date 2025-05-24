import os
from datetime import datetime

from settings import logo, colors

def textMod(text, color, bold):
    style = '\033[1m' if bold else ''
    return f"{style}\033[38;2;{color[0]};{color[1]};{color[2]}m{text}\033[0m"

class App():
    def __init__(self):
        self.logo = logo
        self.databasePath = 'pysengerrDatabase.txt'
        self.running = True
        self.start()

    def start(self):
        os.system('clear')
        print(textMod(self.logo,colors['terminalGreen'],1)+'\n')
        self.username=input('Podaj nazwę urzytkownika: ')

        os.system('clear')
        print(textMod(self.logo,colors['terminalGreen'],1)+'\n')
        #Username color choose
        print('1. ', textMod(self.username, colors['red'],1))
        print('2. ', textMod(self.username, colors['orange'], 1))
        print('3. ', textMod(self.username, colors['yellow'], 1))
        print('4. ', textMod(self.username, colors['green'], 1))
        print('5. ', textMod(self.username, colors['skyblue'], 1))
        print('6. ', textMod(self.username, colors['blue'], 1))
        print('7. ', textMod(self.username, colors['violet'], 1))
        print('8. ', textMod(self.username, colors['pink'], 1))
        number = input('Wybierz kolor swojego nicku: ')
        if number=='1': self.nickColor = colors['red']
        elif number=='2': self.nickColor = colors['orange']
        elif number=='3': self.nickColor = colors['yellow']
        elif number=='4': self.nickColor = colors['green']
        elif number=='5': self.nickColor = colors['skyblue']
        elif number=='6': self.nickColor = colors['blue']
        elif number=='7': self.nickColor = colors['violet']
        elif number=='8': self.nickColor = colors['pink']

        self.run()

    def printMessages(self):
        file = open(self.databasePath, mode='r')
        data = file.read()
        print(data)
        file.close()

    def addMessage(self, message):
        now = datetime.now()
        now_formated = now.strftime("%d.%m.%Y-%H:%M")
        usernameMod = textMod(self.username,self.nickColor,1)
        dateMod = textMod("@"+now_formated,colors['terminalGreen'],0)
        endMod = textMod('~ $ ',colors['terminalBlue'],1)
        file = open(self.databasePath, mode='a')
        wrappedMessage = f"{usernameMod}{dateMod}:{endMod}{message}\n"
        file.write(wrappedMessage)
        file.close()

    def run(self):
        while self.running==True:
            os.system('clear')
            self.printMessages()
            print()
            message = input(textMod('Napisz wiadomość: ',self.nickColor,1))
            if(message == ':q'):
                self.running=False
                break
            self.addMessage(message)


app = App()