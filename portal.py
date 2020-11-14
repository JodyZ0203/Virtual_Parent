import json
import sys
from random import randint
from random import choice
from termcolor import colored
import matplotlib.pyplot as plt
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


'''
with open('basicInformation.json') as file:
    data = json.load(file)
    print(data)
infoSort = data['users']


#infoSort.sort(key=lambda age: age['age'])
#infoSort.sort(key=lambda name: name['name'])
print(infoSort)




def bubbleSort(unsortedList):
    length = len(unsortedList)
    while length > 0:
        length -= 1
        i = 0
        while i < length:
            if infoSort[i]['age'] > infoSort[i+1]['age']:
                infoSort[i], infoSort[i+1] = infoSort[i+1], infoSort[i]
                print(str(i) + " swapped with " + str(i + 1))
            #correctEntry += 1
            i += 1



#print(timeit.timeit('bubbleSort(unsortedList)', setup='from __main__ import bubbleSort, unsortedList', number=infoSort))


#bubbleSort(infoSort)

def selectionSort(unsortedList):
    length = len(unsortedList)
    counter = 0
    j = 0   #min
    i = 0   #current
    while counter < length:
    #length -= 1
    #counter = counter + 1
    #j = 0   #min
    #i = 0   #current
    #counter = 0
    #min1 = infoSort[counter]['age']
    #while i in range(0, length):
        for i in range(j+1, length):
    # If the other element is min than first element
            if infoSort[i]['age'] < infoSort[j]['age']:
                print("current item is " + str(i))
                print("current minimum is " + str(j))
                print("first item in the unsorted list is " + str(counter))
                j = i  # It will change
        infoSort[counter], infoSort[j] = infoSort[j], infoSort[counter]
        i += 1

        #counter += 1
        counter = counter + 1
        j = counter



#selectionSort(infoSort)
#print(infoSort)


def linearSearch(list, key):
    length = len(list)
    i = 0
    while i < length:
        if key == list[i]['age']:
            number = i
            print(str(key) + " is in index: " + str(i))
            return number
        i += 1


start_time = time.time()
linearSearch(infoSort, 22)
print("--- %s seconds ---" % (time.time() - start_time))
#linearSearch(infoSort, 22)


def binerySearch(sortedList, key):
    maxi = len(sortedList)
    mini = 0
    while mini < maxi:
        if (maxi + mini) % 2 == 0:
            i = int((maxi + mini) / 2)
            if infoSort[i]['age'] < key:
                mini = i
            elif infoSort[i]['age'] > key:
                maxi = i
            else:
                print(str(key) + " is in index: " + str(i))
                return i
                mini = maxi
        else:
            i = int((maxi + mini - 1) / 2)
            if infoSort[i]['age'] < key:
                mini = i
            elif infoSort[i]['age'] > key:
                maxi = i
            else:
                print(str(key) + " is in index: " + str(i))
                return i
                mini = maxi



#binerySearch(infoSort, 25)



if min == maxi and infoSort[i]['age'] == key:
    print(min)
else:
    print(-1)

'''

'''
#while correctEntry < 9:
for i in range(length):
    for n in range(i):
        if infoSort[n]['age'] > infoSort[n+1]['age']:
            infoSort[n], infoSort[n+1] = infoSort[n+1], infoSort[i]
            #correctEntry += 1
            #print(i)

    i += 1
'''
'''
print(a)
while correctEntry < 170000:
    for i in range(0, length):
        for j in range(i):
            #print(a[j+1])
            if a[j] > a[j+1]:
               a[j], a[j+1] = a[j+1], a[j]
            correctEntry += 1
            #print(i)

    i += 1
'''
# first create a list that stores the index number and age, and then file those first, and then try to change the actual file
#print(infoSort)
#print(a)
'''
while i < length:
    if loginName == infoSort[i]['age']:
        print("True, username is valid")
        number = i
        print('This user is in ' + str(number))
        return number
        break
    i += 1
'''

def portal():
    '''
    This is a login portal for existing users and new users


    Warnings
    --------
    This program will break if input is odd

    Raises (this section is only applicable if your function raises an exception)
    ------
    ValueError
        Input is not yes or no
    TypeError
        Function does not take in any value
    '''
    answer = input("Is this your first time using Virtual Parent?(yes/no): ")
    if answer == 'no':
        id1 = input("What is your user id: ")
        password1 = input("Enter your password: ")
        user1 = Checker(password1, id1)
        location = user1.idCheck()
        user1.passwordVerify(location)
        admin3 = Admin()
        admin3.statusCheck(location)

    if answer == 'yes':
        signUp()
    else:
        pass
