def nbMonths(price_old, price_new, saving_per_month, percent_loss_by_month):
    savings_total = price_old
    months_to_save = 0

    while savings_total < price_new:
        months_to_save += 1

        if months_to_save % 2 == 0:
            percent_loss_by_month += 0.5

        savings_total += saving_per_month - price_old * (percent_loss_by_month / 100)
        price_old *= 1 - (percent_loss_by_month / 100)
        price_new *= 1 - (percent_loss_by_month / 100)

    return [months_to_save, round(savings_total - price_new)]