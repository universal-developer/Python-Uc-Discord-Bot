from discord.ext.commands import Bot
from discord.ext import commands
import youtube_dl
from main import * 
class Player(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  
  YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
  FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      
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
      pass
  
  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def play(self, ctx, url):
    YDL_OPTIONS = {'format': "bestaudio"}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info=  ydl.extract_info(url,download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,
      **FFMPEG_OPTIONS)
        vc.play(source)

  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def pause(self, ctx):
    await ctx.voice_client.pause()
    await ctx.send("Paused")
  
  @commands.command(pass_context = True)
  @commands.Cog.listener()
  async def resume(self, ctx):
    await ctx.voice_client.resume()
    await ctx.send("Resume")
    
def setup(bot):
  bot.add_cog(Player(bot))