from Utils.percent_cheking_util import check_five_percent


def count_difference(yest_num, bef_yest_num):
    absolute_difference = abs(yest_num - bef_yest_num)
    five_percent_yest = check_five_percent(yest_num)

    if absolute_difference >= five_percent_yest:
        print("The difference between two days is more or equals to five percent")
        return True
    else:
        return False
