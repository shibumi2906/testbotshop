# bot/services/payment_gateway.py
import requests

# Данные для интеграции с Юкасса
YOOKASSA_API_URL = "https://api.yookassa.ru/v3/payments"
SHOP_ID = "your_shop_id"  # Замените на ваш идентификатор магазина
API_KEY = "your_api_key"  # Замените на ваш секретный ключ


# Функция для создания платежа в Юкасса
def create_payment(amount: float, currency: str = "RUB", description: str = "Оплата заказа",
                   redirect_url: str = "https://your-bot-redirect-url.com/payment-success"):
    # Тело запроса к API Юкасса
    data = {
        "amount": {
            "value": f"{amount:.2f}",
            "currency": currency
        },
        "confirmation": {
            "type": "redirect",
            "return_url": redirect_url
        },
        "capture": True,
        "description": description
    }
    # Выполнение POST-запроса к API Юкасса
    response = requests.post(
        YOOKASSA_API_URL,
        json=data,
        auth=(SHOP_ID, API_KEY)  # Аутентификация через SHOP_ID и секретный API-ключ
    )

    # Проверка ответа от сервера
    if response.status_code == 200:
        payment_info = response.json()
        return payment_info.get("confirmation", {}).get("confirmation_url")
    else:
        print(f"Ошибка создания платежа: {response.status_code} - {response.text}")
        return None


# Пример использования в обработчике
async def process_payment(message, amount: float):
    payment_url = create_payment(amount)
    if payment_url:
        await message.reply(f"Оплата создана. Перейдите по ссылке для завершения: {payment_url}")
    else:
        await message.reply("Ошибка создания платежа. Попробуйте позже.")
