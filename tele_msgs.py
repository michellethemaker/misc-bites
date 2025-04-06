# referenced: https://andrewkushnerov.medium.com/how-to-send-notifications-to-telegram-with-python-9ea9b8657bfb
import asyncio
from telegram import Bot, InputFile
import pandas as pd
import matplotlib.pyplot as plt
import io
import os
from dotenv import load_dotenv

load_dotenv()

telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

bot = Bot(token=telegram_token) # create bot object

async def obtainChatID():
    updates = await bot.get_updates() # get updates
    if not updates:
        print("No updates found")
    else:
        for update in updates:
            if update.message:
                #print(update.message) # shows msg data
                chat_id = update.message.chat.id
                chat_title = update.message.chat.title
                message_text = update.message.text
                print(f"Chat ID: {chat_id}  | Chat Title: {chat_title} | Message: {message_text}")

async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def run_bot(messages, chat_id):
    text = '\n'.join(messages)
    await send_message(text, chat_id)

async def send_image(image, chat_id):
    async with bot:
        await bot.send_photo(chat_id=chat_id, photo=InputFile(image))

def create_chart():
    # dummy data for dataframe
    data = {
        'Date': pd.date_range(start='2024-08-01', periods=10, freq='D'),
        'Value': [24.99, 25.49, 26.00, 25.75, 26.99, 26.50, 27.00, 26.80, 27.20, 27.50]
    }
    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Value'], marker='o')
    ax.set_title('Value Trend')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    plt.xticks(rotation=45)

    # save graph to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return buf


async def main():
    # CHAT_ID = obtainChatID(TELEGRAM_BOT_TOKEN)
    # messages = [
    #     'hi there',
    #     'tis me',
    #     'from the other side'
    # ]
    # messages2 = [
    #     'hi there2',
    #     'tis me2',
    #     'from the other side2'
    # ]

    # if messages:
    #     await run_bot(messages, CHAT_ID)
    #     asyncio.run(run_bot(messages2, CHAT_ID))

    # generate image w chart
    image = create_chart()
    await send_image(image, chat_id)
asyncio.run(main())