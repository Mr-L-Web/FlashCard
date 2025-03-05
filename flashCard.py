from tkinter import *
from tkinter import messagebox
import random

root = Tk()

root.title("Flash Cards") #Creates a title for the app window
root.geometry('350x200')#Sets the geometry for the window

capital_list = {'Capital of France?': 'Paris',
                'Capital of Spain?' : 'Madrid',
                'Capital of Austrailia?': 'Canberra',
                'Capital of USA?': 'Washington DC',
                'Capital of UK?': 'London',
                'Capital of Italy?': 'Rome',
                'Capital of Japan?': 'Tokyo',
                'Capital of New Zealand?': 'Wellington',
                'Capital of Brazil?': 'Brasilia',
                'Capital of Canada?': 'Ottawa'} #Dictionary for the Capital city subject


times_table_list = {'2 x 4 = ?' : '8',
                    '5 x 6 = ?' : '30',
                    '8 x 3 = ?' : '24',
                    '7 x 9 = ?' : '63',
                    '12 x 13 =?': '156',
                    '11 x 6 = ?' : '66'}

home = Frame(root)
selectLbl = Label(home, text = "Select your subject") #Label for the home screen
selectLbl.grid(column = 2, row = 0)



capCities = Frame(root)
timTables= Frame(root)
answerC = Entry(capCities, width = 10) #Text box for answers
answerTT = Entry(timTables, width = 10)
markIncorrectC = Label(capCities, text = "Incorrect")
markCorrectC = Label(capCities, text = "Correct")
markIncorrectTT = Label(timTables, text = "Incorrect")
markCorrectTT = Label(timTables, text = "Correct")












    
def capital():
    capCities.grid(column = 0, row = 0)
    menuButtC.grid(column = 0, row = 6)
    global cap
    cap = random.choice(list(capital_list.keys())) #The app picks a capital key from the dictionary at random
    global capCity
    capCity = Label(capCities, text = cap)
    capCity.grid(column = 1, row = 1)
    home.grid_remove()
    sub_AnswerC.grid(column = 3, row = 4)
    answerC.grid(column = 1, row = 4)


def timesTable():
    global tim
    global table
    timTables.grid(column = 0, row = 0)
    menuButtTT.grid(column = 0, row = 6)
    tim = random.choice(list(times_table_list.keys())) #The app picks a times table key from the dictionary at random
    table = Label(timTables, text = tim)
    table.grid(column = 1, row = 1)
    home.grid_remove()
    sub_AnswerTT.grid(column = 3, row = 4)
    answerTT.grid(column = 1, row = 4)



def submitC():
    if answerC.get().lower() == capital_list.get(cap).lower():
        markIncorrectC.grid_remove()
        markCorrectC.grid(column = 2, row = 5)
    else:
        markCorrectC.grid_remove()
        markIncorrectC.grid(column = 2, row = 5)


def submitTT():
    if answerTT.get().lower() == times_table_list.get(tim):
        markIncorrectTT.grid_remove()
        markCorrectTT.grid(column = 2, row = 5)
    else:
        markCorrectTT.grid_remove()
        markIncorrectTT.grid(column = 2, row = 5)
        
def menuC():
    capCities.grid_remove()
    capCity.grid_remove()
    menuButtC.grid_remove()
    home.grid()

def menuTT():
    timTables.grid_remove()
    table.grid_remove()
    menuButtTT.grid_remove()
    home.grid()



capitalLbl = Button(home, text = "Capital Cities", command = capital)
capitalLbl.grid(column = 1, row = 1)
timeLbl = Button(home, text = "Times Tables", command = timesTable)
timeLbl.grid(column = 2 , row = 1)

sub_AnswerC = Button(capCities, text = "Submit Answer", command = submitC)
sub_AnswerTT = Button(timTables, text = "Submit Answer", command = submitTT)


menuButtC = Button(root, text = "Menu", command = menuC)
menuButtTT = Button(root, text = "Menu", command = menuTT)

home.grid(column = 0, row = 0)


    
    






root.mainloop()
