import discord
from discord.ext import commands
import json
import os

# intents = discord.Intents.default()
# intents.members = True
intents = discord.Intents.all()
with open('setting.json','r',encoding='utf8') as jFile:
    jdata = json.load(jFile)



bot = commands.Bot(command_prefix="!",intents = intents)

@bot.event
async def on_ready():
    print("Bot is online")


@bot.command()
async def load(ctx,extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension} done')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'Un-Loaded {extension} done')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'Re-Loaded {extension} done')


for fileName in os.listdir('./cmds'):
    if fileName.endswith('.py'):
        bot.load_extension(F'cmds.{fileName[:-3]}')  #.py

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
    

   