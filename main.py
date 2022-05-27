import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
PREFIX = "uc!"
intents = discord.Intents.default()
intents.members = True
SERVER_NAME = "Universal Creator"

bot = commands.Bot(command_prefix = f"{PREFIX}", help_command = None, intents = intents, description = "Universal Helper", case_insensitive = False)




#Getting users status
def getstatus(self, m):
    if str(m.status) == "dnd":
        return "do not disturb"
    return m.status

#Bot is ready command
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = "Ready to help"))
    print('We have logged in as {0.user}'.format(bot))
    

@bot.command()
async def load_cogs(extension):
    bot.load_extension(f"cogs.{extension}")
    
    print("Cogs is loaded")
    

@bot.command()
async def unload_cogs(extension):
    bot.unload_extension(f"cogs.{extension}")
    
    print("Cogs is unloaded")    
    
@bot.command()
async def reload_cogs(extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    
    print("Cogs is reloaded")        
    
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        
        
#Getting all messages as lowercase
@bot.event
async def on_message(message):
    message.content = message.content.lower()
    await bot.process_commands(message)

#Errors handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You are missing a required argument")
        print(error)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.reply("You do not have a right permisions")
        print(error)
    elif isinstance(error, commands.MissingRole):
        await ctx.reply("You are missing a right role")
        print(error)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.reply("I do not understand you")
        print(error)
    elif isinstance(error, discord.NotFound):
        await ctx.reply("Nobody found")
        print(error)
    elif isinstance(error, discord.Forbidden):
        await ctx.reply("Error 403")
    else:
        await ctx.reply(f"Something went wrong. Error: {error}")
        print(error)

#Running bot
bot.run(DISCORD_TOKEN)
