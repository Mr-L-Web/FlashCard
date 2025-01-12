from tkinter import *
from tkinter import messagebox
import random

root = Tk()

root.title("Flash Cards") #Creates a title for the app window
root.geometry('350x200')#Sets the geometry for the window

capital_list = {'Capital of France?': 'Paris',
                'Capital of Spain?' : 'Madrid',
                'Capital of Austrailia?': 'Canberra'} #Dictionary for the Capital city subject





selectLbl = Label(root, text = "Select your subject") #Label for the home screen
selectLbl.grid(column = 2, row = 0)



answer = Entry(root, width = 10) #Text box for answers

cap = key = random.choice(list(capital_list.keys())) #The app picks a capital key from the dictionary at random

   
def capital():
    capCity = Label(root, text = cap)
    capCity.grid(column = 1, row = 3)
    selectLbl.grid_remove()
    sub_Answer.grid(column = 3, row = 4)
    capitalLbl.grid_remove()
    answer.grid(column = 1, row = 4)

def submit():
    markIncorrect = Label(root, text = "incorrect")
    markCorrect = Label(root, text = "correct")
    if answer.get().lower() == capital_list.get(cap).lower():
        markIncorrect.grid_remove()
        markCorrect.grid(column = 2, row = 5)
    else:
        markCorrect.grid_remove()
        markIncorrect.grid(column = 2, row = 5)
        
    

sub_Answer = Button(root, text = "Submit Answer", command = submit)


capitalLbl = Button(root, text = "Capital Cities", command = capital)
capitalLbl.grid(column = 1, row = 1)










root.mainloop()
