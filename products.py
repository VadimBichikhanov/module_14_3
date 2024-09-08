from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
import logging
from os import path

async def get_buying_list(message: Message):
    products = [
        {"name": "Apple", "description": "Свежее яблоко", "price": 100, "image": "images/apple.jpg"},
        {"name": "Banana", "description": "Спелый банан", "price": 200, "image": "images/banana.jpg"},
        {"name": "Orange", "description": "Апельсин", "price": 300, "image": "images/orange.jpg"},
        {"name": "Grapes", "description": "Виноград", "price": 400, "image": "images/grapes.jpg"}
    ]

    for product in products:
        await message.answer(f"Название: {product['name']} | Описание: {product['description']} | Цена: {product['price']}")
        # Отправка картинки для каждого продукта
        image_path = product['image']
        if path.exists(image_path):
            logging.info(f"Отправка изображения: {image_path}")
            await message.answer_photo(photo=FSInputFile(path=image_path))
        else:
            logging.error(f"Изображение для продукта {product['name']} не найдено: {image_path}")
            await message.answer(f"Изображение для продукта {product['name']} не найдено.")

    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Apple", callback_data="buy_apple")],
            [InlineKeyboardButton(text="Banana", callback_data="buy_banana")],
            [InlineKeyboardButton(text="Orange", callback_data="buy_orange")],
            [InlineKeyboardButton(text="Grapes", callback_data="buy_grapes")]
        ]
    )
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)