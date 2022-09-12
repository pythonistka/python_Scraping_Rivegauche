from config import tg_bot_token
import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(f"Привет!\n"
                        "Напиши мне название парфюма и я пришлю тебе о нем информацию из магазина Рив Гош ;)")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        with open('total_result.json', encoding='utf-8') as f:
            content = json.load(f)
            result = content[message.text]
            link = result["product_link"]
            sale = result["product_price_sale"]
            price = result["product_price_base"]
            price_sale = result["product_price"]

        await message.reply(f"Первоначальная цена: {price} руб.\n"
                            f"Цена со скидкой: {price_sale} руб.\n"
                            f"Размер скидки: {sale}\n"
                            f"Ссылка на сайте: {link}\n"
                            )

    except:
        await message.reply("\U00002620 Проверьте название парфюма")


if __name__ == '__main__':
    executor.start_polling(dp)
