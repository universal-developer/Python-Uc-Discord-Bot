import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import sqlite3
from datetime import datetime, timedelta, timezone


load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
PREFIX = "uc!"
intents = discord.Intents.default()
intents.members = True
SERVER_NAME = "Universal Creator"
#CONNECTION = sqlite3.connect("/Users/artush/Code/bots/discord/uc-discord-bot/uc-bot-db.sqlite3")
#CURSOR = CONNECTION.cursor()


bot = commands.Bot(command_prefix = f"{PREFIX}", help_command = None, intents = intents, description = "Universal Helper", case_insensitive = False)

#Bot is ready command
@bot.event
async def on_ready():
    #print("Database created and Successfully Connected to SQLite") 
    #print("============================================================")
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
    await bot.get_channel(963807822846496818).send(f"Welcome {member.mention} to the {SERVER_NAME} ")

#Bot sends message for members, when they're leave
@bot.event
async def on_member_remove(member):
    await bot.get_channel(964176007605125180).send(f"Bye {member.mention}")
 
#Help command    
@bot.command(name = 'help')
async def on_help(ctx):
    await ctx.send(f"""***Here is what I can actually do:***
                   
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

**‼️It doesn't matter in which case the command is written. Be it uc!help or UC!HELP or Uc!HeLp‼️**

***🦄Other commands such as role-claim are reproduced automatically by the developer of this bot. 🦄 ***      
    """)

#Welcome Command
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['welcome', 'welcome_command'], brief = "Showing welcome command")
async def on_welcome(ctx):
    
    channel_id = bot.get_channel(964218392007544923)
    
    embed = discord.Embed(title = "🚀🚀🚀 You're Welcome 🚀🚀🚀", description = """
                          
                          
                          
                          **My name is 🦄UC🦄 and I am Universal Creator's handheld assistant.\n\nI'm here to help him manage this server, but luckily I have something for you too. \n\n I hope you enjoy being on the server.😉 \n\nBy the way, do not forget, my creator is hard at work on the distributions, which will soon be made🔥🔥🔥.**
                          
                          
                          
                          """, color = discord.Color.purple())
    embed.set_author(name = "Universal Creator", icon_url = ctx.author.avatar_url)
    embed.set_footer(text = f"So, here is what I can actually do: {channel_id}")
    await ctx.send(embed = embed)

#Clean chat command
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['clean', 'cleaning', 'cls', 'clear'], brief = "Clear chat from message. 20 Messages by default", usage = "clear <amount=20>")
async def on_clear(ctx, amount: int = 50):
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
async def kick_user(ctx, member: discord.Member, *, reason):
    link = await ctx.channel.create_invite(max_age = 300)
    
    await member.send(f"Dear {member.mention}, you were kicked for {reason}")
    await ctx.guild.kick(member, reason = reason)
    await ctx.send(f"{member.mention} has been successfully kicked for {reason}.")
    

#Ban users
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['ban', 'bn'])
async def ban_user(ctx, member: discord.Member, *, reason):
    link = await ctx.channel.create_invite(max_age = 300)
    
    await member.send(f"Dear {member.mention} has been successfully banned for {reason} in {link}")
    await ctx.guild.ban(member, reason = reason)
    await ctx.send(f"{member.mention} has been successfully banned for {reason}.")

#Showing banned users list
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['banned_list', 'banned_lst'])
async def banned_users(ctx):
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
@bot.command(aliases = ['unban', 'unbn'])
async def unban_user(ctx, id: int):
    link = await ctx.channel.create_invite(max_age = 300)
    
    user = await bot.fetch_user(id)
    await member.send(f"Dear {member.mention}, you were unbanned in {link}")
    await ctx.guild.unban(user)
    await ctx.send(f"{user.mention} has been successfully unbanned")
    
#Mute users
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['mt', 'mute'])
async def mute_user(ctx, member: discord.Member): 
    link = await ctx.channel.create_invite(max_age = 300)
    
    mute_role = discord.utils.get(ctx.message.guild.roles, name = "Mute")
    
    await member.add_roles(mute_role)
    await ctx.send(f"Dear {member.mention}, you were muted for breaking the rules")
    await member.send(f"Dear {member.mention}, you have got mute in {link} for breaking rules")

#Unmute user
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['unmt', 'unmute'])
async def unmute_user(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name = "Mute")
    link = await ctx.channel.create_invite(max_age = 300)
    
    await member.remove_roles(mute_role)
    await member.send(f"Dear {member.mention}, you were unmuted in {link}")
    await ctx.send(f"{member.mention} was successfully unmuted")

#Getting users status
def getstatus(m):
    if str(m.status) == "dnd":
        return "do not disturb"
    return m.status

#User information command
@bot.command(aliases = ['member_info', 'user_info'])
async def info(ctx, member: discord.Member):
    # Calculating time since the user created his discord account using the member.created_at method
    c_delta = datetime.utcnow() - member.created_at
    c_ago = datetime.fromtimestamp(c_delta.seconds, tz = timezone.utc).strftime("%H:%M:%S")
    c_at = member.created_at.strftime("%c")

    # Getting join position by sorting the guild.members list with the member.joined_at method
    join_pos = sorted(ctx.guild.members, key = lambda member: member.joined_at).index(member) + 1
    
    # Defining discord.Embed instance
    embed = discord.Embed(title = f"{member.name}#{member.discriminator}", timestamp = datetime.utcnow(), color = discord.Color.purple())
    
    # Adding fields to the embed
    embed.add_field(name = "Status:", value=getstatus(member), inline = True)
    embed.add_field(name = "Guild name:", value=member.display_name, inline=True)
    embed.add_field(name = "Join position:", value=f"{join_pos}/{len(ctx.guild.members)}", inline = True)

    embed.add_field(name = "Created at:", value=f"{c_at}\n({c_delta.days} days, {c_ago} ago)", inline = True)
    embed.add_field(name = "ID:", value=member.id, inline=True)
    embed.add_field(name = "Bot:", value="✅ Yes" if member.bot else "❌ No", inline = True)
    
    # Setting the thumbnail as the users profile picture
    embed.set_thumbnail(url = member.avatar_url)
    
    # Setting a footer
    embed.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)

    await ctx.send(embed = embed)

