import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
PREFIX = "uc!"
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=f"{PREFIX}", help_command = None, intents=intents)

#Bot is ready command
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#Bot sends message for members, when they're joining
@bot.event
async def on_member_join(member):
    await bot.get_channel(963807822846496818).send(f"{member.name} has joined")

#Bot sends message for members, when they're leave
@bot.event
async def on_member_remove(member):
    await bot.get_channel(964176007605125180).send(f"{member.name} has left")
 
#Help command    
@bot.command(name = 'help')
async def on_help(ctx):
    await ctx.send("Custom help command")

#Welcome Command
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['welcome', 'welcome_command'], brief = "Showing welcome command")
async def on_welcome(ctx):
    
    channel_id = bot.get_channel(964218392007544923)
    
    embed = discord.Embed(title = "🚀🚀🚀 You're Welcome 🚀🚀🚀", url = "https://realdrewdata.medium.com/", description = """
                          
                          
                          
                          My name is 🦄UC🦄 and I am Universal Creator's handheld assistant.\n\nI'm here to help him manage this server, but luckily I have something for you too. \n\n I hope you enjoy being on the server.😉 \n\nBy the way, do not forget, my creator is hard at work on the distributions, which will soon be made🔥🔥🔥.
                          
                          
                          
                          """, color = discord.Color.purple())
    embed.set_author(name = "Universal Creator", icon_url = ctx.author.avatar_url)
    embed.set_footer(text = f"So, here is what I can actually do: {channel_id}")
    await ctx.send(embed = embed)

#Clean chat command
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['clean', 'cleaning', 'cls', 'clear'], brief = "Clear chat from message. 10 Messages by default", usage = "clear <amount=10>")
async def on_clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit = amount)
 
@commands.has_permissions(administrator = True)    
@bot.command(aliases = ['create_txt_channel'])
async def create_text_channel(ctx, channel_name):
	guild = ctx.guild
	await guild.create_text_channel(channel_name)


"""
@bot.command(name="очистить", brief="Очистить чат от сообщений, по умолчанию 10 сообщений", usage="clear <amount=10>")
async def clear(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Was deleted {amount} messages...")
"""


bot.run(DISCORD_TOKEN)
