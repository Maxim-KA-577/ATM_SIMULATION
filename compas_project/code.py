from tkinter import *
from tkinter import ttk
import tkinter as tk

def validate_input(char):
    return char.isdigit()

def save_setting(root, pin, money, valid_period, number):
    pin = pin.get()
    money = money.get()
    valid_period = valid_period.get()
    number = number.get()
    if len(pin) != 4 or len(number) != 16 or len(valid_period) != 4:
        error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
        error_label.place(x=10,y=250)

    else:
        if int(valid_period) // 100 > 12 or int(valid_period) // 100 < 1:
            error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
            error_label.place(x=10,y=250)

        else:
            root.destroy()
            create_window()

def create_window():
    window = Tk()
    window.title("ATM")
    window.minsize(1100, 600)
    window.maxsize(1100, 600)
    canvas = Canvas(bg="grey", width=1100, height=600)
    canvas.pack()
    canvas.create_rectangle(850, 200, 1050, 205)
    card = canvas.create_rectangle(860, 210, 1040, 500, fill="green")
    canvas.create_rectangle(50, 10, 700, 350, fill="black")
        
#создаём окно настройки карты
window = Tk()
window.title("card setting")
window.minsize(600, 400)
window.maxsize(600, 400)

#создаём поля ввода и соханяем полученные данные
validate = window.register(validate_input)
pin_label = tk.Label(window, text = "введите пинкод(4 цифры без пробелов)", font=("Arial", 10))
pin_label.place(x = 10, y = 95)
pin_var = tk.StringVar()
pin = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))
pin.place(x = 10,y = 115)
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
save = tk.Button(window, text = "закончить настройку", command = lambda: save_setting(window, pin, money, valid_period, number))
save.place(x = 10,y = 200)
    
    
    
