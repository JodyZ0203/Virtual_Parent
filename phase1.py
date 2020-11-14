from random import randint
from random import choice
import json
from portal import Checker


#portal()

#passwordVault = {'James': 'ix799225ot', 'Kobe': '82481lakers'} #todo: store this file



#with open('intents.json') as file:
   # data = json.load(file)

preMadeInformation = '''
{ 
    "users": [
      {
         "userId": "JL7",
         "name": "Json Liam",
         "age": 12,
         "password": "D~b237427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BB08",
         "name": "Boke Bryant",
         "age": 6,
         "password": "kobes824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll213",
         "name": "Levert Lewis",
         "age": 25,
         "password": "progamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "Tester1",
         "name": "Tester1",
         "age": 22,
         "birthday": [
            "0000",
            "00",
            "00"
         ],
         "password": "123456",
         "country": "Null"
      },
      {
         "userId": "king257",
         "name": "Lebron James",
         "age": 24,
         "birthday": [
            "2002",
            "03",
            "12"
         ],
         "password": "KingJames636",
         "country": "United States"
      },
      {
         "userId": "Jinl7",
         "name": "Jeremy Lamb",
         "age": 19,
         "password": "D~b2374dsfdsf3427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BBB0308",
         "name": "Ball Lonzo",
         "age": 23,
         "password": "kball33824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll223213",
         "name": "Lance Lewis",
         "age": 25,
         "password": "progdfamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "JL7",
         "name": "Json Liam",
         "age": 18,
         "password": "D~b237427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BB08",
         "name": "Boke Bryant",
         "age": 16,
         "password": "kobes824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll213",
         "name": "Levert Lewis",
         "age": 15,
         "password": "progamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "Tester1",
         "name": "Tester1",
         "age": 20,
         "birthday": [
            "0000",
            "00",
            "00"
         ],
         "password": "123456",
         "country": "Null"
      },
      {
         "userId": "king257",
         "name": "Lebron James",
         "age": 24,
         "birthday": [
            "2002",
            "03",
            "12"
         ],
         "password": "KingJames636",
         "country": "United States"
      },
      {
         "userId": "Jinl7",
         "name": "Jeremy Lamb",
         "age": 13,
         "password": "D~b2374dsfdsf3427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BBB0308",
         "name": "Ball Lonzo",
         "age": 13,
         "password": "kball33824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll223213",
         "name": "Lance Lewis",
         "age": 35,
         "password": "progdfamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "JL7",
         "name": "Json Liam",
         "age": 47,
         "password": "D~b237427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BB08",
         "name": "Boke Bryant",
         "age": 6,
         "password": "kobes824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      },
      {
         "userId": "Ll213",
         "name": "Levert Lewis",
         "age": 11,
         "password": "progamer3232",
         "birthday": [
            "2005",
            "05",
            "06"
         ],
         "country": "Brazil"
      },
      {
         "userId": "Tester1",
         "name": "Tester1",
         "age": 10,
         "birthday": [
            "0000",
            "00",
            "00"
         ],
         "password": "123456",
         "country": "Null"
      },
      {
         "userId": "king257",
         "name": "Lebron James",
         "age": 21,
         "birthday": [
            "2002",
            "03",
            "12"
         ],
         "password": "KingJames636",
         "country": "United States"
      },
      {
         "userId": "Jinl7",
         "name": "Jeremy Lamb",
         "age": 19,
         "password": "D~b2374dsfdsf3427di&",
         "birthday": [
            "2005",
            "02",
            "02"
         ],
         "country": "Finland"
      },
      {
         "userId": "BBB0308",
         "name": "Ball Lonzo",
         "age": 20,
         "password": "kball33824",
         "birthday": [
            "2003",
            "03",
            "24"
         ],
         "country": "Canada"
      }
   ]
}

data = json.loads(preMadeInformation)
with open('basicInformation.json', 'w') as file:
    json.dump(data, file, indent=3)


'''


class User:
    '''
    the class that holds information about the user

    Attributes
    ----------
    name : str
        The name of the user
    password : str
        This is the user password
    age : int
        The age of the user

    Methods
    -------
    verifyLogin()
        Attempts to verify the password
    changePassword()
        Attempts to change a password
    '''

    def __init__(self, name, password, age):
        '''
        Constructor that initialize a user


        Parameters
        ----------
        name : str
            The name of the user
        password : str
            The password of the user
        age: int
            The age of the user

        '''
        self.id = self
        self.name = name
        self.password = password
        self.age = age

    def verifyLogin(self):
        '''
        This function checks to see if the password our user enters is correct or not

        It asks the user to enter the password and see if it matches with what we have in the database

        Parameters
        ----------
        none

        Returns
        -------
        bool
            True if the verification is successful
            False if the attempted failed

        Warnings
        --------
        If a incorrect name is entered, it will raise a key error.

        Raises
        ------
        KeyError
            If the input of the username is incorrect, and it can not be found in the dictionary
        NameError
            If the input is a name and not a string, so it is not defined
        TypeError
            There should not be any input, otherwise it will raise a type error.
        '''
        userName = input("name: ")
        passWord = input("password: ")
        checkName = passwordVault[userName]
        if checkName == passWord:
            print("Login Success")
            print('Loading...')
            return True
        else:
            print("False!!")
            return False

    def changePassword(self):
        '''
        This function allows you to change your password

        Parameters
        ----------

        Returns
        -------
        void

        Warnings
        --------
        If a incorrect option is choosed, a UnboundLocalError will surface.

        Raises
        ------
        TypeError
            There should not be any input, otherwise it will raise a type error.
        '''
        id = self.name
        option = input("Do you want me to generate a password for you? (yes/no): ")
        if option == 'yes':
            newPassword = generatePassword(True)

        elif option == 'no':
            newPassword = input("Enter your new password: ")

        passwordVault[id] = newPassword
        print('Your name is: '+ self.name)
        print('Your new password is: ' + passwordVault[id])
        print(passwordVault)




def generatePassword(x):
    '''
    This function generates a random password

    Parameters
    ------------
    x: bool

    Returns
    -------
    str
       The password generated using this function should be a string because it consists of numbers and characters.

    Warnings
    --------
    If will break if the input is not True.


    '''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = len(alpha)
    if bool(x):
        for i in range(length):
            wordOne = choice(alpha) + choice(alpha)
            wordTwo = choice(alpha) + choice(alpha)
            password = randint(100000, 999999)
            newPassword = (wordOne+str(password)+wordTwo)
            return newPassword
    else:
        pass


a = input(str('NMAE: '))
b = input(str('Password: '))
Jody111 = User(a, b, 18)

#Jody111.verifyLogin()
#print(generatePassword('str'))
#Jody111.changePassword()
'''
try:
    Jody111.changePassword(1234566)
except TypeError:
    print("Raised a TypeError as expected")

try:
    Jody111.verifyLogin('james')
    Jody111.verifyLogin(1)
except TypeError:
    print("Raised a TypeError as expected")
except NameError:
    print("Raised a NameError as expected")
except KeyError:
    print("Raised a KeyError as expected")
'''