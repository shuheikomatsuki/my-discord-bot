import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content == 'ping':
        await message.channel.send('pong!')

TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)