try:
    print(portal('hi'))
except (TypeError) as e:
    print('Something went wrong: ' + str(e))

def signUp():
    '''
    This is a sign up function for new users

    Warnings
    --------
    This program will break if input is odd

    Raises
    ------
    TypeError
        Function does not take in any value
    '''
    myDict = dict({'userId': 'null', 'name': 'null', 'age': 0, 'birthday': [], 'password': 'null', 'country': 'null'})
    if bool:
        print('Please enter your basic information so your Virtual Parent can know more about you')
        userId = input("Enter a login name: ")
        name = input("What is your name?: ")
        age = int(input('How old are you?: '))
        print('When were you born?(year/month/day)?')
        print('For example, 2001/03/15')
        birthday = str(input('Enter your birthday: '))
        country = input("Which country are you currently living in?: ")
        urPassword = input('Type in a password: ')
        correctPassword = admin1.passwordCheck(urPassword)
        admin1.passwordStrength(correctPassword)

        myDict['userId'] = userId
        myDict['name'] = name
        myDict['age'] = age
        myDict['birthday'] = birthday.split('/')
        myDict['password'] = correctPassword
        myDict['country'] = country
        with open('basicInformation.json') as file:
            info = json.load(file)
            print(info)
            info["users"].append(myDict)
            print(info)
            info.update(info)
        with open('basicInformation.json', 'w+') as file:
            json.dump(info, file, indent=3)
            print(info)
            file.close()

try:
    print(signUp('hello'))
except (TypeError) as b:
    print('Something went wrong: ' + str(b))


class Checker:
    '''
    A checker that checks for password and username in the database

    Attributes
    ----------
    password : str
               The user's password
    username : str
               The  username of the user

    Methods
    -------
    idCheck() -> int
             Prints the location of the user information
    passwordVerify(number: int) -> None
             Prints if the password matches the user

    '''
    def __init__(self, password, username):
        '''
        Constructor to build a checker object


        Parameters
        ----------
        password : str
                 The password of the user
        username : str
                 The username of the user


        '''
        self.password = password
        self.username = username

    def idCheck(self):
        '''
        Checks the name of our user with the database to see if they match

        Returns
        -------
        int
            The position of the user in the list

        Raises
        ------
        TypeError
            This function does not take in any value

        '''
        loginName = self.username
        with open('basicInformation.json') as file:
            data = json.load(file)
            print(data)
        info_check = data['users']
        print(info_check)
        length = len(info_check)
        i = 0
        while i < length:
            if loginName == info_check[i]['userId']:
                print("True, username is valid")
                number = i
                print('This user is in ' + str(number))
                return number
                break
            i += 1
        else:
            sys.exit('Your username is not in our database')

    def passwordVerify(self, number):
        '''
        Verfies the password the user enters

        Parameters
        ----------
        number : int
               This is the input of position in order to find where the password is stored


        Raises
        ------
        TypeError
            If number is not an int
        IndexError
            If the number is out of range

        '''
        with open('basicInformation.json') as file:
            data = json.load(file)
        infoCheck = data['users']

        if not isinstance(number, int):
            raise TypeError('passwordVerify expecting the input as a number')
        if number > len(infoCheck):
            raise IndexError('List Index out of range')

        password_check = self.password

        if password_check == infoCheck[number]['password']:
            print('Access Granted')
            print('Welcome Back, ' + infoCheck[number]['name'])
            return True
        else:
            print('Wrong Password')
            return False

try:
    user2 = Checker('dsfsdfs', 'Jo')
    print(user2.passwordVerify(100))
    print(user2.passwordVerify('gfhf'))
    print(user2.idCheck('hi'))
except (TypeError, IndexError) as c:
    print('Something went wrong: ' + str(c))



