import sys
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import json
import tkinter.messagebox
import pygame
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
from tkinter import simpledialog
from portal import Admin
from portal import Checker
from portal import Password
from portal import User

window = tk.Tk()
window.title('Virtual Parent')
window.geometry('500x500')
pygame.init()



def exitApplication():
    '''
    This function closes the whole program


    Warnings
    --------
    This is function will close everything
    '''
    window.quit()
    sys.exit(0)

class Window:
    '''
    A Graphical User Interface parent window


    Methods
    -------
    initialize() -> None
        creates a parent window
    soundEffect() -> None
        plays a sound

    '''
    def __init__(self):
        '''
        Constructor that builds Gui window

        '''
        pass

    def initialize(self):
        '''
        This method initialize the current window, and this method will be inherited by sub classes


        Raises
        ------
        NotImplementedError
            This error is raise because it does not do anything, and its purpose is to be overridden by sub classes


        '''
        raise NotImplementedError()

    def soundEffect(self):
        '''
        This method creates sound effects


        Raises
        ------
        NotImplementedError
            This error is raise because it does not do anything, and its purpose is to be overridden by sub classes


        '''
        raise NotImplementedError()


class SignUpWindow(Window):
    '''
    A signup window that inherits from window class


    Methods
    -------
    initialize() -> None
        creates a signup window
    passwordCheck() -> None
        checks the password
    actualSignUp() -> None
        sign up the new user
    passwordStrength() -> None
        checks for the strength of the password

    '''
    def __init__(self):
        '''
        This class inherits from the window class


        '''
        super().__init__()

    def initialize(self):
        '''
        This method creates the sign up window

        This method gives you the options to sign up and check the strength of the password


        Warnings
        --------
        This method takes longer to load, so you have to wait a bit to enter the values.

        Raises
        ------
        TypeError
            This method does not take in any value as input
        '''
        windowSignUp = tk.Toplevel(window)
        windowSignUp.geometry('500x500')
        windowSignUp.title('Sign Up Window')

        canvas1 = Canvas(windowSignUp, width=250, height=250)
        canvas1.pack(side='top')
        image1 = Image.open("VpSignUpAvatar.png")
        imageOne = image1.resize((224, 230), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(imageOne)
        label = Label(image=img1)
        label.image = img1
        canvas1.create_image(20, 10, anchor=NW, image=img1)

        new_id = tk.StringVar()
        new_name = tk.StringVar()
        new_age = tk.StringVar()
        new_password = tk.StringVar()
        tk.Label(windowSignUp,
                 text="Please enter your basic information so your Virtual Parent can know more about you."
                 , font=('Times New Roman', 13), width=65, height=3).place(x=12, y=232)
        tk.Label(windowSignUp, text="Enter a login name:", font=('Times New Roman', 15),
                 width=35, height=2).place(x=20, y=278)
        newId = tk.Entry(windowSignUp, textvariable=new_id)
        newId.place(x=243, y=284)
        tk.Label(windowSignUp, text="Enter your full name:", font=('Times New Roman', 15),
                 width=35, height=2).place(x=20, y=320)
        newName = tk.Entry(windowSignUp, textvariable=new_name)
        newName.place(x=243, y=325)

        tk.Label(windowSignUp, text="Enter your age:", font=('Times New Roman', 15),
                 width=35, height=2).place(x=20, y=360)
        newAge = tk.Entry(windowSignUp, textvariable=new_age)
        newAge.place(x=243, y=366)

        tk.Label(windowSignUp, text="Enter your password:", font=('Times New Roman', 15),
                 width=35, height=2).place(x=20, y=403)
        newPassword = tk.Entry(windowSignUp, textvariable=new_password)
        newPassword.place(x=243, y=407)

        '''
        def getValue3():
            newPassword1 = newPassword.get()
            return newPassword1

        def getValue4():
            newId1 = newId.get()
            return newId1

        def getValue5():
            newName1 = newName.get()
            return newName1

        def getValue6():
            newAge1 = int(newAge.get())
            return newAge1
        '''
        tk.Button(windowSignUp, text='Sign Up', width=7,
                  height=2, fg="SkyBlue1", command=lambda: [self.passwordCheck(newPassword.get(), windowSignUp, newId.get(),
                                                            newName.get(), int(newAge.get()))]).place(x=220, y=450)

        tk.Button(windowSignUp, text='Check', width=5, height=1, fg="red", command=lambda: [self.passwordStrength(newPassword.get())]).place(x=433,y=409)

    def passwordCheck(self, new_pass, window_sign, new_id, new_name, new_age):
        '''
        This method checks to see if the password is taken by other users

        If the password is not taken, it will be stored in the datafile

        Parameters
        ----------
        new_pass : str
            new user's password
        window_sign: TK
            parent window
        new_id : str
            new user's id
        new_name : str
            new user's full name
        new_age : int
            new user's age

        Raises
        ------
        TypeError
            input has other types
        '''
        with open('basicInformation.json') as file:
            data = json.load(file)
            print(data)
        checker = data['users']
        print(checker)
        length = len(checker)
        i = 0


        #new_pass = newPassword.get()
        while i < length:
            if new_pass == checker[i]['password']:
                print("This password is taken!")
                #a = tkinter.messagebox.askretrycancel(title='Password is taken', message='Choose another password',)
                right = 0
                while right < 1:
                    anotherPassword = simpledialog.askstring("Input", "Enter another password?",
                                                    parent=window_sign)
                    if anotherPassword != checker[i]['password']:
                        self. actualSignUp(window_sign, anotherPassword, new_id, new_name, new_age)
                        #return anotherPassword
            i += 1
        else:
            self.actualSignUp(window_sign, new_pass, new_id, new_name, new_age)

    def actualSignUp(self, windowSign, password, new_id, name, age):
        '''
        This method saves the verified user information in the file



        Parameters
        ----------
        windowSign: window
            parent window
        password : str
            user's password
        new_id : str
            new user's id
        name : str
            new user's full name
        age : int
            new user's age

        Raises
        ------
        TypeError
                   user inputs the wrong type of data
        '''


        newPassword1 = password
        myDict2 = dict({'userId': 'null', 'name': 'null', 'age': 0, 'birthday': [], 'password': 'null', 'country':
            'null', 'status': 'users', 'tasks': [], 'timer': 0})
        myDict2['userId'] = new_id
        myDict2['name'] = name
        myDict2['age'] = age
        # myDict2['birthday'] = birthday.split('/')
        myDict2['password'] = newPassword1
        # myDict2['country'] = country
        with open('basicInformation.json') as file:
            info = json.load(file)
            info['users'].append(myDict2)
            info.update(info)

        with open('basicInformation.json', 'w+') as file:
            json.dump(info, file, indent=3)
            file.close()
        tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
        #loginSound()
        windowSign.destroy()

    def passwordStrength(self, password):
        '''
        This method checks to see if the password is strong enough



        Parameters
        ----------
        password : str
            new user's password

        Raises
        ------
        TypeError
            password is not string
        '''
        admin1 = Password()
        levelOfStrength = admin1.passwordStrength(password)
        tkinter.messagebox.showinfo(message=levelOfStrength)


class LoginWindow(Window):
    '''
    A login window that inherits from window class


    Methods
    -------
    initialize() -> None
        creates a login window
    soundEffect() -> None
        plays a welcoming sound
    '''
    def __init__(self):
        super().__init__()

    def initialize(self):
        '''
        This method creates the login window

        This method serves as a tool for both users and admins to login

        Raises
        ------
        TypeError
            This method does not take in any value as input
        '''
        windowLogin = tk.Toplevel(window)
        windowLogin.geometry('500x500')
        windowLogin.title('Login Window')

        enter_id = tk.StringVar()
        enter_password = tk.StringVar()

        canvas2 = Canvas(windowLogin, width=290, height=290)
        canvas2.pack(side="top")
        image2 = Image.open("VPLogin.png")
        imageTwo = image2.resize((285, 250), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(imageTwo)
        img_o = Label(image=img2)
        img.image = img2
        img_o.pack(side=TOP)
        canvas2.create_image(20, 10, anchor=NW, image=img2)

        tk.Label(windowLogin, text="Enter your user id:", font=('Times New Roman', 15),
                 width=35, height=2).place(x=20, y=278)
        enterId = tk.Entry(windowLogin, textvariable=enter_id)
        enterId.place(x=243, y=284)

        tk.Label(windowLogin, text="Enter your password:", font=('Times New Roman', 15),
                 width=35, height=2).place(x=20, y=320)
        enterPassword = tk.Entry(windowLogin, textvariable=enter_password, show='*')
        enterPassword.place(x=243, y=325)

        Button(windowLogin,
               text="exit", compound=LEFT, command=exitApplication).pack(side=BOTTOM)

        Admin1 = AdminWindow()

        '''
        def getValue():
            enterId1 = enterId.get()
            return enterId1
        

        def getValue1():
            enterPassword1 = enterPassword.get()
            return enterPassword1
        '''
        tk.Button(windowLogin, text='Login', width=7,
                  height=2, fg="SkyBlue2", command=lambda: [Admin1.adminLogin(windowLogin, enterId.get(), enterPassword.get())]
                  ).place(x=215, y=380)

        self.soundEffect()

    def soundEffect(self):
        '''
        This method lets the program greets the user


        Raises
        ------
        TypeError
            This method does not take in any value as input
        '''
        pygame.mixer.music.load("Greetings.mp3")
        pygame.mixer.music.play()


class AdminWindow(Admin):
    '''
    A admin window that inherits from Admin class

    Methods
    -------
    statusCheck() -> None
        check for user's status
    adminLogin() -> None
        log the admin into special portal
    adminPortal() -> None
        admin portal with exclusive features
    ageDemographics() -> None
        shows the admin statistics about current user's age
    deleteUser() -> None
        deletes a user that is inactive or inappropriate

    '''
    def __init__(self):
        '''
        Constructor to build a password object


        '''
        super().__init__()

    def statusCheck(self, number):
        '''
        This method uses its parent class's method to distinguish between users and admins

        Parameters
        ----------
        number : int
            new user's password

        Raises
        ------
        TypeError
            number is not int
        '''
        super().statusCheck(number)

    def adminLogin(self, parent, enterId, enterPassword):
        '''
        This method verifies admin login

        Parameters
        ----------
        parent : TK
            parent window
        enterId : str
            admin id
        enterPassword : str
            admin password

        Raises
        ------
        TypeError
            id and password can only be str
        '''

        #enterId1 = enterId.get()
        #enterPassword1 = enterPassword.get()
        user1 = Checker(enterPassword, enterId)
        #user1 = Checker(password, user_id)
        location = user1.idCheck()
        user1.passwordVerify(location)
        admin3 = Admin()
        adminLogin = admin3.statusCheck(location)
        if adminLogin:
            parent.destroy()
            self.adminPortalOne()
        else:
            parent.destroy()
            user_one = UserWindow(enterId, enterPassword)
            user_one.userPortal()

    def adminPortalOne(self):
        '''
        This method creates a window for admins to navigate, and is only for admins

        Raises
        ------
        TypeError
            This function does not taken any value
        '''
        #loginSound()
        tk.messagebox.showinfo(title='Access Granted', message='Welcome Back')
        adminLoginWindow = tk.Toplevel(window)
        adminLoginWindow.geometry('500x500')
        adminLoginWindow.title('Admin Window')
        tk.Button(adminLoginWindow, text='Delete User', width=20,
                  height=2, fg="SkyBlue2", command=lambda: [self.deleteUser(adminLoginWindow)]).place(x=185, y=350)
        tk.Button(adminLoginWindow, text='User Demographics', width=20,
                  height=2, fg="SkyBlue2", command=self.ageDemographics).place(x=185, y=380)

    def ageDemographics(self):
        '''
        This method let's the admin check data on our user.

        Raises
        ------
        TypeError
            There should not be any input, otherwise it will raise a type error.
        '''
        super().ageDemographics()

    def deleteUser(self, parent):
        '''
        This method lets admin delete users that violates any polocies

        Parameters
        ----------
        parent : TK
                parent window

        Raises
        ------
        TypeError
            parent window is neither str nor int

        '''

        userId = simpledialog.askstring("Delete User", "Enter the User Id",
                                        parent=parent)
        admin_one = Checker("none", userId)
        user_location = admin_one.idCheck()
        with open('basicInformation.json') as file:
            data = json.load(file)
        info = data['users']
        tkinter.messagebox.askyesno(title='deleting User', message=info[user_location], parent=parent)
        while True:
            super().deleteUser(userId)
            break
        else:
            pass


class UserWindow(User):
    '''
    A user window that inherits from User class

    Methods
    -------
    userPortal() -> None
        user's special portal
    changePassword() -> None
        user can request a change to their password
    passwordCheckTwo() -> str
        checks for the user password to make sure the password is not taken
    userFeedback() -> None
        user can give feedback in this method
    textInput() -> None
        user enters their feedback here
    toDoList() -> None
        creates a todolist window
    addTask() -> None
        user can add tasks
    deleteOne() -> None
        user can delete a task
    deleteAll() -> None
        user can delete all the tasks they created
    chatNow() -> None
        creates a chat window
    chat() -> None
        begin chatting with the chatbot by entering responses
    chatResponse() -> None
        chatbot will respond to any request from the user
    destroyWindow() -> None
        destroy a window
    countdown() -> none
        Locks a window and countdown


    '''
    def __init__(self, userId, userPassword):
        '''
        Constructor to build a password object


		Parameters
		----------
		userId : str
			active user's id
		userPassword : str
			active user's password
		fg : str
		    main colour theme
		entries : int
			To check how many times user sent a message to the chatbot
        '''
        super().__init__()
        self.userId = userId
        self.userPassword = userPassword
        self.fg = "MediumPurple1"
        self.entries = 0

    def userPortal(self):
        '''
        This method creates a window for users to navigate, and is only for admins

        Raises
        ------
        TypeError
            This function does not taken any value
        '''
        tk.messagebox.showinfo(title='Access Granted', message='Welcome Back')
        userWindow = tk.Toplevel(window)
        userWindow.geometry('500x500')
        userWindow.title('User Window')

        tk.Button(userWindow, text='Change Password', width=20,
              height=2, fg="SkyBlue2", command=lambda: [self.changePassword(userWindow)]).place(x=160, y=260)

        tk.Button(userWindow, text='Feedback', width=20,
                  height=2, fg="SkyBlue2", command=lambda: [self.userFeedback(userWindow)]).place(x=160, y=320)

        tk.Button(userWindow, text='Quit', width=20,
                  height=2, fg="SkyBlue2", command=lambda: [exitApplication()]).place(x=160, y=290)

        tk.Button(userWindow, text='Chat Now', width=20,
                  height=2, fg="SkyBlue1", command=lambda: [self.chatNow(userWindow)]).place(x=160, y=200)

        #tk.Button(userWindow, text='Meal Planner', width=20,
                  #height=2, fg="SkyBlue2", command=None).place(x=160, y=290)

        #tk.Button(userWindow, text='Workout Generator', width=20,
                  #height=2, fg="SkyBlue2", command=None).place(x=160, y=260)

        tk.Button(userWindow, text='To-do List', width=20,
                  height=2, fg="SkyBlue2", command=lambda: [self.toDoList(userWindow)]).place(x=160, y=230)

    def changePassword(self, parent):
        '''
        This method can change password for our users

        Users have the freedom to decide if they want us to generate a password or not

        Parameters
		----------
		parent : TK
			parent window

        Raises
        ------
        TypeError
            This function only takes the window has input
        '''
        YES = tkinter.messagebox.askyesno(title='Password Change', message="Do you want me to generate a password for "
                                                                           "you?", parent=parent)
        if YES:
            passwordGen = Password()
            newPassword1 = passwordGen.generatePassword()
            verifiedPassword = self.passwordCheckTwo(newPassword1, parent)
            user1 = Checker(verifiedPassword, self.userId)
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

            tk.messagebox.showinfo("Information", "Your new password is " + verifiedPassword)

        else:
            answer = simpledialog.askstring("Input", "Enter your new password: ",
                                            parent=parent)
            if answer is not None:
                newPassword2 = answer
                verifiedPassword = self.passwordCheckTwo(newPassword2, parent)
                user1 = Checker(verifiedPassword, self.userId)
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

                tk.messagebox.showinfo("Information", "Your new password is " + verifiedPassword)

            else:
                pass

        #username1 = input("username: ")

    def passwordCheckTwo(self, password, parent):
        '''
        This method checks the password with other passwords in the file to make sure each user gets their own password


        Parameters
        ----------
        password : str
            user's new password
        parent : TK
            parent window


        Raises
        ------
        TypeError
            This function only takes the window and the password has input
        '''
        with open('basicInformation.json') as file:
            data = json.load(file)
        checker = data['users']
        length = len(checker)
        i = 0
            # new_pass = newPassword.get()
        while i < length:
            if password == checker[i]['password']:
                tk.messagebox.showwarning("Warning", "This password is taken! ")
                    # a = tkinter.messagebox.askretrycancel(title='Password is taken', message='Choose another password',)
                right = 0
                while right < 1:
                    anotherPassword = simpledialog.askstring("Input", "Enter another password?",
                                                                 parent=parent)
                    if anotherPassword != checker[i]['password']:
                        return anotherPassword
            i += 1
        else:
            return password

    def userFeedback(self, parent):
        '''
        This method is available for users to give feedback on our product


        Parameters
        ----------
        parent : TK
            parent window

        Raises
        ------
        TypeError
            This function only takes the window has input
        '''
        user_feedback = tk.Toplevel(parent)
        user_feedback.geometry('400x400')
        user_feedback.title('User Feedback')
        #feedback1 = tk.StringVar()
        #feedback_one = tk.Entry(user_feedback, textvariable=feedback1)
        #feedback_one.pack(ipady=10)
        feedback1 = Text(user_feedback, width=30, height=15)
        feedback1.place(x=80, y=60)
        tk.Label(user_feedback, text="Type in your feedback in the box below", font=('Times New Roman', 15),
                 width=35, height=2).place(x=43, y=18)
        tk.Button(user_feedback, text='Submit', width=20,
                  height=2, fg="SkyBlue2", command=lambda: [self.textInput(feedback1), self.destroyWindow(user_feedback)
                                                            ]).place(x=100, y=350)

    def textInput(self, feedback):
        '''
        This method can change password for our users

        Parameters
        ----------
        feedback : text
            feedback texts

        Raises
        ------
        TypeError
            This function only takes the feedback as input
        '''
        text = feedback.get("1.0", "end-1c")
        if text == "":
            tkinter.messagebox.showerror("Empty", "Empty feedback")

        else:
            dictOne = dict({'userId': 'null', 'comment': 'null', 'issue#': 0, 'status': 'pending'})
            dictOne['userId'] = self.userId
            dictOne['comment'] = text
            with open('feedback_file.json') as file:
                data = json.load(file)
            length = len(data["feedback"])
            dictOne['issue#'] = data["feedback"][length-1]["issue#"] + 1

            data["feedback"].append(dictOne)
            data.update(data)

            with open('feedback_file.json', 'w+') as file:
                json.dump(data, file, indent=3)
                file.close()

            tkinter.messagebox.showinfo('Success', 'Thank you, We have received your feedback')

    def toDoList(self, parent):
        '''
        This method is a to do list to help organize the user's daily activities

        Parameters
        ----------
        parent : TK
            parent window

        Raises
        ------
        TypeError
            This function only takes the window has input
        '''
        toDoWindow = tk.Toplevel(parent)
        toDoWindow.geometry('400x400')
        toDoWindow.title('My To-do List')
        listBox1 = Listbox(toDoWindow)
        #Lb1.insert(1, "Python")
        listBox1.place(x=115, y=160)
        tk.Label(toDoWindow, text="To do List", bg='MediumPurple1',
                 font=('Times New Roman', 15), width=35, height=2).place(x=60, y=10)

        Button(toDoWindow, text='Delete All', compound=LEFT, command=lambda: [self.deleteAll(listBox1, data, location)]).place(x=205, y=128)

        Button(toDoWindow, text="Add Task", compound=LEFT, command=lambda: [self.addTask(listBox1, task_one.get(), tasks
                                                                , data), task.delete(0, 'end')]).place(x=150, y=100)

        #delete_place = Button(toDoWindow, text="Delete Task", command=lambda listBox=listBox1: listBox1.delete(ANCHOR))
        #a.grid(sticky="nsew")
        #delete_place.place(x=93, y=128)

        delete_place = Button(toDoWindow, text="Delete Task",
                              command=lambda: [self.deleteOne(listBox1, data, ANCHOR, location)])
        # a.grid(sticky="nsew")
        delete_place.place(x=93, y=128)

        task_one = tk.StringVar()
        task = tk.Entry(toDoWindow, textvariable=task_one)
        task.place(x=105, y=70)

        user1 = Checker(self.userPassword, self.userId)
        location = user1.idCheck()

        with open('basicInformation.json') as file:
            data = json.load(file)
        tasks = data['users'][location]['tasks']
        data.update(data)

        for item in tasks:
            listBox1.insert(END, item)

    @staticmethod
    def addTask(listbox, task, tasksList, data):
        '''
        This method can add tasks for our users

        Parameters
        ----------
        listbox : listbox
            to do list box
        task: str
            the task user added
        tasksList: list
            list of all the tasks
        data : dict
            dict of all the user data

        Raises
        ------
        TypeError
            If the input does not match the true data type
        '''
        listbox.insert(END, task)
        tasksList.append(task)
        data.update(data)
        with open('basicInformation.json', 'w+') as file:
            json.dump(data, file, indent=3)
            file.close()

    @staticmethod
    def deleteOne(listbox, data, position, location):
        '''
        This method can delete a task in the list box

        Parameters
        ----------
        listbox : listbox
            listbox for the to do list
        data : dict
            dictionary that contains user information
        position: ANCHOR
            location of the cursor
        location: int
            position of the user file

        Raises
        ------
        TypeError
            This function only takes the listbox, data, position, and location as input
        '''
        item = listbox.get(listbox.curselection())
        listbox.delete(position)
        data['users'][location]['tasks'].remove(str(item))
        data.update(data)

        with open('basicInformation.json', 'w+') as file:
            json.dump(data, file, indent=3)
            file.close()


    @staticmethod
    def deleteAll(listbox, data, location):
        '''
        This method can be used to delete all tasks in the listbox

        Parameters
        ----------
        listbox : listbox
        	box that holds all the tasks
        data: dict
            dictionary that holds all the info
        location: int
            location of the user file

        Raises
        ------
        TypeError
            This function only takes the listbox, data, and location as input
        '''
        listbox.delete(0, END)
        data['users'][location]['tasks'] = []
        data.update(data)
        with open('basicInformation.json', 'w+') as file:
            json.dump(data, file, indent=3)
            file.close()

    def chatNow(self, parent):
        '''
        This method initiates a new chat interface, which is the main focus of this program


        Parameters
        ----------
        parent : TK
        	parent window

        Raises
        ------
        TypeError
            This function only takes the window has input
        '''
        chatWindow = tk.Toplevel(parent)
        chatWindow.geometry('400x400')
        chatWindow.title('Chat with Virtual Parent')
        chatWindow.resizable(width=FALSE, height=FALSE)

        user1 = Checker(self.userPassword, self.userId)
        location = user1.idCheck()
        with open('basicInformation.json') as file:
            data = json.load(file)
        timeLeft = data['users'][location]['timer']

        if timeLeft != 0:
            tkinter.messagebox.showinfo('Timer', 'It seems like you have unfinished countdown')
            self.countdown(timeLeft, data, location)

        Button(chatWindow, text='Begin Chatting', command=lambda: [self.chat(chatWindow)]).place(x=138, y=290)

        canvas3 = Canvas(chatWindow, width=285, height=285)
        canvas3.pack(side="top")
        image3 = Image.open("VpHome.png")
        imageThree = image3.resize((280, 160), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(imageThree)
        img_a = Label(image=img3)
        img.image = img3
        img_a.pack(side=TOP)
        canvas3.create_image(20, 10, anchor=NW, image=img3)

    def loadingBar(self, parent):
        '''
        This method can change password for our users


        Parameters
        ----------
        parent : TK
            parent window

        Warnings
        --------
        This method does not have the progress bar loaded up. It only acts like a bridge for now

        Raises
        ------
        TypeError
            This function only takes the window has input
        '''
        progressBar = Progressbar(parent, orient=HORIZONTAL,
                               length=120, mode='determinate')
        progressBar.place(x=100, y=100)
        '''
        import time
        progressBar['value'] = 10
        parent.update_idletasks()
        time.sleep(10)

        progressBar['value'] = 90
        parent.update_idletasks()
        '''
        import time
        time.sleep(2)
        progressBar['value'] = 100

    def chat(self, parent):
        '''
        This method trains the chatbot and downloads language boxes

        Parameters
        ----------
        parent : TK
        	parent window

        Warnings
        --------
        This chatbot takes a while to train and it learned mandarin on its own

        Raises
        ------
        TypeError
            This function only takes the window has input
        '''
        chatbot = ChatBot('Virtual Parent')
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train("chatterbot.corpus.english")

        ChatLog = Text(parent, bd=0, bg="white", height="8", width="50", font="Arial", )
        ChatLog.config(state=DISABLED)
        # Bind scrollbar to Chat window
        scrollbar = Scrollbar(parent, command=ChatLog.yview, cursor="heart")
        ChatLog['yscrollcommand'] = scrollbar.set
        # Create Button to send message
        #SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                            #bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                            #command=send)
        # Create the box to enter message
        #EntryBox = Text(parent, bd=0, bg="white", width="29", height="5", font="Arial")
        # EntryBox.bind("<Return>", send)
        # Place all components on the screen
        scrollbar.place(x=383, y=6, height=386)
        ChatLog.place(x=6, y=6, height=386, width=370)
        #EntryBox.place(x=128, y=401, height=90, width=265)
        #SendButton.place(x=6, y=401, height=90)

        text_one = tk.StringVar()
        text = tk.Entry(parent, textvariable=text_one)
        text.place(x=30, y=368)
        Button(parent, text="Send", compound=LEFT, command=lambda: [self.chatResponse(text.get(), chatbot, ChatLog),
                                                                    text.delete(0, 'end')]).place(x=260, y=370)

    def chatResponse(self, response, chatbot, ChatLog):
        '''
        This method gets the chat bot's response

        Parameters
        ----------
        response : str
        	user's input
        chabot: chatbot
            chatbot created by Virtual Parent
        ChatLog: text
            text box that displays conversation

        Raises
        ------
        TypeError
            This function only takes response, chatbot, and ChaLog as input
        '''
        self.entries = self.entries + 1
        if self. entries == 32:
            tkinter.messagebox.showinfo('Timer', 'Take a break, you can resume chatting in 3 minutes, '
                                                 'You should stand up and stretch')
            user1 = Checker(self.userPassword, self.userId)
            location = user1.idCheck()
            with open('basicInformation.json') as file:
                data = json.load(file)

            self.countdown(180, data, location)



        #print(self.entries)
        if response != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + response + '\n\n')
            ChatLog.config(foreground=self.fg, font=("Times New Roman", 13))
            reply = chatbot.get_response(response)
            ChatLog.insert(END, "Virtual Parent: " + str(reply) + '\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

    @staticmethod
    def countdown(timeR, data, location):
        '''
        This method is used to make sure users don't talk to the chatbot for too long

        Parameters
        ----------
        timeR : int
            time out for users
        data: dict
            dict that stores all other user's info
        location : int
            user's location in the dict

        Raises
        ------
        TypeError
            This function only takes timeR, data, and location as input
        '''
        while timeR > 0:
            print(timeR)
            timeR -= 1
            data['users'][location]['timer'] = timeR
            data.update(data)
            with open('basicInformation.json', 'w+') as file:
                json.dump(data, file, indent=3)
                file.close()
            time.sleep(1)


    @staticmethod
    def destroyWindow(parent):
        '''
        This method destroys window not in use

        Parameters
        ----------
        parent = TK
            parent window

        Raises
        ------
        TypeError
            This function only takes parent as input
        '''
        parent.destroy()



windowSignUp = SignUpWindow()
window_login = LoginWindow()


canvas = Canvas(window, width=400, height=400)
canvas.pack(side='top')
image = Image.open("VPAvatar.gif")
        #image = image.resize((252, 200), Image.ANTIALIAS)
image = image.resize((244, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
        #img = ImageTk.PhotoImage(Image.open("VPLogo.png"))
        #image = img.resize((250, 250), Image.ANTIALIAS)
canvas.create_image(70, 20, anchor=NW, image=img)

tk.Label(window, text="Is this your first time using Virtual Parent?", bg='MediumPurple1',
                          font=('Times New Roman', 15), width=35, height=4).place(x=110, y=300)


button1 = tk.Button(window, text='Yes', width=7, height=2, fg="SkyBlue1", command=lambda: [windowSignUp.initialize()])
button2 = tk.Button(window, text='No', width=7, height=2, fg="SkyBlue1", command=window_login.initialize)
button1.pack()
button2.pack(pady=10)




#seconds = input()
#while not seconds.isdigit():
    #print("That wasn't an integer! Enter an integer:")
    #seconds = input()
#seconds = int(seconds)
#countdown(seconds)




'''
feedback = {
    "feedbacks": {
        "userId": "abc",
        "comment": "This function has huge issue."
    }
}
with open("feedback_file.json", "w") as write_file:
    json.dump(feedback, write_file, indent= 5)
'''

window.mainloop()
