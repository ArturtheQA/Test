import tkinter as TK





#Menu  has 2 fields and 1 button"submit"
#size of the menu is 400*600
#First row is username
username=input('print name')
#Second row is password
password=input('print pwd')

#Submit button triggers the logic in engine(Name of te module here)

isOn=input ("Click button")
TK.mainloop()

def Button(isOn):
    if isOn is True:
        print(username)+print(password)


#Menu Standart
TK.Menu
Menu.