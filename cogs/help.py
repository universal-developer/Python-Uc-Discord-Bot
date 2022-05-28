from discord.ext import commands
import discord
from main import *

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
     
  @commands.command(name = 'help')
  @commands.Cog.listener()
  async def on_help(self, ctx):
    embed = discord.Embed(title = "🚀🚀🚀 ***Here is what I can actually do:*** 🚀🚀🚀", description = """
                                      
    ***For mere mortals***
    **| {PREFIX}help** - *displays help command 🚀*
    **| {PREFIX}user_info <@mention user>** - *shows user info 🚀*

    ***For Administrators:***
    **| {PREFIX}cvc <channels name>** - *creates voice channel (for administrators only) 🚀*
    **| {PREFIX}ctc <channels name>** - *creates text channel (for administrators only) 🚀*
    **| {PREFIX}cls <amount>** - *cleans chat, besides pined messages. The amount equals to 50 by default. Also you can use: clear, cleaning, clear (for administrators only) 🚀*
    **| {PREFIX}welcome** - *shows welcome message (for administrators only) 🚀*
    **| {PREFIX}kick <@user> <reason>** - *kicks user from server (for administrators only) 🚀*
    **| {PREFIX}ban <@user> <reason>** - *bans user from server (for administrators only) 🚀*
    **| {PREFIX}banned_list** - *shows banned users list. You can also use: banned_lst, banned_users (for administrators only) 🚀*
    **| {PREFIX}unban <@user's id>** - *unbans user (for administrators only) 🚀*
    **| {PREFIX}mute <@mention user>** - *mutes user (for administrators only) 🚀*
    **| {PREFIX}unmute <@mention user>** - *unmutes user (for administrators only) 🚀*
                                
    """, color = discord.Color.purple())
  
    # Setting the thumbnail as the users profile picture
    embed.set_thumbnail(url = ctx.author.avatar_url)
    
    # Setting a footer
    embed.set_footer(text = """**‼️It doesn't matter in which case the command is written. Be it uc!help or UC!HELP or Uc!HeLp‼️**

    ***🦄Other commands such as role-claim are reproduced automatically by the developer of this bot. 🦄 ***      
      """, icon_url = ctx.author.avatar_url)
    

    


    await ctx.send(embed = embed)      

def setup(bot):
  bot.add_cog(Help(bot))