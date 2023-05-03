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


def main():
    last_five = []
    with open("operations.json", "r") as file:
        operations = json.load(file)
        operations.sort(
            key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f") if x.get('date') else datetime.min,
            reverse=True)
        for x in range(0, 5):
            date = datetime.strftime(datetime.strptime(operations[x].get('date'),
                                                       "%Y-%m-%dT%H:%M:%S.%f").date(), "%d.%m.%Y")
            description = operations[x].get('description')
            if operations[x].get("from"):
                score_from = f'{score_modulation(operations[x].get("from"))} -> '
            else:
                score_from = ""
            score_to = score_modulation(operations[x].get('to'))
            bablishko = f"{operations[x].get('operationAmount').get('amount')} " \
                        f"{operations[x].get('operationAmount').get('currency').get('name')}"
            last_five.append(f"{date} {description}\n"
                             f"{score_from}{score_to}\n"
                             f"{bablishko}\n\n")
        return "".join(last_five)


if __name__ == '__main__':
    print(main())
