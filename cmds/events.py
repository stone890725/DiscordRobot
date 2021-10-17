import discord
from discord.ext import commands
from core.Classes import Cog_Extension
import json


class Events(Cog_Extension):
    
    with open('setting.json','r',encoding='utf8') as jFile:
        jdata = json.load(jFile)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(jdata["TestRobotChannel"])
        await channel.send(F'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = bot.get_channel(jdata["TestRobotChannel"])
        await channel.send(F'{member} leave!')
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == 'test':
            await msg.channel.send('hi')


def setup(bot):
    bot.add_cog(Events(bot))