from discord.ext import commands
from main import * 

class Member(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @bot.event
  @commands.Cog.listener()
  async def on_member_join(self, member):
      await bot.get_channel(963807822846496818).send(f"Welcome {member.mention} to the {SERVER_NAME} ")

  #Bot sends message for members, when they're leave
  @bot.event
  @commands.Cog.listener()
  async def on_member_remove(self, member):
      await bot.get_channel(964176007605125180).send(f"Bye {member.mention}")
      

def setup(bot):
  bot.add_cog(Member(bot))