 ## PROFESSOR SADA BOT
import asyncio
import json
import random
import string
import time
from pathlib import Path
from discord.ext import commands, tasks

version = 'v1.2'
config = json.loads(Path("config.json").read_text())

## Defining the server and bot token

user_token = config["user_token"]
spam_id = config["spam_id"]
client = commands.Bot(command_prefix= '&' )

## Spammer
intervals = [3.0, 2.2, 2.4, 2.6, 2.8]

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    message = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 7) * 5)
    try:
        await channel.send(message)
        print(f'Sent message ' + message)
    except Exception as e:
        print("Something went wrong while sending the message:", str(e))

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

@client.event
async def on_ready():
    global spam
    print(f'Logged into account: {client.user.name}')
    spam.start()

print()
print(f'Created by evad3r. {version}')

asyncio.run(client.run(f"{user_token}"))
