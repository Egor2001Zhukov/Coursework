import json
from _datetime import datetime


def score_modulation(text):
    if text:
        score_or_cart = text.split()
        if score_or_cart[0] == "Счет":
            s = f"**{text.split()[-1][12:16]}"
            score = f"Счет {s}"
        else:
            score = f'{" ".join(score_or_cart[0:-1])} ' \
                    f'{text.split()[-1][0:4]} ' \
                    f'{text.split()[-1][5:7]}** **** ' \
                    f'{text.split()[-1][12:16]}'
    else:
        score = ""
    return score
