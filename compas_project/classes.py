class ATM():
    def __init__(self, money, card = None):
        self.money = money
        self.condition = "ATM_WAIT"
        self.card = card
        
    def set_card(self, card):
        self.condition = "ATM_CHECK_PAN"
        return self.condition
        
    def check_pan(self, attempt, data, text):
        if attempt != 3:
            if text == data:
                self.condition = "ATM_GOOD_ATTEMPT"
            else:
                self.condition = "ATM_BAD_ATTEMPT"
        if attempt == 3:
            if text == data:
                self.condition = "ATM_GOOD_ATTEMPT"

            else:
                self.condition = "ATM_BLOCK_CARD"
        return self.condition

    def get_money(self, money):
        if money % 100 == 0 and money <= self.money:
            self.condition = "ATM_GOOD_SUM"

    def set_money(self, money):
        if money % 100 == 0:
            self.condition = "ATM_GOOD_SET"

    def check_balans(self):
        self.condition = "ATM_CHECK_BAlANS" 

    def get_condition(self):
        return self.condition

class Card():
    def __init__(self, card_pan, card_valid_period, card_number, card_money):
        self.card_money = card_money
        self.card_pan = card_pan
        self.card_valid_period = card_valid_period
        self.card_number = card_number