class Password:
    '''
    A class that does everything about the password

    Attributes
    ----------
    none

    Methods
    -------
    changePassword() -> None
             Changes the password and updates it
    generatePassword() -> str
             Generates a new password for the user
    passwordStrength(password: str) -> int
             Checks the strength of the password and returns a score of security

    '''
    def __init__(self):
        '''
        Constructor to build a password object


        '''
        pass

    def changePassword(self):
        '''
        This function allows you to change your password

        Warnings
        --------
        If a incorrect option is choosed, a UnboundLocalError will surface

        Raises
        ------
        TypeError
            There should not be any input, otherwise it will raise a type error.
        '''
        option = input("Do you want me to generate a password for you? (yes/no): ")
        if option == 'yes':
            newPassword = self.generatePassword()

        elif option == 'no':
            newPassword = input("Enter your new password: ")
            admin1.passwordStrength(newPassword)
        verifiedPassword = self.passwordCheck(newPassword)

        username1 = input("username: ")
        user1 = Checker(verifiedPassword, username1)
        location = user1.idCheck()
        with open('basicInformation.json') as file:
            data = json.load(file)
        print(data)
        print(data['users'][location]['password'])
        data['users'][location]['password'] = verifiedPassword
        print(data)
        with open('basicInformation.json', 'w+') as file:
            json.dump(data, file, indent=3)
            file.close()

        print('Your new password is: ' + newPassword)

    @staticmethod
    def generatePassword():
        '''
        This function generates a random password

        Returns
        -------
        str
           The password generated using this function should be a string because it consists of numbers and characters.

        TypeError
            There should not be any input, otherwise it will raise a type error.
        '''
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
        symbol = ['#', '%', '^', '&', '*', '+', '@', '!', '?', '~']
        wordOne = choice(alpha) + choice(symbol) + choice(alpha)
        wordTwo = choice(alpha) + choice(alpha) + choice(symbol)
        password = randint(100000, 999999)
        prepPassword = (wordOne + str(password) + wordTwo)
        newPassword = prepPassword.capitalize()
        password_statement = ("Generated password: " + str(newPassword))
        print(password_statement)
        return newPassword

    @staticmethod
    def passwordCheck(password):
        '''
        Checks to see if a password is taken


        Parameters
        ----------
        password : str
               The password should be a str

        Returns
        -------
        str
            The password that is not taken

        Raises
        ------
        TypeError
             If the password is not a str
        '''
        if not isinstance(password, str):
            raise TypeError('passwordCheck expecting a str as input')

        with open('basicInformation.json') as file:
            data = json.load(file)
            print(data)
        checker = data['users']
        print(checker)
        length = len(checker)
        i = 0

        while i < length:

            if password == checker[i]['password']:
                print("This password is taken!")
                anotherPassword = input("Use another password: ")
                if anotherPassword != checker[i]['password']:
                    return anotherPassword

            i += 1

        else:
            print("You can use this password")
            return password

    def passwordStrength(self, password):
        '''
        Password strength is being calculated on a scale of 4

        This will check the password strength from length, characters being used

        Parameters
        ----------
        password : str
                Password is the input

        Returns
        -------
        str
            level of security of the password

        Raises
        ------
        TypeError
              If the input is not str


        '''
        if not isinstance(password, str):
            raise TypeError('passwordStrength expecting a str as input')

        aStatement = 'This password is '

        #strong = colored(aStatement + 'strong', 'green')
        #ok = colored(aStatement + 'decent', 'cyan')
        #weak = colored(aStatement + 'weak', 'yellow')
        #bad = colored(aStatement + 'horrible', 'red')

        strong = (aStatement + 'strong')
        ok = (aStatement + 'decent')
        weak = (aStatement + 'weak')
        bad = (aStatement + 'horrible')
        score = 0
        if len(password) >= 10:
            score = score + 1
        if not password.isalpha():
            score = score + 1
        if not password.isdigit():
            score = score + 1
        if not password.isalnum():
            score = score + 1
        if ' ' in password or password.isspace():
            score = 0
        if score == 0:
            print(bad)
            return bad
            #self.generatePassword()
        elif score == 1:
            print(weak)
            return weak
            #self.generatePassword()
        elif score == 2:
            print(ok)
            return ok
        else:
            print(strong)
            return strong
        #return score


admin1 = Password()
try:
    admin2 = Password()
    print(admin2.changePassword(100))
    print(admin2.generatePassword('gfhf'))
    print(admin2.passwordCheck(2))
    print(admin2.passwordStrength(3))
except TypeError as d:
    print('Something went wrong: ' + str(d))




#def delUser(number):
    #del data['users'][i]

#portal()
#admin2.generatePassword()
#admin1.passwordStrength('  dsf')
#admin1.changePassword()
'''
Data can be in many forms such as str, int, float and so much more. Apparently, the maximum length of a str that Json 
can hold is 2097152 characters, which is huge and will be hard to pass that limit. As for the file size limit, 
18446744073709551616 characters is the answer, which is equivalent to 2^64 bytes. Moreover, Json is a lightweight basic 
file, so it mainly supports 6 data types: string, number, boolean, null, array, and object. By using sys.maxsize, it 
shows me the largest positive integer supported by python, which is 9223372036854775807, and the largest negative 
integer is -maxint - 1, which gives you -9223372036854775806. 





#print(sys.maxsize)

>>> class User:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)

>>> student_objects = [
        User('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '0 - 10', '10 - 18', '18 - 28', '28 - 50'

child = 0
teen = 0
adult = 0
elder = 0
length = len(infoSort)


while length > 0:
    length -= 1
    i = 0
    while i < length:
        if i in range(0, 10):
            child = child + 1
        if i in range(10 - 18):
            teen = teen + 1
        if i in range(18, 28):
            adult = adult + 1
        else:
            elder = elder + 1
        print(i)
        i += 1
'''


