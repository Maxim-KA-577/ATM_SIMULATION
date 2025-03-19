class ATM():
    def __init__(self, money, card = None):
        self.money = money
        self.condition = "ATM_WAIT"
        self.card = card
        
    def set_card(self, card):
        if card != None:
            self.condition = "ATM_CHECK_PAN"
        return self.condition
        
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
    def __init__(self, card_pan, card_valid_period, card_number, card_money):
        self.card_money = card_money
        self.card_pan = card_pan
        self.card_valid_period = card_valid_period
        self.card_number = card_number
