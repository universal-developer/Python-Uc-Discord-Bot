import discord
from discord.ext import commands
from main import * 

class Welcome(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
     
  @commands.has_permissions(administrator = True)
  @commands.command(aliases = ['welcome', 'welcome_command'], brief = "Showing welcome command")
  @commands.Cog.listener()
  async def on_welcome(self, ctx):
      
      channel_id = bot.get_channel(964218392007544923)
      
      embed = discord.Embed(title = "🚀🚀🚀 You're Welcome 🚀🚀🚀", description = """
                            
                            
                            
                            **My name is 🦄UC🦄 and I am Universal Creator's handheld assistant.\n\nI'm here to help him manage this server, but luckily I have something for you too. \n\n I hope you enjoy being on the server.😉 \n\nBy the way, do not forget, my creator is hard at work on the distributions, which will soon be made🔥🔥🔥.**
                            
                            
                            
                            """, color = discord.Color.purple())
      embed.set_author(name = "Universal Creator", icon_url = ctx.author.avatar_url)
      embed.set_footer(text = f"So, here is what I can actually do: {channel_id}")
      await ctx.send(embed = embed)
      
def setup(bot):
  bot.add_cog(Welcome(bot))