import discord
from discord.ext import commands
from main import * 

class Channels(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
     
  #Clean chat command
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['clean', 'cleaning', 'cls', 'clear'], brief = "Clear chat from message. 20 Messages by default", usage = "clear <amount=20>")
  @commands.Cog.listener()
  async def on_clear(self, ctx, amount: int = 50):
      await ctx.channel.purge(limit = amount, check = lambda msg: not msg.pinned)

  #Create text channel 
  @commands.has_permissions(administrator = True)  
  @commands.command(aliases = ['create_txt_channel', 'ctc'])
  @commands.Cog.listener()  
  async def create_text_channel(self, ctx, channel_name):
    guild = ctx.guild
    await guild.create_text_channel(channel_name)

  #Create voice channel 
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['create_vc_channel', 'cvc'])
  @commands.Cog.listener()    
  async def create_voice_channel(self, ctx, channel_name):
    guild = ctx.guild
    await guild.create_voice_channel(channel_name)

  #Delete text channel
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['dtc', 'delete_txt_channel'])
  @commands.Cog.listener()
  async def delete_text_channel(self, ctx, channel: discord.TextChannel):
      if channel is not None:
        await channel.delete()
      else:
        await ctx.send(f'No channel named, "{channel}", was found')

  #Delete voice channel      
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['dvc', 'delete_vc_channel'])
  @commands.Cog.listener()
  async def delete_voice_channel(self, ctx, channel: discord.VoiceChannel):
      if channel is not None:
        await channel.delete()
      else:
        await ctx.send(f'No channel named, "{channel}", was found')
      
def setup(bot):
  bot.add_cog(Channels(bot))