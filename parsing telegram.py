from telethon.sync import TelegramClient
import pytz
import asyncio
import csv

API_ID = '********'
API_HASH = '********************************'
PHONE = '************'
CHANNEL_USERNAME = 'Arrowwoodsboy'
TARGET_LINK = 'twitch.tv/arrowwoods'
TIMEZONE = pytz.timezone('Europe/Samara')
CSV_FILENAME = 'streamdate.csv'

async def main():
    client = TelegramClient('session_name', API_ID, API_HASH)
    await client.start(PHONE)
    
    print("Авторизация успешна")
    
    channel = await client.get_entity(CHANNEL_USERNAME)
    post_dates = []
    
    async for message in client.iter_messages(channel):
        if message.text and TARGET_LINK in message.text:
            dt = message.date.astimezone(TIMEZONE)
            post_dates.append(dt)
            print(f"Найден пост от {dt}")
    
    with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date', 'time'])
        
        for dt in post_dates:
            time_in_hours = dt.hour + dt.minute/60
            writer.writerow([
                dt.strftime('%Y-%m-%d'),
                f"{time_in_hours:.4f}"
            ])

asyncio.run(main())