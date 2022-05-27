from discord.ext.commands import Bot
from discord.ext import commands
import youtube_dl
from discord import FFmpegPCMAudio
from discord.utils import get


from main import * 
class Player(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
      
  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def join(self, ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f"I connected in voice channel **{channel}**")
  
  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def leave(self, ctx):
    channel = ctx.author.voice.channel
    if (ctx.voice_client): 
        await ctx.guild.voice_client.disconnect() 
        await ctx.send(f"I left from **{channel}**")
    else: # But if it isn't
        await ctx.send("I'm not in a voice channel right now")
  
  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def play(self, ctx, url):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('1.m4a')
    player = voice.play(source)
    voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source = URL, **FFMPEG_OPTIONS))
    
    
def setup(bot):
  bot.add_cog(Player(bot))