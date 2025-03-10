from tkinter import *
from tkinter import ttk
import tkinter as tk
import classes

def validate_input(char):
    return char.isdigit()

def save_setting(root, pan, money, valid_period, number):
    pan = pan.get()
    money = money.get()
    valid_period = valid_period.get()
    number = number.get()
    if len(pan) != 4 or len(number) != 16 or len(valid_period) != 4:
        error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
        error_label.place(x=10,y=250)

    else:
        if int(valid_period) // 100 > 12 or int(valid_period) // 100 < 1:
            error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
            error_label.place(x=10,y=250)

        else:
            root.destroy()
            create_window(pan, valid_period, number, money)

def create_window(card_pan, valid_period, number, card_money):
    card = classes.Card(pan, valid_period, number, money)
    
    window = Tk()
    window.title("ATM")
    window.minsize(1100, 600)
    window.maxsize(1100, 600)
    canvas = Canvas(bg="grey", width=1100, height=600)
    canvas.pack()
    canvas.create_rectangle(850, 200, 1050, 205)
    card = canvas.create_rectangle(860, 210, 1040, 500, fill="green")
    canvas.create_rectangle(50, 10, 700, 350, fill="black")

    insert_card = ttk.Button(text = "вставить карту", command = lambda: activate(card))
    insert_card.place(x = 860, y = 550)

def activate(card):
    atm = classes.ATM(87000, card)

    #сделать строки ввода как на окне настройки карты
    #реализовать анологичной структурой 

window = Tk()
window.title("card setting")
window.minsize(600, 400)
window.maxsize(600, 400)

#ОБЪЯВЛЕНИЯ
#ПОСТАНОВКА
validate = window.register(validate_input)
pan_label = tk.Label(window, text = "введите пинкод(4 цифры без пробелов)", font=("Arial", 10))
pan_label.place(x = 10, y = 95)
pan_var = tk.StringVar()
pan = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
pan.place(x = 10,y = 115)
valid_period_label = tk.Label(window, text = "введите срок годности карты(4 цифры без пробелов)", font=("Arial", 10))
valid_period_label.place(x = 10, y = 55)
valid_period = tk.StringVar()
valid_period = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
valid_period.place(x = 10, y = 75)
number_label = tk.Label(window, text = "введите номер карты(16 цифор без пробелов)", font=("Arial", 10))
number_label.place(x = 10, y = 15)
number = tk.StringVar()
number = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
number.place(x = 10, y = 35)
money_label = tk.Label(window, text = "введите баланс карты(без пробелов)", font=("Arial", 10))
money_label.place(x = 10, y = 135)
money = tk.StringVar()
money = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
money.place(x = 10, y = 155)
save = tk.Button(window, text = "закончить настройку", command = lambda: save_setting(window, pan, money, valid_period, number))
save.place(x = 10,y = 200)
    
    
    
