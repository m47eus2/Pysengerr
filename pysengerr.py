import os
from datetime import datetime
from settings import logo
from settings import textMod


class App():
    def __init__(self):
        self.logo = logo
        #self.databasePath = '/home/raspberrypi/.pysengerrDatabase.txt'
        #self.usersPath = 'home/raspberrypi/.pysengerrUsers.txt'
        self.databasePath = 'pysengerrDatabase.txt' #For testing
        self.usersPath = 'pysengerrUsers.txt' #For testing
        self.running = True
        self.exit = True
        self.logining()

    def logining(self):
        while self.exit==True:
            os.system('clear')
            print(textMod(self.logo,28,220,154,1)+'\n')

            print('1. Zaloguj się')
            print('2. Utwórz konto')
            print('3. Wyjdź z pysenderr')
            a=input()

            if a=='1':
                try:
                    with open("pysengerrUsers.txt", "r") as f:
                        dane = f.readlines()
                    self.user = User(dane[0].strip(), dane[1].strip())
                    os.system('clear')
                    print(textMod(self.logo,28,220,154,1)+'\n')
                    login=input('Podaj nik: ')

                    if login==self.user.login:
                        haslo=input('Podaj haslo: ')

                        if haslo==self.user.password:
                            self.name=login
                            self.exit = False
                            self.start()
                        else:
                            print('Niepoprawne haslo!')
                            input()
                    else:
                        print('Nie ma takiego konta!')
                        input()
                except FileNotFoundError:
                    os.system('clear')
                    print(textMod(self.logo,28,220,154,1)+'\n')
                    print('Nie ma jeszcze żadnego konta na pysengerr! Stwórz jakieś!')
                    input()

            if a=='2':
                os.system('clear')
                print(textMod(self.logo,28,220,154,1)+'\n')
                login=input('Jaki chcesz miec nik: ')
                password=input('Jakie chcesz mieć haslo: ')
                self.user = User(login, password)
                with open("pysengerrUsers.txt", "w") as f:
                    f.write(self.user.login + "\n")
                    f.write(self.user.password)
            
            if a=='3':
                os.system('clear')
                print(textMod(self.logo,28,220,154,1)+'\n')
                print('Na pewno?')
                a=input(f"[{textMod('y', 255, 0, 0, 1)},{textMod('N', 0, 255, 0, 1)}]: ")

                if a=='y':
                    self.exit=False


    def start(self):

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
        self.exit=False

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

class User():
    def __init__(self, a, b):
        self.login = a
        self.password = b

app = App()