
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import json
import tkinter.messagebox
import pygame
from tkinter import simpledialog





window = tk.Tk()
window.title('Virtual Parent')
window.geometry('500x500')


canvas = Canvas(window, width=400, height=400)
canvas.pack(side='top')
image = Image.open("VPAvatar.gif")
#image = image.resize((252, 200), Image.ANTIALIAS)
image = image.resize((244, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
#img = ImageTk.PhotoImage(Image.open("VPLogo.png"))
#image = img.resize((250, 250), Image.ANTIALIAS)
canvas.create_image(70, 20, anchor=NW, image=img)


pygame.init()


def introSound():
    pygame.mixer.music.load("MainQuestion.mp3")
    pygame.mixer.music.play()

introSound()
label1 = tk.Label(window, text="Is this your first time using Virtual Parent?", bg='MediumPurple1',
                  font=('Times New Roman', 15), width=35, height=4).place(x=110, y=300)
#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
#label1.pack(pady=10)


def userSignUp():
    def actualSignUp(newPasswordU):
        newId1 = newId.get()
        newName1 = newName.get()
        newAge1 = int(newAge.get())
        newPassword1 = newPasswordU
        myDict2 = dict({'userId': 'null', 'name': 'null', 'age': 0, 'birthday': [], 'password': 'null', 'country':
                   'null', 'status': 'users'})
        myDict2['userId'] = newId1
        myDict2['name'] = newName1
        myDict2['age'] = newAge1
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
        tkinter. messagebox.showinfo('Welcome', 'You have successfully signed up!')
        loginSound()
        windowSignUp.destroy()

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
    tk.Label(windowSignUp, text="Please enter your basic information so your Virtual Parent can know more about you."
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

    def passwordCheck():
        with open('basicInformation.json') as file:
            data = json.load(file)
            print(data)
        checker = data['users']
        print(checker)
        length = len(checker)
        i = 0
        new_pass = newPassword.get()
        while i < length:
            if new_pass == checker[i]['password']:
                print("This password is taken!")
                #a = tkinter.messagebox.askretrycancel(title='Password is taken', message='Choose another password',)
                right = 0
                while right < 1:
                    anotherPassword = simpledialog.askstring("Input", "Enter another password?",
                                                    parent=windowSignUp)
                    if anotherPassword != checker[i]['password']:
                        actualSignUp(anotherPassword)
                        #return anotherPassword
            i += 1
        else:
            actualSignUp(new_pass)

    tk.Button(windowSignUp, text='Sign Up', width=7,
                        height=2, fg="SkyBlue1", command=passwordCheck).place(x=220, y=450)

    def password_strength():
        from portal import Password
        admin1 = Password()
        levelOfStrength = admin1.passwordStrength(newPassword.get())
        tkinter.messagebox.showinfo(message=levelOfStrength)

    tk.Button(windowSignUp, text='Check', width=5,height=1, fg="red", command=password_strength).place(x=433, y=409)

        #command = lambda: [actualSignUp(), loginSound()]
        #command = actualSignUp


def loginSound():
    pygame.mixer.music.load("Greetings.mp3")  # Loading File Into Mixer
    pygame.mixer.music.play()


def userLogin():
    from portal import Admin
    def checking():
        from portal import Checker
        enterId1 = enterId.get()
        enterPassword1 = enterPassword.get()
        user1 = Checker(enterPassword1, enterId1)
        location = user1.idCheck()
        password_verify = user1.passwordVerify(location)
        admin3 = Admin()
        adminLogin = admin3.statusCheck(location)
        if adminLogin:
            windowLogin.destroy()
            loginSound()
            tk.messagebox.showinfo(title='Access Granted', message='Welcome Back, ' + enterId1)
            adminLoginWindow = tk.Toplevel(window)
            adminLoginWindow.geometry('500x500')
            adminLoginWindow.title('Admin Login Window')

            def demo():
                admin3.ageDemographics()

            def user_delete():
                userId = simpledialog.askstring("Delete User", "Enter the User Id",
                                                    parent=adminLoginWindow)
                admin_one = Checker("none", userId)
                user_location = admin_one.idCheck()
                with open('basicInformation.json') as file:
                    data = json.load(file)
                info = data['users']
                tkinter.messagebox.askyesno(title='deleting User', message=info[user_location], parent=adminLoginWindow)
                while True:
                    admin3.deleteUser(userId)
                    break
                else:
                    pass

            tk.Button(adminLoginWindow, text='Delete User', width=20,
                      height=2, fg="SkyBlue2", command=user_delete).place(x=185, y=350)
            tk.Button(adminLoginWindow, text='User Demographics', width=20,
                      height=2, fg="SkyBlue2", command=demo).place(x=185, y=380)
            #todo: delete user and class of portals, change password

        elif password_verify:
            loginSound()
            tk.messagebox.showinfo(title='Access Granted', message='Welcome Back, ' + enterId1)

        else:
            tk.messagebox.showerror(message='Error, Wrong Password, try again.')

    windowLogin = tk.Toplevel(window)
    windowLogin.geometry('500x500')
    windowLogin.title('Login Window')

    enter_id = tk.StringVar()
    enter_password = tk.StringVar()

    canvas2 = Canvas(windowLogin, width=300, height=300)
    canvas2.pack(side='top')
    image2 = Image.open("VPLogin.png")
    imageTwo = image2.resize((285, 250), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(imageTwo)
    canvas2.create_image(20, 10, anchor=NW, image=img2)

    tk.Label(windowLogin, text="Enter your user id:", font=('Times New Roman', 15),
             width=35, height=2).place(x=20, y=278)
    enterId = tk.Entry(windowLogin, textvariable=enter_id)
    enterId.place(x=243, y=284)

    tk.Label(windowLogin, text="Enter your password:", font=('Times New Roman', 15),
             width=35, height=2).place(x=20, y=320)
    enterPassword = tk.Entry(windowLogin, textvariable=enter_password, show='*')
    enterPassword.place(x=243, y=325)

    tk.Button(windowLogin, text='Login', width=7,
              height=2, fg="SkyBlue2", command=checking).place(x=215, y=380)

    image3 = Image.open("VpHome.png")
    imageThree = image3.resize((87, 50), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(imageThree)
    Button(windowLogin, image=img3,
           compound=LEFT, command=exit).pack(side=BOTTOM)


def exit():
    window.quit()
    sys.exit(0)


button1 = tk.Button(window, text='Yes', width=7,
              height=2, fg="SkyBlue1", command=userSignUp)
button2 = tk.Button(window, text='No', width=7,
              height=2, fg="SkyBlue1", command=userLogin)
button1.pack()
button2.pack(pady=10)


class ChatBot:
    pass


class User:
    pass


class SignUpWindow:
    pass


class MainWindow:
    def __init__(self):
        pass


class LoginWindow:
    pass



from portal import Admin
from portal import Checker


class AdminWindow(Admin):
    def __init__(self):
        '''
        Constructor to build a password object


        '''
        super().__init__()

    def statusCheck(self, number):
        super().statusCheck(number)

    def adminLogin(self):
        enterId1 = enterId.get()
        enterPassword1 = enterPassword.get()
        user1 = Checker(enterPassword1, enterId1)
        location = user1.idCheck()
        password_verify = user1.passwordVerify(location)
        admin3 = Admin()
        adminLogin = admin3.statusCheck(location)
        if adminLogin:
            self.adminPortal()


    def adminPortal(self):
        windowLogin.destroy()
        loginSound()
        tk.messagebox.showinfo(title='Access Granted', message='Welcome Back, ' + enterId1)
        adminLoginWindow = tk.Toplevel(window)
        adminLoginWindow.geometry('500x500')
        adminLoginWindow.title('Admin Login Window')
        tk.Button(adminLoginWindow, text='Delete User', width=20,
                  height=2, fg="SkyBlue2", command=self.deleteUser).place(x=185, y=350)
        tk.Button(adminLoginWindow, text='User Demographics', width=20,
                  height=2, fg="SkyBlue2", command=self.ageDemographics()).place(x=185, y=380)

    def adminLoginWindow(self):
        adminLoginWindow = tk.Toplevel(window)
        adminLoginWindow.geometry('500x500')
        adminLoginWindow.title('Admin Login Window')
        return adminLoginWindow

    @staticmethod
    def ageDemographics():
        super().ageDemographics()

    def deleteUser(self):
        userId = simpledialog.askstring("Delete User", "Enter the User Id",
                                        parent=self.adminLoginWindow)
        admin_one = Checker("none", userId)
        user_location = admin_one.idCheck()
        with open('basicInformation.json') as file:
            data = json.load(file)
        info = data['users']
        tkinter.messagebox.askyesno(title='deleting User', message=info[user_location], parent=self.adminLoginWindow)
        while True:
            super().deleteUser(userId)
            break
        else:
            pass


window.mainloop()



