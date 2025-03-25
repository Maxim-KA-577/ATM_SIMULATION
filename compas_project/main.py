from tkinter import *
from tkinter import ttk
import tkinter as tk
import classes
def validate_input(char):
    return char.isdigit()

def save_setting(root, pan, money, valid_period, number):
    global data
    global assis_data
    
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
            card = classes.Card(card_pan, card_valid_period, card_number, card_money)
            create_window(card)
            data = card_pan
            assis_data = card_money

def create_window(card_for_atm):
    global assis_canv
    
    window = Tk()
    window.title("ATM")
    window.minsize(1000, 500)
    window.maxsize(1000, 500)
    canvas = Canvas(bg="grey", width=1100, height=500)
    canvas.pack()
    assis_canv = canvas
    
    port = canvas.create_rectangle(750, 130, 950, 135)
    screen = canvas.create_rectangle(50, 10, 630, 430, fill="black")
    card_draw = canvas.create_rectangle(760, 140, 940, 430, fill="green")
    
    btn_working = ttk.Button(text = "вставить кату", command = lambda: (refresh(atm, window, canvas, card_for_atm, card_draw, btn_working, text)))
    btn_working.place(x = 810, y = 440)

def start_programm():    
    window = Tk()
    window.title("card setting")
    window.minsize(600, 400)
    window.maxsize(600, 400)
    
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

def refresh(atm = None, window = None, canvas = None, card_for_atm = None, card_draw = None, btn_working = None, text = None):
    condition = atm.get_condition()
    
    if condition == "ATM_WAIT":
        global assis_card_draw
        
        canvas.delete(card_draw)
        card_draw = canvas.create_rectangle(755, 131, 945, 134, fill="green")
        assis_card_draw = card_draw
        btn_working.destroy()
        atm.set_card(card_draw)
        refresh(atm, window)
    elif condition == "ATM_CHECK_PAN" or condition == "ATM_BAD_ATTEMPT":
        global assis_root
        global assis_label
        assis_root = window
        
        assis_label = tk.Label(window, text = "введите пинкод", font=("Arial", 12))
        assis_label.place(x = 260, y = 190)
        window.bind("<KeyPress>", keypressed)

    elif condition == "ATM_GOOD_ATTEMPT":
        window.unbind("<KeyPress>")
        btn_ckeck_balans = ttk.Button(text = "Посмотреть баланс карты", command = lambda: check_balans(atm, btn_ckeck_balans, btn_remove_money, btn_add_money))
        btn_remove_money = ttk.Button(text = "Снять деньги с карты", command = lambda: remove_money(atm, window, btn_ckeck_balans, btn_remove_money, btn_add_money))
        btn_add_money = ttk.Button(text = "Внести деньги на карту", command = lambda: set_money(atm, window, btn_ckeck_balans, btn_remove_money, btn_add_money))

        btn_ckeck_balans.place(x = 250, y = 390)
        btn_remove_money.place(x = 60, y = 390)
        btn_add_money.place(x = 460, y = 390)

    elif condition == "ATM_BLOCK_CARD":
        label_block = tk.Label(window, text = "Карта заблокирована", font = ("Arial", 14))
        label_block.place(x = 260,y = 200)
        canvas.delete(card_draw)

    elif condition == "ATM_CHECK_BAlANS":
        global assis_data
        
        label = tk.Label(window, text = "Ваш баланс:" + str(assis_data), font=("Arial", 14))
        btn_end = ttk.Button(window, text = "Закончить работу с банкоматом", command = lambda: end(btn_end,label))

        btn_end.place(x = 250, y = 390)
        label.place(x = 260, y = 190)

    elif condition == "ATM_GOOD_SUM":
        global assis_balans
        
        label = tk.Label(window, text = f"На карте осталось: {str(assis_balans)} рублей", font=("Arial", 14))
        btn_end = ttk.Button(window, text = "Закончить работу с банкоматом", command = lambda: end(btn_end,label))

        label.place(x = 200, y = 190)
        btn_end.place(x = 250, y = 390)

    elif condition == "ATM_GOOD_SET":
        global assis_balans_set
        label = tk.Label(window, text = f"Денег на карте: {assis_balans_set}", font=("Arial", 14))
        btn_end = ttk.Button(window, text = "Закончить работу с банкоматом", command = lambda: end(btn_end,label))

        label.place(x = 260, y = 190)
        btn_end.place(x = 250, y = 390)

