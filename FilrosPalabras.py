import discord
from discord.ext import commands,tasks
import datetime 
from itertools import cycle
import os

bot = commands.Bot(command_prefix = '/')

with open('FiltrosPalabras.txt') as archivo:
    archivo =  archivo.read().split()




@bot.event 
async def on_message(message):
    for Palabra in archivo:
        if Palabra in message.content.lower():
            await message.delete()
            await message.channel.send(f'Hey, {message.author.mention} ten cuidado con lo que dices!!!')
        else:
            await bot.process_commands(message)


@bot.event
async def on_ready():
    print("BOT listo!")
    print(archivo)
 
 
 
bot.run('')    #Crea un bot e un Token: https://discord.com/developers/applications


