from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if not entered_code is correct_code:
        return False

    current_date = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date = datetime.strptime(expiration_date, "%B %d, %Y")

    return current_date <= expiration_date