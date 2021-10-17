import discord
from discord.ext import commands
from core.Classes import Cog_Extension

class React(Cog_Extension):

# @bot.command()
# async def SendImage(ctx):
#     pic = discord.File('本機圖片位置')
#     await ctx.send(File=pic)

    @commands.command()
    async def SendImage(self,ctx):
        await ctx.send('https://media.discordapp.net/attachments/688438282450763817/839099394929197056/54440563cddfcf678f19d61bfdfb6f59.gif')

def setup(bot):
    bot.add_cog(React(bot))
