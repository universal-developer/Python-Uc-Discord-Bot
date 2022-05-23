import discord
import youtube_dl
from discord.ext import commands

from main import * 

players = {}

class Player(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def join(self, ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    
  @commands.command(pass_content = True)
  @commands.Cog.listener()
  async def leave(self, ctx):
    server = ctx.message.server
    voice_bot = bot.voice_bot_in(server)
    await voice_bot.disconnect()
    
  @commands.command(pass_context = True)
  async def play(self, ctx):
    server = ctx.message.server
    voice_bot = bot.voice_bot_in(server)
    player = await voice_bot.create_ytdl_player(url)
    players[server.id] = player
    
    players.start()
    
def setup(bot):
  bot.add_cog(Player(bot))