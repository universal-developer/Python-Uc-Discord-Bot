import discord
from discord.ext import commands
from datetime import datetime, timedelta, timezone
from main import * 

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #User information command
  @commands.command(aliases = ['member_info'])
  async def info(self, ctx, member: discord.Member):
      # Calculating time since the user created his discord account using the member.created_at method
      c_delta = datetime.utcnow() - member.created_at
      c_ago = datetime.fromtimestamp(c_delta.seconds, tz = timezone.utc).strftime("%H:%M:%S")
      c_at = member.created_at.strftime("%c")

      # Getting join position by sorting the guild.members list with the member.joined_at method
      join_pos = sorted(ctx.guild.members, key = lambda member: member.joined_at).index(member) + 1
      
      # Defining discord.Embed instance
      embed = discord.Embed(title = f"{member.name}#{member.discriminator}", timestamp = datetime.utcnow(), color = discord.Color.purple())
      
      # Adding fields to the embed
      embed.add_field(name = "Status:", value = getstatus(self, member), inline = True)
      embed.add_field(name = "Guild name:", value = member.display_name, inline=True)
      embed.add_field(name = "Join position:", value = f"{join_pos}/{len(ctx.guild.members)}", inline = True)

      embed.add_field(name = "Created at:", value=f"{c_at}\n({c_delta.days} days, {c_ago} ago)", inline = True)
      embed.add_field(name = "ID:", value=member.id, inline=True)
      embed.add_field(name = "Bot:", value="✅ Yes" if member.bot else "❌ No", inline = True)
      
      # Setting the thumbnail as the users profile picture
      embed.set_thumbnail(url = member.avatar_url)
      
      # Setting a footer
      embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)

      await ctx.send(embed = embed)
  
      
def setup(bot):
  bot.add_cog(Fun(bot))