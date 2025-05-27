# bot.py

from keep_alive import keep_alive
keep_alive()

import discord
import os

intents = discord.Intents.default()
intents.message_content = True  # ✅ ←これを追加！

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "ping":
        await message.channel.send("pong!")

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
