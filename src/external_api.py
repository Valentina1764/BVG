import os
from dotenv import load_dotenv
import requests


def converter_currency(transaction: dict) -> float:
    """Функция конвертации валют с помощью внешнего API"""
    load_dotenv()

    apilayer_token = os.getenv("APILAYER_KEY")

    if not apilayer_token:
        raise ValueError("API token не найден.")

    headers = {"apikey": apilayer_token}

    if transaction["operationAmount"]["currency"]["code"] == "USD":
        amount_in_currency = transaction["operationAmount"]["amount"]
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount_in_currency}",
            headers=headers,
        )

        if response.status_code != 200:
            raise Exception(f"Запрос не выполнен, код ошибки: {response.status_code}")

        result = response.json()["result"]
        return result

    elif transaction["operationAmount"]["currency"]["code"] == "EUR":
        amount_in_currency = transaction["operationAmount"]["amount"]
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount_in_currency}",
            headers=headers,
        )

        if response.status_code != 200:
            raise Exception(f"Запрос не выполнен, код ошибки: {response.status_code}")

        result = response.json()["result"]
        return result

    else:
        raise Exception("Не корректный код валюты.")