class Admin:
    def __init__(self):
        '''
        Constructor to build a password object


        '''
        pass

    def statusCheck(self, number):
        '''
        Checks the status to determine if the user is a user or a administrator


        Parameters
        ----------
        number : int
               This is the input of position in order to find where the status is stored


        Raises
        ------
        TypeError
            If number is not an int
        IndexError
            If the number is out of range

        '''
        with open('basicInformation.json') as file:
            data = json.load(file)
        infoCheck = data['users']

        if not isinstance(number, int):
            raise TypeError('passwordVerify expecting the input as a number')
        if number > len(infoCheck):
            raise IndexError('List Index out of range')

        if infoCheck[number]["status"] == "administrator":
            print("loading admin portal")
            return True
            #self.adminPortal()
        elif infoCheck[number]['status'] == "user":
            pass

    def adminPortal(self):
        '''
        This is the admin portal where admin can access other features


        Raises
        ------
        TypeError
            This function does not take in any value
        '''
        responses = input("What do you wish to do (1: ageDemographics) : ")
        if responses == 'ageDemographics' or '1':
            self.ageDemographics()

        if responses == 'delete User' or '2':
            userIdOne = input("Which user to delete: ")
            self.deleteUser(userIdOne)

    def ageDemographics(self):
        '''
        Admins can access this to see a graph of user's age.


        TypeError
            There should not be any input, otherwise it will raise a type error.
        '''

        with open('basicInformation.json') as file:
            data = json.load(file)
            print(data)
        infoSort = data['users']

        infoSort.sort(key=lambda age: age['age'])
        labels = '0 - 10', '10 - 20', '20 - 30', '30 - 40', '40 - 50'
        child = 0
        teen = 0
        youngAdult = 0
        adult = 0
        middleAged = 0
        length = len(infoSort)
        i = 0
        while i < length:
            if 0 <= infoSort[i]['age'] < 10:
                child = child + 1
            elif 10 <= infoSort[i]['age'] < 20:
                teen = teen + 1
            elif 20 <= infoSort[i]['age'] < 30:
                youngAdult = youngAdult + 1
            elif 30 <= infoSort[i]['age'] < 40:
                adult = adult + 1
            else:
                middleAged = middleAged + 1
            i += 1
        sizes = []
        sizes.insert(0, child / length)
        sizes.insert(1, teen / length)
        sizes.insert(2, youngAdult / length)
        sizes.insert(3, adult / length)
        sizes.insert(4, middleAged / length)
        print(sizes)
        explode = (0, 0.1, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title('Age Pie Graph')
        plt.show()

    @staticmethod
    def deleteUser(userId):
        '''
        Admins can delete users that violated any policies


        TypeError
            The input should only be a str
        '''
        with open('basicInformation.json') as file:
            data = json.load(file)
            print(data)
        #length = len(info)
        for i in data['users'][:]:
            if i['userId'] == userId:
                data['users'].remove(i)
                print(data)
                data.update(data)
        with open('basicInformation.json', 'w+') as file:
            json.dump(data, file, indent=3)
            file.close()



try:
    adminx = Admin()
    print(adminx.statusCheck('hi'))
    print(adminx.adminPortal(22))
    print(adminx.ageDemographics(20))
except (TypeError, IndexError) as c:
    print('Something went wrong: ' + str(c))
#portal()
'''
chatbot = ChatBot('Virtual Parent')

#trainer = ListTrainer(chatbot)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.chinese")

while True:
    request = input('You: ')
    response = chatbot.get_response(request)
    print('Bot: ', response)
'''
'''
# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response("How is your health")

print(response)
'''


class User:
    def __init__(self):
        '''
        Constructor to build a password object


        '''
        pass


    def userPortal(self):
        '''
        This is the user portal where admin can access other features


        Raises
        ------
        TypeError
            This function does not take in any value
        '''
        responses = input("What do you wish to do (1: changePassword) : ")
        if responses == 'changePassword' or '1':
            self.changePassword()

    @staticmethod
    def changePassword(self):
        '''
        This function will be overridden


        Raises
        ------
        TypeError
            This function does not take in any value
        '''
        pass

