class CreditCard(object):
    def __init__(self, credit_card_type, card_number, expiration_date, cardholder_name, security_code):
        self.credit_card_type = credit_card_type
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cardholder_name = cardholder_name
        self.security_code = security_code
