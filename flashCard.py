from tkinter import *
from tkinter import messagebox
import random

root = Tk()

root.title("Flash Cards") #Creates a title for the app window
root.geometry('350x200')#Sets the geometry for the window

capital_list = {'Capital of France?': 'Paris',
                'Capital of Spain?' : 'Madrid',
                'Capital of Austrailia?': 'Canberra'} #Dictionary for the Capital city subject


    
def capital():
    capCities.grid(column = 0, row = 0)
    global cap
    global capCity
    cap = random.choice(list(capital_list.keys())) #The app picks a capital key from the dictionary at random
    capCity = Label(capCities, text = cap)
    capCity.grid(column = 1, row = 1)
    home.grid_remove()
    sub_Answer.grid(column = 3, row = 4)
    answer.grid(column = 1, row = 4)


def submit():
    if answer.get().lower() == capital_list.get(cap).lower():
        markIncorrect.grid_remove()
        markCorrect.grid(column = 2, row = 5)
    else:
        markCorrect.grid_remove()
        markIncorrect.grid(column = 2, row = 5)
        
def menu():
    capCities.grid_remove()
    capCity.grid_remove()
    home.grid()




home = Frame(root)
selectLbl = Label(home, text = "Select your subject") #Label for the home screen
selectLbl.grid(column = 2, row = 0)
capitalLbl = Button(home, text = "Capital Cities", command = capital)
capitalLbl.grid(column = 1, row = 1)






    
    

capCities = Frame(root)
answer = Entry(capCities, width = 10) #Text box for answers
markIncorrect = Label(capCities, text = "Incorrect")
markCorrect = Label(capCities, text = "Correct")
sub_Answer = Button(capCities, text = "Submit Answer", command = submit)






menuButt = Button(root, text = "Menu", command = menu)
menuButt.grid(column = 0, row = 6)

home.grid(column = 0, row = 0)





root.mainloop()
