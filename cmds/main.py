﻿import discord
from discord.ext import commands
from core.Classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'延遲時間:{self.bot.latency*1000:.3f} ms')

    @commands.command()
    async def hi(self,ctx):
        await ctx.send(F'1233')


def setup(bot):
    bot.add_cog(Main(bot))