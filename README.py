import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command, Text

# Token va kanal ID'larining ro'yxati
BOT_TOKEN = '7569521007:AAElsUyoMXtLCIMxflICi_8nnluhM48enng'
PROXY_URL = "http://proxy.server:3128"

# Tekshiriladigan kanallar ro'yxati
CHANNEL_IDS = [
    {"id": "-1002389116755", "url": "https://t.me/kinomt","name": "Kanalat 1"},  # Kanal 1
    {"id": "-1002443890726", "url": "https://t.me/+pW5eQNfXUUwyZWYx"}  # Kanal 2
]

# Tekshirilmaydigan kanallar ro'yxati
EXCLUDED_CHANNELS = [
    {"id": "-1001234567890", "url": "https://t.me/+tngRrVg11Xg0M2Ux"},
    {"id": "-1001234567890", "url": "https://instagram.com/kinomtv"} # Kanal 5 (faqat ko'rinadi)
]

# Video File ID
VIDEO_FILE_ID = "BAACAgIAAxkBAAIBPWdjElqzwpcrga50kKIYM1WJ0mllAAKzTgACs-soS6Ucv1bivKZLNgQ"  # O'zingizning video ID'nizni qo'ying

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=BOT_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)

# Foydalanuvchi obuna holatini tekshiruvchi funksiya
async def check_subscription(user_id):
    not_subscribed_channels = []  # Foydalanuvchi obuna bo'lmagan kanallar ro'yxati
    for channel in CHANNEL_IDS:  # Faqat tekshiriladigan kanallarni ko'rib chiqamiz
        check_sub_channel = await bot.get_chat_member(chat_id=channel["id"], user_id=user_id)
        if check_sub_channel.status == "left":
            not_subscribed_channels.append(channel)
    return not_subscribed_channels

# /start komanda uchun handler
@dp.message_handler(Command("start"))
async def send_welcome(message: Message):
    not_subscribed_channels = await check_subscription(message.from_user.id)
    if not not_subscribed_channels:
        await message.answer("✅ Botdan foydalanish mumkin!")
    else:
        all_channels = not_subscribed_channels + EXCLUDED_CHANNELS
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=" Kanal",
                        url=channel["url"]
                    )
                ] for channel in all_channels
            ] + [
                [
                    InlineKeyboardButton(
                        text="✅ A'zo bo'ldim ✅",
                        callback_data="azo"
                    )
                ]
            ],
            row_width=1
        )
        await message.answer(
            "⬇️ <b>Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling</b> ⬇️",
            reply_markup=keyboard,
            parse_mode='HTML'
        )

# Callback query uchun handler
@dp.callback_query_handler(Text(equals="azo"))
async def callback_subscribe(callback_query: CallbackQuery):
    not_subscribed_channels = await check_subscription(callback_query.from_user.id)
    if not not_subscribed_channels:
        await callback_query.message.answer("✅ Botdan foydalanishingiz mumkin! ")
    else:
        all_channels = not_subscribed_channels + EXCLUDED_CHANNELS
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="❓ Kanalga a'zo bo'lish",
                        url=channel["url"]
                    )
                ] for channel in all_channels
            ] + [
                [
                    InlineKeyboardButton(
                        text="✅ A'zo bo'ldim ✅",
                        callback_data="azo"
                    )
                ]
            ],
            row_width=1
        )
        await callback_query.message.reply(
            "❌ Kanalarga A'zo bo'lmadingiz, qayta urinib ko'ring! ❌",
            reply_markup=keyboard
        )

