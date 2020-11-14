from random import randint
from random import choice

passwordVault = {'James': 'ix799225ot'} #todo: store this file

class User:
    def __init__(self, name, password, age):
        self.id = self
        self.name = name
        self.password = password
        self.age = age

    def verifyLogin(self):
        pass

    def changePassword(self):
        id = self.name
        passwordVault[id] = self. password
        print(self.name)
        print(passwordVault[id])
        print(passwordVault)



class Password:
    def __init__(self, owner, lengthOfPassword, passwordStrength, password):
        self.owner = owner
        self.lengthOfPassword = lengthOfPassword
        self.passwordStrength = passwordStrength
        self.password = password


    def updatePassword(self, owner):
        id = owner
        newPassword = generatePassword(True) #be careful on duplicate names
        passwordVault[id] = newPassword
        print(passwordVault)
        with open('passwordVault.txt', 'w+') as f:
            print(passwordVault, file=f)



def generatePassword(x):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = len(alpha)

    if bool(x) == True:

        for i in range(length):
            wordOne = choice(alpha) + choice(alpha)
            wordTwo = choice(alpha) + choice(alpha)
            password = randint(100000, 999999)
            newPassword = (wordOne+str(password)+wordTwo)
            return newPassword
        else:
            pass

#newPassword = generatePassword(True)
#print(newPassword)

with open('passwordVault.txt', 'w+') as f:
    print(passwordVault, file=f)
#passwordOne = Password('Jody',11,'strong','121344')
#passwordOne.updatePassword('Jody')

Jodygamer111 = User('Jody', '1234566', 18)
Jodygamer111.changePassword()


