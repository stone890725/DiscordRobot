import discord
from discord.ext import commands
import

# intents = discord.Intents.default()
# intents.members = True
intents = discord.Intents.all()
 
bot = commands.Bot(command_prefix="!",intents = intents)

@bot.event
async def on_ready():
    print("Bot is online")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(899185079329357865)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(899185079329357865)
    await channel.send(F'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'延遲時間:{bot.latency*1000:.3f} ms')


    
bot.run("ODk5MTgxOTE2OTc5MzYzODUx.YWvCaw.wO3gg9ooTY38zvrtnhVmht3nWbc")
   

#  @bot.event
# async def Funcname(parameter_list):