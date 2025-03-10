class ATM():
    def __init__(self, money, card = None):
        self.money = money
        self.condition = "ATM_WAIT"
        
    def set_card(self, card):
        if card != None:
            self.card = card
            self.condition = "ATM_CHECK_PAN"
        
    def check_pan(self, attempt, data):
        if attempt != 3:
            if card.card_pan == data:
                self.condition = "ATM_GOOD_ATTEMPT"
            else:
                self.condition = "ATM_BAD_ATTEMPT"
        else:
            self.condition = "ATM_BLOCK_CARD"
        return self.condition

    def add_money_to_ATM(self, money):
        if money % 100 != 0:
            self.condition = "ATM_BAD_SUM"
        else:
            self.condition = "ATM_GOOD_SUM"
            self.money += money
        return self.condition

    def remove_money_from_ATM(self, money):
        if money % 100 != 0:
            self.condition = "ATM_NO_SET"
        else:
            if money >= 1000000:
                self.condition = "ATM_NO_SUM"
            else:
                self.condition = "ATW_GOOD_SET"
                self.money -= money
        return self.condition

    def remvoe_money_to_card(self, money):  
        self.condition = remove_money_from_ATM(money)                       
        if self.condition == "ATW_GOOD_SET":
            self.card.money -= money
            self.condition = "ATM_CARD_GOOD"
        elif self.condition == "ATM_NO_SUM" or self.condition == "ATM_NO_SET":
            self.condition = "ATM_BAD_SET"
        return self.condition

    def remove_money_from_card(self, money):
        self.condition == add_money_to_ATM(money)
        if self.condition == "ATM_GOOD_SUM":
            self.money += money
            self.card.money += money
            self.condition = "ATM_GOOD_GET"
        elif self.condition == "ATM_BAD_SUM":
            self.condition = "ATM_NO_GET"
        return self.condition

    def check_balans(self, card_money):
        self.condition = "ATM_CHECK_BAlANS"

    def get_condition(self):
        return self.condition

class Card():
    def __init__(self, money, pan):
        self.money = money
        self.card_pan = pan



"""
card = Card(1000, "1234")
atm = ATM(100000, card)

while True: 
    if atm.get_condition() == "ATM_WAIT":
        if input("вставить карту") == "+":
            atm.set_card(card)
    elif atm.get_condition() == "ATM_CHECK_PAN":
        attemps = 0
        while attemps != 3:
            condition = atm.check_pan(attemps, input("Введите пан"))
            if condition == "ATM_GOOD_ATTEMPT":
                print("good")
                break
            elif condition == "ATM_BAD_ATTEMPT":
                print("bad")
                attemps+=1
            if attemps == 3:
                print("block")
                break
"""