def set_money(atm, window, btn1, btn2, btn3):
    global assis_set
    
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()

    label = tk.Label(window, text = "Введите сумму которую хотите внести", font = ("Arial", 12))
    btn_set = ttk.Button(window, text = "внести деньги на карту", command = lambda: check_set(atm, btn_set))
    assis_set = label
    
    btn_set.place(x = 240, y = 260)
    label.place(x = 190, y = 190)
    window.bind("<KeyPress>", keypressed_for_work)

def check_set(atm, btn):
    global text
    global assis_set
    global assis_remove
    global assis_balans_set
    global assis_root
    
    atm.set_money(int(text))
    if atm.condition == "ATM_GOOD_SET":
        assis_balans_set = assis_data + int(text)
        btn.destroy()
        assis_set.destroy()
        assis_remove.destroy()
        refresh(atm, assis_root)

def end(btn, label):
    global assis_root

    btn.destroy()
    label.destroy()
    
    btn_get_card = ttk.Button(assis_root, text = "забрать карту", command = lambda: get_card(btn_get_card))

    btn_get_card.place(x = 810, y = 90)
    
def get_card(btn):
    global assis_card_draw
    global assis_canv

    btn.destroy()
    
    assis_canv.delete(assis_card_draw)
    
def remove_money(atm, window, btn1, btn2, btn3):
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()

    label = tk.Label(window, text = "введите сумму (кратную 100)", font = ("Arial", 12))
    btn_remove = ttk.Button(window, text = "снять деньги с карты", command = lambda: check_remove(atm, btn_remove, label))

    label.place(x = 240, y = 200)
    btn_remove.place(x = 240, y = 260)

    window.bind("<KeyPress>", keypressed_for_work)

def check_remove(atm, btn, label):
    global text
    global assis_remove
    global assis_data
    global assis_balans

    try:
        if int(text) <= assis_data:
            atm.get_money(int(text))

        if atm.condition == "ATM_GOOD_SUM":
            assis_balans = assis_data - int(text)
            atm.money -= int(text)
            btn.destroy()
            label.destroy()
            assis_remove.destroy()
            refresh(atm)
    except:
        pass

def keypressed_for_work(event):
    global text
    
    if event.keycode in range(48, 58):  
        symbol = str(event.keycode - 48)
        text += symbol

    if len(text) == 9:
        text = text[1:]

    draw_text(text)

def draw_text(text):
    global assis_root
    global assis_remove

    if assis_remove is not None:
        assis_remove.destroy()
    
    assis_remove = tk.Label(assis_root, text = text, font = ("Arial", 10))
    assis_remove.place(x = 260, y = 230)
    
def check_balans(atm, btn1, btn2, btn3):
    atm.check_balans()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    refresh(atm)

def check_pan(assis_root):
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

        print(data)
        print(atm.condition)
        print(text)

        attempt += 1
        text = ""
        hidden_text = ""
        
def keypressed(event):
    global text
    global hidden_text
    global assis_hidden_label
    
    if event.keycode in range(48, 58):  
        symbol = str(event.keycode - 48)
        text += symbol
        hidden_text += "*"

        if assis_hidden_label is not None:
            assis_hidden_label.destroy()
            
        pan_label = tk.Label(assis_root, text=hidden_text, font=("Arial", 12))
        pan_label.place(x=310, y=220)
        assis_hidden_label = pan_label
        
        check_pan(assis_root)

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
assis_data = None
assis_remove = None
assis_set = None
assis_balans_set = None

start_programm()
