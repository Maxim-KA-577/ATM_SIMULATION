from tkinter import *
from tkinter import ttk
import tkinter as tk
import classes

def validate_input(char):
    return char.isdigit()

def save_setting(root, pan, money, valid_period, number):
    card_pan = pan.get()
    card_money = money.get()
    card_valid_period = valid_period.get()
    card_number = number.get()
    if len(str(card_pan)) != 4 or len(str(card_number)) != 16 or len(str(card_valid_period)) != 4:
        error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
        error_label.place(x=10,y=250)

    else:
        if int(card_valid_period) // 100 > 12 or int(card_valid_period) // 100 < 1:
            error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
            error_label.place(x=10,y=250)

        else:
            root.destroy()
            create_window()
            card = classes.Card(card_pan, card_valid_period, card_number, card_money)

def create_window():
    window = Tk()
    window.title("ATM")
    window.minsize(1100, 500)
    window.maxsize(1100, 500)
    canvas = Canvas(bg="grey", width=1100, height=500)
    canvas.pack()
    
    #canvas.create_rectangle(850, 130, 1050, 135)
    #canvas.create_rectangle(50, 10, 730, 430, fill="black")
    card_draw = canvas.create_rectangle(860, 140, 1040, 430, fill="green")
    print(card_draw)
    
    btn_working = ttk.Button(text = "вставить кату", command = lambda: atm.set_card())
    btn_working.place(x = 910, y = 440)
        
#создаём окно настройки карты
window = Tk()
window.title("card setting")
window.minsize(600, 400)
window.maxsize(600, 400)

atm = classes.ATM(1000000)

#создаём поля ввода и соханяем полученные данные card
validate = window.register(validate_input)
pan_label = tk.Label(window, text = "введите пинкод(4 цифры без пробелов)", font=("Arial", 10))
pan_var = tk.StringVar()
pan = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
valid_period_label = tk.Label(window, text = "введите срок годности карты(4 цифры без пробелов)", font=("Arial", 10))
valid_period = tk.StringVar()
valid_period = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
number_label = tk.Label(window, text = "введите номер карты(16 цифор без пробелов)", font=("Arial", 10))
number = tk.StringVar()
number = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
money_label = tk.Label(window, text = "введите баланс карты(без пробелов)", font=("Arial", 10))
money = tk.StringVar()
money = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))

pan_label.place(x = 10, y = 95)
pan.place(x = 10,y = 115)
valid_period_label.place(x = 10, y = 55)
valid_period.place(x = 10, y = 75)
number_label.place(x = 10, y = 15)
number.place(x = 10, y = 35)
money_label.place(x = 10, y = 135)
money.place(x = 10, y = 155)


save = tk.Button(window, text = "закончить настройку", command = lambda: save_setting(window, pan, money, valid_period, number))
save.place(x = 10,y = 200)

#работа с банкоматом
txt = ""
def refresh_window(atm, card, txt):
    if (atm.get_condition() == "ATM_WAIT"):
        create_window()
        window.update()
        #set_card()
        refresh_window()
    elif (atm.get_condition() == "AT"):
        pass
    else:
        pass


                







    
