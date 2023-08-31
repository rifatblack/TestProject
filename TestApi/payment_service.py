

class PaymentService:
    def process_payment(self, amount, card_number, expiry_date, cvv):
        # we can replace this with a real payment gateway integration
        if len(card_number) == 16 and cvv == '123':
            return True
        return False

    def subscribe(self, user, plan):
        # we can replace this with a real subscription logic
        if plan == 'premium':
            user.is_premium_member = True
            user.save()
