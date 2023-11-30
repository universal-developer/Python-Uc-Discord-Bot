from discord.ext import commands
import discord
from main import *

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name = 'help')
  @commands.Cog.listener()
  async def on_help(self, ctx):
    embed = discord.Embed(title = "🚀🚀🚀 ***Here is what I can actually do:*** 🚀🚀🚀", color = discord.Color.purple())
    
    embed.add_field(name = "Help\nUser_info\nCVC\n", value = "Displays help command\nshows user information\n",inline = True)
  
    # Setting the thumbnail as the users profile picture
    embed.set_thumbnail(url = ctx.author.avatar_url)
    
    # Setting a footer
    embed.set_footer(text = """**‼️It doesn't matter in which case the command is written. Be it uc!help or UC!HELP or Uc!HeLp‼️**

    ***🦄Other commands such as role-claim are reproduced automatically by the developer of this bot. 🦄 ***      
      """, icon_url = ctx.author.avatar_url)
  
    await ctx.send(embed = embed)      
def setup(bot):
  bot.add_cog(Help(bot))