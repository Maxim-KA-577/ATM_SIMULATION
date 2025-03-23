from tkinter import *
from tkinter import ttk
import tkinter as tk
import classes  # Убедитесь, что этот модуль доступен и правильно импортирован
def validate_input(char):
    return char.isdigit()

def save_setting(root  #""", pan, money, valid_period, number"""
                 ):
    global data
    """
    card_pan = pan.get()
    card_money = money.get()
    card_valid_period = valid_period.get()
    card_number = number.get()
    """
    card_pan = 1111
    card_money = 1000
    card_valid_period = 1111
    card_number = 1111111111111111
    if len(str(card_pan)) != 4 or len(str(card_number)) != 16 or len(str(card_valid_period)) != 4:
        error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
        error_label.place(x=10,y=250)   

    else:
        if int(card_valid_period) // 100 > 12 or int(card_valid_period) // 100 < 1:
            error_label = tk.Label(root, text = "Данные введены не правильно", font=("Arial", 20))
            error_label.place(x=10,y=250)

        else:
            root.destroy()
            card = classes.Card(card_pan, card_valid_period, card_number, card_money)
            create_window(card)
            data = card_pan

def create_window(card_for_atm):
    global assis_canv
    
    window = Tk()
    window.title("ATM")
    window.minsize(1100, 500)
    window.maxsize(1100, 500)
    canvas = Canvas(bg="grey", width=1100, height=500)
    canvas.pack()
    assis_canv = canvas
    
    port = canvas.create_rectangle(850, 130, 1050, 135)
    screen = canvas.create_rectangle(50, 10, 730, 430, fill="black")
    card_draw = canvas.create_rectangle(860, 140, 1040, 430, fill="green")
    
    btn_working = ttk.Button(text = "вставить кату", command = lambda: (refresh(atm, window, canvas, card_for_atm, card_draw, btn_working, text)))
    btn_working.place(x = 910, y = 440)

def start_programm():    
    window = Tk()
    window.title("card setting")
    window.minsize(600, 400)
    window.maxsize(600, 400)
    """
    validate = window.register(v alidate_input)
    
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
    """
    save = tk.Button(window, text = "закончить настройку", command = lambda: save_setting(window #""", pan, money, valid_period,
                                                                                          ))
    save.place(x = 10,y = 200)

def refresh(atm = None, window = None, canvas = None, card_for_atm = None, card_draw = None, btn_working = None, text = None):
    condition = atm.get_condition()
    
    if condition == "ATM_WAIT":
        global assis_card_draw
        
        canvas.delete(card_draw)
        card_draw = canvas.create_rectangle(855, 131, 1045, 134, fill="green")
        assis_card_draw = card_draw
        btn_working.destroy()
        atm.set_card(card_draw)
        refresh(atm, window)
    elif condition == "ATM_CHECK_PAN" or condition == "ATM_BAD_ATTEMPT":
        global assis_root
        global assis_label
        assis_root = window
        
        assis_label = tk.Label(window, text = "введите пинкод", font=("Arial", 12))
        assis_label.place(x = 310, y = 190)
        window.bind("<KeyPress>", keypressed)

    elif condition == "ATM_GOOD_ATTEMPT":
        window.unbind("<KeyPress>")
        

    elif condition == "ATM_BLOCK_CARD":
        label_block = tk.Label(window, text = "Карта заблокирована", font = ("Arial", 14))
        label_block.place(x = 310,y = 200)
        canvas.delete(card_draw)


def check_pan(assis_root, a):
    global text
    global hidden_text
    global attempt
    global data
    
    if len(text) == 4:
        global assis_canv
        global assis_label
        global assis_hidden_label
        global assis_card_draw
        
        atm.check_pan(attempt, data, int(text))
        print(atm.condition)

        if atm.condition == "ATM_GOOD_ATTEMPT":
            assis_label.destroy()
            assis_hidden_label.destroy()
            refresh(atm, assis_root, assis_canv)
        elif atm.condition == "ATM_BLOCK_CARD":
            assis_label.destroy()
            assis_hidden_label.destroy()
            refresh(atm, assis_root, assis_canv, None, assis_card_draw)
        elif atm.condition == "ATM_BAD_ATTEMPT":
            assis_label.destroy()
            assis_hidden_label.destroy()
            refresh(atm, assis_root)

        attempt += 1
        text = ""
        hidden_text = ""
        
def keypressed(event):
    global text
    global hidden_text
    global assis_hidden_label
    
    if event.keycode in range(48, 58):  
        digit = str(event.keycode - 48)
        text += digit
        hidden_text += "*"

        if assis_hidden_label is not None:
            assis_hidden_label.destroy()
            
        pan_label = tk.Label(assis_root, text=hidden_text, font=("Arial", 12))
        pan_label.place(x=310, y=220)
        assis_hidden_label = pan_label
        
        check_pan(assis_root, assis_canv)

atm = classes.ATM(1000000)
text = ""
hidden_text = ""
attempt = 1
data = None
assis_root = None
assis_canv = None
assis_label = None
assis_hidden_label = None
assis_card_draw = None

start_programm()
