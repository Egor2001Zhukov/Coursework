import pytest

from utils.functions import score_modulation, load_jsonfile, last_five_operations


@pytest.mark.parametrize("text, answer", [("Счет 84163357546688983493", "Счет **3493"),
                                          ("Maestro 7810460011115568", "Maestro 7810 46** **** 5568"),
                                          ("", "")])
def test_score_modulation(text, answer):
    assert score_modulation(text) == answer


@pytest.mark.parametrize("filename, answer", [("operations.json", list)])
def test_load_jsonfile(filename, answer):
    assert type(load_jsonfile(filename)) == answer


@pytest.mark.parametrize("operations, answer", [([{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }],
    "30.06.2018 Перевод организации\n"
    "Счет **6952 -> Счет **6702\n"
    "9824.07 USD\n\n"
    "23.03.2018 Открытие вклада\n"
    "Счет **2431\n"
    "48223.05 руб.\n\n")])
def test_last_five_operations(operations, answer):
    assert last_five_operations(operations) == answer
