#import logging

# logging.basicConfig(
#     filename="./logs/masks.log",
#     filemode="w",
#     encoding="UTF-8",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )


def get_mask_card_number(loc_number_card: str) -> str:
    """
    Функция возвращает замаскированный номер карты
    """
    try:
        if len(loc_number_card) != 16:
            raise ValueError("Ошибка ввода номера карты. Ожидается 16 цифр. Попробуйте еще раз")

        # logging.info(f"Запуск программы маскирования номера банковской карты")
        masked_card = f"{loc_number_card[:4]} {loc_number_card[4:6]}** **** {loc_number_card[-4:]}"
        # logging.info(f"Маскированный номер карты: {masked_card}")
        return masked_card

    except Exception as e:
        # logging.error(f"Произошла ошибка при маскировании номера карты: {e}")
        raise


def get_mask_account(loc_number_account: str) -> str:
    """
    Функция возвращает замаскированный номер счета
    """
    try:
        if len(loc_number_account) != 20:
            raise ValueError("Ошибка ввода номера счета. Ожидается 20 цифр. Попробуйте еще раз")

        # logging.info(f"Запуск программы маскирования номера банковского счета")
        masked_account = f"**{loc_number_account[-4:]}"
        # logging.info(f"Маскированный номер счета: {masked_account}")
        return masked_account

    except Exception as e:
        # logging.error(f"Произошла ошибка при маскировании номера счета: {e}")
        raise
