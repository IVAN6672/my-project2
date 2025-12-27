import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, InputMediaPhoto
TOKEN = "8413883797:AAGJ9ZS1gTk1cQeDbxfEPXt4-SBhvgWr8wA"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"""Привет, {message.from_user.first_name}! 🌍
Я бот, посвященный проблеме глобального потепления.
Доступные команды:
/info - что происходит с климатом
/weather - наглядные последствия
/tips - как ты можешь помочь""")
@dp.message(Command("info"))
async def info_handler(message: types.Message):
    await message.answer("""🌡️ Глобальное потепление — это долгосрочное повышение средней температуры Земли.
Основные причины:
• Сжигание угля, нефти и газа
• Вырубка лесов
• Сельское хозяйство (метан)
Это приводит к таянию ледников, повышению уровня океана и экстремальной жаре.""")
@dp.message(Command("weather"))
async def photos_handler(message: types.Message):
    await message.answer("Собираю фотографии последствий...")
    file_names = ["photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg"]
    media_group = []
    for name in file_names:
        file_path = os.path.join("photos", name)
        if os.path.exists(file_path):
            media_group.append(InputMediaPhoto(media=FSInputFile(file_path)))
        else:
            print(f"Файл {file_path} не найден!")
    if media_group:
        try:
            await message.answer_media_group(media=media_group)
        except:
            await message.answer("Ошибка при отправке альбома.")
    else:
        await message.answer("Папка 'photos' пуста или файлы названы неверно.")
@dp.message(Command("tips"))
async def tips_handler(message: types.Message):
    await message.answer("""🌱 Что можешь сделать ты?
1. Энергия: выключай свет и приборы
2. Транспорт: ходи пешком или на велосипеде
3. Покупки: меньше лишних вещей, меньше пластика
4. Еда: выбрасывай меньше продуктов""")
async def main():
    print("Бот запущен и готов!")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
