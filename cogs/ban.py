import discord
from discord.ext import commands
import discord.utils
from main import * 

class Ban(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
     
  #Ban users
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['bn'])
  async def ban(self, ctx, member: discord.Member, *, reason):
      link = await ctx.channel.create_invite(max_age = 300)
      
      await member.send(f"Dear {member.mention}, you was banned for {reason} in {link}")
      await ctx.guild.ban(member, reason = reason)
      await ctx.send(f"{member.mention} has been successfully banned for {reason}.")

  #Showing banned users list
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['banned_list', 'banned_lst'])
  async def show_banned_list(self, ctx):
      bans = await ctx.guild.bans()
      
      for ban_entry in bans:
          user = ban_entry.user
          user_name = user.name
          discriminator = user.discriminator
          user_id = user.id
          reason = ban_entry.reason
          
          await ctx.send(f"""
  *User:* **{user}**
  *Username:* **{user_name}**
  *Discriminator (#):* **{discriminator}**
  *User ID:* **{user_id}**
  *Reason:* **{reason}**           
              """)

  #Unban users
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['unbn'])
  async def unban(self, ctx, id: int):
    link = await ctx.channel.create_invite(max_age = 300)
    
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f"{user.mention} has been successfully unbanned")
    await user.send(f"Dear {user.mention}, you were unbanned in {link}")
    
      
def setup(bot):
  bot.add_cog(Ban(bot))