import discord
from discord.ext import commands
from main import * 

class Mute(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #Mute users
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['mt'])
  async def mute(self, ctx, member: discord.Member): 
      link = await ctx.channel.create_invite(max_age = 300)
      
      mute_role = discord.utils.get(ctx.message.guild.roles, name = "Mute")
      
      await member.add_roles(mute_role)
      await ctx.send(f"Dear {member.mention}, you were muted for breaking the rules")
      await member.send(f"Dear {member.mention}, you have got mute in {link} for breaking rules")

  #Unmute user
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['unmt'])
  async def unmute(self, ctx, member: discord.Member):
      mute_role = discord.utils.get(ctx.message.guild.roles, name = "Mute")
      link = await ctx.channel.create_invite(max_age = 300)
      
      await member.remove_roles(mute_role)
      await member.send(f"Dear {member.mention}, you were unmuted in {link}")
      await ctx.send(f"{member.mention} was successfully unmuted")   
  
def setup(bot):
  bot.add_cog(Mute(bot))