@commands.has_permissions(administrator = True)
@bot.command(aliases = ['add_role', 'cr'])
async def create_role(ctx, name):
    guild = ctx.guild
    
    await guild.create_role(name = name)
    await ctx.send(f"Role {name} was successfully created")

#Role claim messages
@commands.has_permissions(administrator = True)
@bot.command(aliases = ['rcm'])
async def roles_claim_message(ctx):
    embed = discord.Embed(title = f"🦄Hi. Here you can get role🦄", description = """
                          
**Here you can choose a role based on your interests and skills. Just click on the reaction, and the role will appear for you.🚀

In addition, new features and chats will open up for you, of course, both text and voice. I would also like to add that with the number of messages you send on our server, your level increases, which also gives you some rights.🚀

Of course, firstly you will have to complete a survey with the bot so that we can be sure of your adequacy.🚀

It is worth mentioning that in this way you can even get the role of a moderator.🚀**

                          
                          """,  color = discord.Color.orange())
    
    embed.set_author(name = "Universal Creator", icon_url = ctx.author.avatar_url)
    
    guild = ctx.guild
    dev_role = discord.utils.get(guild.roles, name = "Dev")
    gamer_role = discord.utils.get(guild.roles, name = "Gamer")
    musicant_role = discord.utils.get(guild.roles, name = "Musicant")
    doctor_role = discord.utils.get(guild.roles, name = "Doctor")
    artist_role = discord.utils.get(guild.roles, name = "Artist")
    writer_role = discord.utils.get(guild.roles, name = "Writer")
    trader_role = discord.utils.get(guild.roles, name = "Trader")
    businessman_role = discord.utils.get(guild.roles, name = "Businessman")
    designer_role = discord.utils.get(guild.roles, name = "Photograpgher")
    movie_role = discord.utils.get(guild.roles, name = "Movie")
    
    talant_embed = discord.Embed(title = f"Talant roles", description = f"""
                                
**Dev**: ***💻***
**Gamer**: ***🎮***
**Musicant**: ***🎵***
**Doctor**: ***🩺***
**Artist**: ***🎨***
**Writer**: ***🖊***
**Trader**: ***📈***
**Businessman**: ***📥***
**Photographer**: ***📸***
**Movie**: ***🎥***
                                
                                
                                """, color = discord.Color.purple())
    
    await ctx.send(embed = embed)
    
    message = await ctx.send(embed = talant_embed)
    
    await message.add_reaction("💻")
    await message.add_reaction("🎮")
    await message.add_reaction("🎵")
    await message.add_reaction("🩺")
    await message.add_reaction("🎨")
    await message.add_reaction("🖊")
    await message.add_reaction("📈")
    await message.add_reaction("📥")
    await message.add_reaction("📸")
    await message.add_reaction("🎥")
    
    
    
@bot.event
async def on_raw_reaction_add(payload):
    
    guild = bot.get_guild(payload.guild_id)
    
    dev_role = discord.utils.get(guild.roles, name = "Dev")
    gamer_role = discord.utils.get(guild.roles, name = "Gamer")
    musicant_role = discord.utils.get(guild.roles, name = "Musicant")
    doctor_role = discord.utils.get(guild.roles, name = "Doctor")
    artist_role = discord.utils.get(guild.roles, name = "Artist")
    writer_role = discord.utils.get(guild.roles, name = "Writer")
    trader_role = discord.utils.get(guild.roles, name = "Trader")
    businessman_role = discord.utils.get(guild.roles, name = "Businessman")
    designer_role = discord.utils.get(guild.roles, name = "Photograpgher")
    movie_role = discord.utils.get(guild.roles, name = "Movie")
    
    member = payload.member
    guild = bot.get_guild(payload.guild_id)
    
    emoji = payload.emoji.name
    
    if emoji == "💻":
        role = discord.utils.get(guild.roles, name = "Developer")
    elif emoji == '🎮':
        role = discord.utils.get(guild.roles, name = "Gamer")
    elif emoji == "🎵":
        role = discord.utils.get(guild.roles, name = "Musicant")
    elif emoji == "🩺":
        role = discord.utils.get(guild.roles, name = "Doctor")
    elif emoji == "🎨":
        role = discord.utils.get(guild.roles, name = "Artist")
    elif emoji == "🖊":
        role = discord.utils.get(guild.roles, name = "Writer")
    elif emoji == "📈":
        role = discord.utils.get(guild.roles, name = "Trader")
    elif emoji == "📥":
        role = discord.utils.get(guild.roles, name = "Businessman")
    elif emoji == "📸":
        role = discord.utils.get(guild.roles, name = "Photographer")
    elif emoji == "🎥":
        role = discord.utils.get(guild.roles, name = "Movie")

    await member.add_roles(role)
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
    else:
        await ctx.reply("Something went wrong")
        print(error)

bot.run(DISCORD_TOKEN)