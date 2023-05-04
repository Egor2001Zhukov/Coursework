import json
from _datetime import datetime


def load_jsonfile(filename: str):
    with open(filename, "r") as file:
        return json.load(file)


def score_modulation(text: str):
    if text:
        score_or_cart = text.split()
        if score_or_cart[0] == "Счет":
            s = f"**{text.split()[-1][-4:]}"
            score = f"{''.join(score_or_cart[0:-1])} {s}"
        else:
            score = f'{" ".join(score_or_cart[0:-1])} ' \
                    f'{text.split()[-1][0:4]} ' \
                    f'{text.split()[-1][4:6]}** **** ' \
                    f'{text.split()[-1][12:16]}'
    else:
        score = ""
    return score


def last_five_operations(operations: list):
    count = 5
    new_list =[]
    last_five = []
    [new_list.append(i) for i in operations if i != {}]
    new_list.sort(
        key=lambda y: datetime.strptime(y['date'], "%Y-%m-%dT%H:%M:%S.%f") if y.get('date') else datetime.min,
        reverse=True)
    if len(new_list) < 5:
        count = len(new_list)
    for x in range(0, count):
        date = datetime.strftime(datetime.strptime(new_list[x].get('date'),
                                                   "%Y-%m-%dT%H:%M:%S.%f").date(), "%d.%m.%Y")

        description = new_list[x].get('description')

        if new_list[x].get("from"):
            score_from = f'{score_modulation(new_list[x].get("from"))} -> '
        else:
            score_from = ""

        score_to = score_modulation(new_list[x].get('to'))

        bablishko = f"{new_list[x].get('operationAmount').get('amount')} " \
                    f"{new_list[x].get('operationAmount').get('currency').get('name')}"

        last_five.append(f"{date} {description}\n"
                         f"{score_from}{score_to}\n"
                         f"{bablishko}\n\n")
    return "".join(last_five)

