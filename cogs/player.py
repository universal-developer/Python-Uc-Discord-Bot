
import discord
from discord.ext.commands import Bot
from discord.ext import commands

from main import * 

players = {}

class Player(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def join(self, ctx):
    server = ctx.message.server
    if client.is_voice_connected(server):
      voice_client = client.voice_client_in(server)
      await voice_client.disconnect()
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    
  @commands.command(pass_content = True)
  @commands.Cog.listener()
  async def leave(self, ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    if voice_client != None:
      await voice_client.disconnect()
    
  @commands.command(pass_context = True)
  async def play(self, ctx):
    server = ctx.message.server
    voice_bot = bot.voice_bot_in(server)
    player = await voice_bot.create_ytdl_player(url)
    players[server.id] = player
    
    players.start()
    
def setup(bot):
  bot.add_cog(Player(bot))