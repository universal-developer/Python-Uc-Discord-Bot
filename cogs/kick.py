import discord
from discord.ext import commands
from main import * 

class Kick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
     
  ##Kick users
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['kick', 'kck'])
  async def kick_user(self, ctx, member: discord.Member, *, reason):
      link = await ctx.channel.create_invite(max_age = 300)
      
      await member.send(f"Dear {member.mention}, you were kicked for {reason}")
      await ctx.guild.kick(member, reason = reason)
      await ctx.send(f"{member.mention} has been successfully kicked for {reason}.")
      
def setup(bot):
  bot.add_cog(Kick(bot))