# Har qanday xabar uchun handler
@dp.message_handler()
async def handle_message(message: Message):
    # Foydalanuvchi kanalga a'zo bo'lmasa
    not_subscribed_channels = await check_subscription(message.from_user.id)
    if not not_subscribed_channels:
        # Kanalga a'zo bo'lgan bo'lsa, buyruqlarni qabul qilish
        if message.text == "34":
            await message.answer("segt")
        elif message.text == "39":
            await message.answer("se55gt")
        elif message.text == "35":
            await message.answer("solom")
        elif message.text == "36":
            await message.answer("senmi")
        elif message.text == "23":
            await message.answer_video(
                video="BAACAgIAAxkBAANuZ2Ltl02bqIVVAhl9aQvEFxDy7NgAApppAALH4dhKU0O1_wFg8-c2BA",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "24":
            await message.answer_video(
                video="BAACAgQAAxkBAAIBDWdi_czxs-BTPOaxSSN2i1KpfGedAAI1EgACfeQYU8W4lFJ3y7rcNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "592":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBK2djDpGhwk2yxFSnSKS8kwXPCoarAAKOVwAC1uL5SrgeedTfDAouNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "561":
            await message.answer_video(
                video="BAACAgQAAxkBAAIBLWdjDwvgEseMlgXbr8Xe_PKNdLpLAAKwEwAC-6L4U0MXfSQ5n94MNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "554":
            await message.answer_video(
                video="BAACAgQAAxkBAAIBL2djD4L4QEi5ZnHKZ-wyqutd_z1HAAISFQACmRj4USKgcJ_Hp498NgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "541":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBMWdjD-4tH7JnAgcynQX7WUEEpmIUAAJ4XQACSSEJShCYoSGjP2BWNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "548":
            await message.answer_video(
                video="BAACAgQAAxkBAAIBM2djEFRP5q1K3W4E2i2N6vxfCGgGAALDFAACdW44U3zjIMet7JGENgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "535":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBNWdjEODPzkcSJpP68nW9UGmpiq2WAAJVXwAC5Bs4Svd0XOs2t110NgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "348":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBN2djEVtIVBEo4wOYtQt151wUaeCBAAJ8UAACKtJASiPwRowP4qgxNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "497":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBOWdjEa_Mbr0IE7KdSDSOK-6i04mvAAIVXgAC4HQRSF71TkOiILa2NgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "496":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBO2djEf2Di_eHYLw-aeACI8mK5s0OAAKqWwACHWWQSdMvBUe6SaZHNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "485":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBPWdjElqzwpcrga50kKIYM1WJ0mllAAKzTgACs-soS6Ucv1bivKZLNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "464":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBP2djEqMzPTCxs4mSJ_kgynT7-296AAL6VAACcVeRS_d6SHFzYonMNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "439":
            await message.answer_video(
                video="BAACAgIAAxkBAAIBoGdj7IDLunMGkL6XpGNJUH6tate3AAJHXQACX0-4SlLgIt2gfR1BNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "456":
            await message.answer_video(
                video="BAACAgQAAxkBAAIBomdj7-63Bk4Xh7eTizF9zPB4b5-CAALoFQACD-J4Ubsfk1ZrjoRbNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "556":
             await message.answer_video(
                video="BAACAgQAAxkBAAIBomdj7-63Bk4Xh7eTizF9zPB4b5-CAALoFQACD-J4Ubsfk1ZrjoRbNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "600":
            await message.answer_video(
        video="BAACAgIAAxkBAAIGcmdo3ooEuH6XhBnGGM6UhOHgnAR0AALcXwACWO0RSzRR9jHZfaBgNgQ",
        caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
    )
        elif message.text == "602":
            await message.answer_video(
                video="BAACAgQAAxkBAAIGdGdo3r-Tlt3U56-4B4DC0kpTs186AALDFgACUTbBUjLqBJ5JudAgNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "604":
            await message.answer_video(
                video="BAACAgIAAxkBAAIGdmdo3sYSqb9nz9UAATtEw6ibNwyUjAACW1sAAsILgUomMfxywPkv2zYE",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "606":
            await message.answer_video(
                video="BAACAgIAAxkBAAIGeGdo3s0vLQtpP4wrwukX3Wu0oQABgwACgWQAArArMUohmE5hHkBUXjYE",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "608":
            await message.answer_video(
                video="BAACAgIAAxkBAAIGemdo3yH865_gVH8h-GPLaaXfn7q0AAI1WwAChVMQS_V7jkiowk0FNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "610":
            await message.answer_video(
                video="BAACAgIAAxkBAAIGfGdo30bMq4mJtaPMDnzzcH8_Yj7XAAIzUwACaW_ISqoJQg2daLuqNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "612":
            await message.answer_video(
                video="BAACAgIAAxkBAAIGfmdo30x6M3PbHlHzyRF1Y6M-7AddAAKrWwACr1GBSsahXaNJwlpuNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "614":
            await message.answer_video(
                video="BAACAgIAAxkBAAIGhGdo3-ZD6BEJ17KqkgjYmwU7Rj6fAAKxYwACFBNIS7PNxhDdu_i3NgQ",
                caption="Deha 1080p \n\n Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "616":
            await message.answer_video(
                video="BAACAgIAAxkBAAIGgGdo31BiP_p4CB20Qzp_yAGWNXJmAAK6UQACsCs5SmltDgZ5MEmNNgQ",
                caption="Deha 1080p \n\n Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "618":
            await message.answer_video(
                video="BAACAgIAAxkBAAIJ5WduWp4r1I83mp_uuKAWOoj1qTkjAALhWgAC8KJgS9zjXE054JIUNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "620":
            await message.answer_video(
                video="BAACAgIAAxkBAAIJ7GduXJPtZz3zsOPSawwnBQNO1AmmAAKAXgACuBtZS_t0MnW85IkgNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "770":
            await message.answer_video(
                video="BAACAgIAAxkBAAIEsGdlk5h0T_zFkVwalqVObR2HZTKuAAJqIgAC_ZX4SsIRMLtWAAFIqDYE",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "772":
            await message.answer_video(
                video="BAACAgQAAxkBAAIEsmdllH8qEurhsi-NbllgkD4W4xaVAAJbEAACTsiIUnHFDRN2D9f1NgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "774":
            await message.answer_video(
                video="BAACAgEAAxkBAAIEtGdllSqxVn_VFu10qbU-QyjK96dgAAITAwACYeg5RiJZED09DGrGNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "776":
            await message.answer_video(
                video="BAACAgEAAxkBAAIEtmdllZ4EZz3IxlhuUp-ByKNqZV40AAIkAQACq1MRRrWheAhDD0qaNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "778":
            await message.answer_video(
                video="BAACAgQAAxkBAAIEuGdllf-OeTwECZ7GVWyLH1m-eRIvAALHEQACIbbAUsb6JQzpnb84NgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "780":
            await message.answer_video(
                video="BAACAgQAAxkBAAIEumdll4emCtTDVey9t9SHzrb56SvFAAJ2DwAC9mrYU3SE7TzGL8VrNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "782":
            await message.answer_video(
                video="BAACAgIAAxkBAAIEvmdlm2Ut_T30135WIjgTsG3nOI-GAAKnWwACPlMoS1heUcLtJ80uNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "784":
            await message.answer_video(
                video="BAACAgIAAxkBAAIEwGdlqU8maQoPATfXudDIydT2Qi4xAAKYbQAC3hzZSpb-gbany9shNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "786":
            await message.answer_video(
                video="BAACAgQAAxkBAAIFEmdmiUxSlP0Xk8kHgHqDxWbB4JymAAJ8EQAC1ScBU9MMw1GKIxjWNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "788":
            await message.answer_video(
                video="BAACAgIAAxkBAAIFFGdmig2qvvw7e2IFB0yLAR2F9FdRAAJLSgACbS6YSguHhGTRjB1BNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "790":
            await message.answer_video(
                video="BAACAgIAAxkBAAIFFmdmio5qPM169ms74KtMbet_ciyQAAKtMQAC2E2gSbwLK89IXv9ZNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "792":
            await message.answer_video(
                video="BAACAgQAAxkBAAIFGGdmiwhAbI-Hnl0FpJZ__hhmBF-OAAJ3FQAC5yDAUUFZ73ILvqk6NgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "794":
            await message.answer_video(
                video="BAACAgQAAxkBAAIFGmdmi1ZIGWLfs079xv1SnPhD7PyxAAKzEQACXYURUZExu36sD9RBNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "796":
            await message.answer_video(
                video="BAACAgEAAxkBAAIFHGdmi49Ii7-i8Sq0Em83xbNTCVMmAALpAQACFcFIRS4baSG8pdPqNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "798":
            await message.answer_video(
                video="BAACAgQAAxkBAAIFHmdmi9caF5iiFlBmoAlxSzXo3pxKAAKCEQACC7UBU15QeBiIywhmNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "800":
            await message.answer_video(
                video="BAACAgQAAxkBAAIFIGdmjC67tlGIB0M7I80qF8UMN2QdAAKrCgACEWgBUiHzphColM8TNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "802":
            await message.answer_video(
                video="BAACAgIAAxkBAAIFImdmjHhT2t_nkgYZw1tFIJQDnbpzAAI1DgACFehxS6WuEfvc1HniNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "804":
            await message.answer_video(
                video="BAACAgQAAxkBAAIFJGdmjNAwG49GCMJ2wm1ehWzDyM90AAJfEgACY7OxUBFI-xUj3qjNNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )
        elif message.text == "806":
            await message.answer_video(
                video="BAACAgQAAxkBAAIFKGdmlMeE4arLlPO9KXuquLaRRGNJAAKGBgACY1CgUmvRLizmz4BWNgQ",
                caption="Kinoni ko'rishingiz mumkin    kanalimizga azo bo'ling @kinomt"
            )

        else:
            await message.answer("⚠️ Bu KOD noto'g'ri yoki mavjud emas! \n \n kerakli kod bu yerda @kinomt")
    else:
        # Kanalga a'zo bo'lmagan bo'lsa, kanalga a'zo bo'lish uchun oyna yuboriladi
        all_channels = not_subscribed_channels + EXCLUDED_CHANNELS
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=" Kanalga a'zo bo'lish",
                        url=channel["url"]
                    )
                ] for channel in all_channels
            ] + [
                [
                    InlineKeyboardButton(
                        text="✅ A'zo bo'ldim ✅",
                        callback_data="azo"
                    )
                ]
            ],
            row_width=1
        )
        await message.answer(
            "⬇️ <b>Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling</b> ⬇️",
            reply_markup=keyboard,
            parse_mode='HTML'
        )


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_video_id(message: Message):
    video_id = message.video.file_id
    await message.answer(f"Video File ID: {video_id}")

# Asosiy funksiya
async def main():
    print("Bot ishga tushmoqda...")
    await dp.start_polling()

# Botni ishga tushirish
if __name__ == "__main__":
    asyncio.run(main())
