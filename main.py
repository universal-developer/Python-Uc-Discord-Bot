import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import sqlite3


load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
PREFIX = "uc!"
intents = discord.Intents.default()
intents.members = True
CONNECTION = sqlite3.connect("/Users/artush/Code/bots/discord/uc-discord-bot/uc-bot-db.sqlite3")
CURSOR = CONNECTION.cursor()


bot = commands.Bot(command_prefix = f"{PREFIX}", help_command = None, intents = intents, description = "Universal Helper", case_insensitive = False)

#Bot is ready command
@bot.event
async def on_ready():
    print("Database created and Successfully Connected to SQLite") 
    print("============================================================")
    await bot.change_presence(activity = discord.Game(name = "Ready to help"))
    print('We have logged in as {0.user}'.format(bot))
    
#Getting all messages as lowercase
@bot.event
async def on_message(message):
    message.content = message.content.lower()
    await bot.process_commands(message)

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
    await ctx.send(f"""***Here is what I can actually do:***
                   
**| {PREFIX}help** - *displays help command 🚀*
**| {PREFIX}cvc <channels name>** - *creates voice channel (for administrators only) 🚀*
**| {PREFIX}ctc <channels name>** - *creates text channel (for administrators only) 🚀*
**| {PREFIX}cls <amount>** - *cleans chat, besides pined messages. Also you can use: clear, cleaning, clear (for administrators only) 🚀*
**| {PREFIX}welcome** - *shows welcome message (for administrators only) 🚀*
**| {PREFIX}kick <@user> <reason>** - *kicks user from server (for administrators only) 🚀*
**| {PREFIX}ban <@user> <reason>** - *bans user from server (for administrators only) 🚀*
**| {PREFIX}banned_list** - *shows banned users list. You can also use: banned_lst, banned_users (for administrators only) 🚀*
**| {PREFIX}unban <@user's id>** - *unbans user (for administrators only) 🚀*

**‼️It doesn't matter in which case the command is written. Be it uc!help or UC!HELP or Uc!HeLp‼️**

***🦄Other commands such as role-claim are reproduced automatically by the developer of this bot. 🦄 ***      
    """)

#Welcome Command
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['welcome', 'welcome_command'], brief = "Showing welcome command")
async def on_welcome(ctx):
    
    channel_id = bot.get_channel(964218392007544923)
    
    embed = discord.Embed(title = "🚀🚀🚀 You're Welcome 🚀🚀🚀", url = "https://realdrewdata.medium.com/", description = """
                          
                          
                          
                          **My name is 🦄UC🦄 and I am Universal Creator's handheld assistant.\n\nI'm here to help him manage this server, but luckily I have something for you too. \n\n I hope you enjoy being on the server.😉 \n\nBy the way, do not forget, my creator is hard at work on the distributions, which will soon be made🔥🔥🔥.**
                          
                          
                          
                          """, color = discord.Color.purple())
    embed.set_author(name = "Universal Creator", icon_url = ctx.author.avatar_url)
    embed.set_footer(text = f"So, here is what I can actually do: {channel_id}")
    await ctx.send(embed = embed)

#Clean chat command
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['clean', 'cleaning', 'cls', 'clear'], brief = "Clear chat from message. 20 Messages by default", usage = "clear <amount=20>")
async def on_clear(ctx, amount: int = 20):
    await ctx.channel.purge(limit = amount, check = lambda msg: not msg.pinned)

#Create text channel 
@commands.has_permissions(administrator = True)    
@bot.command(aliases = ['create_txt_channel', 'ctc'])
async def create_text_channel(ctx, channel_name):
	guild = ctx.guild
	await guild.create_text_channel(channel_name)

#Create voice channel 
@commands.has_permissions(administrator = True)    
@bot.command(aliases = ['create_vc_channel', 'cvc'])
async def create_voice_channel(ctx, channel_name):
	guild = ctx.guild
	await guild.create_voice_channel(channel_name)
 
#Kick users
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['kick', 'kck'])
async def kick_user(ctx, user: discord.Member, *, reason):
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} has been successfully kicked for {reason}.")

#Ban users
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['ban', 'bn'])
async def ban_user(ctx, user: discord.Member, *, reason):
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} has been successfully banned for {reason}.")

#Showing banned users list
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['banned_list', 'banned_lst'])
async def banned_users(ctx):
    bans = await ctx.guild.bans()
    pretty_list = ["ID: {0.id}\nName: {0.name}\nDiscriminator: {0.discriminator}".format(entry.user) for entry in bans]
    await ctx.send("**Ban list:** \n{}".format("\n".join(pretty_list)))

#Unban users
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['unban', 'unbn'])
async def unban_user(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f"{user} has been successfully unbanned")

@commands.has_permissions(administrator = True)
@bot.command(aliases = ['level', 'lvl'])
async def on_levels(ctx, id):
    user = await bot.fetch_user(id)
    name = user.name
    discriminator = user.discriminator
    level = 1
    
    await ctx.send(user.name + '\n' + user.discriminator)
    
    my_user = (
         0, name, discriminator, level
    )
    
    CURSOR.executemany('INSERT INTO users_database VALUES (?,?,?,?)', my_user)

#Errors handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You are missing a required argument")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.reply("You do not have a right permisions")
    elif isinstance(error, commands.MissingRole):
        await ctx.reply("You are missing a right role")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.reply("I don't understand you")
    else:
        await ctx.reply("Something went wrong")
        print(error)

bot.run(DISCORD_TOKEN)
