import discord
from discord.ext import commands
from main import * 

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #Create role
    @commands.has_permissions(administrator = True)
    @commands.command(aliases = ['make_role', 'cr'])
    @commands.Cog.listener()
    async def create_role(self, ctx, name):
        guild = ctx.guild
        
        await guild.create_role(name = name)
        await ctx.send(f"Role {name} was successfully created")


    @commands.command(aliases = ['delrole', 'dr'], pass_context = True)
    @commands.has_permissions(administrator = True)
    @commands.Cog.listener()
    async def delete_role(ctx, name):
        role_object = discord.utils.get(ctx.message.guild.roles, name = name)
        await role_object.delete()
        await ctx.send(f"Role {name} was successfully deleted")
    
    
    @commands.command(aliases = ['deluserrole', 'dur'], pass_context = True)
    @commands.has_role('staff')
    async def mute(ctx, user: discord.Member):
        role_get = get(member.guild.roles, id=role_id) 
        await member.remove_roles(role_get) 
        await bot.say("{} has been muted from chat".format(user.name))
        
    #Role claim messages
    @commands.has_permissions(administrator = True)
    @commands.command(aliases = ['rcm'])
    async def roles_claim_message(self, ctx):
        embed = discord.Embed(title = f"🦄Hi. Here you can get role🦄", description = """
                            
    **Here you can choose a role based on your interests and skills. Just click on the reaction, and the role will appear for you.🚀

    In addition, new features and chats will open up for you, of course, both text and voice. I would also like to add that with the number of messages you send on our server, your level increases, which also gives you some rights.🚀

    Of course, firstly you will have to complete a survey with the bot so that we can be sure of your adequacy.🚀

    It is worth mentioning that in this way you can even get the role of a moderator.🚀**

                            
                            """,  color = discord.Color.orange())
        
        embed.set_author(name = "Universal Creator", icon_url = ctx.author.avatar_url)
        
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
    **NFT Collector**: ***💸***
                                    
                                    
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
        await message.add_reaction("💸")
        
        
    #Getting role on reaction press
    @bot.event
    async def on_raw_reaction_add(payload):
        
        guild = bot.get_guild(payload.guild_id)
        member = payload.member
        emoji = payload.emoji.name
        
        if emoji == "💻":
            role = discord.utils.get(guild.roles, name = "Dev")
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
        elif emoji == "💸":
            role = discord.utils.get(guild.roles, name = "NFT Collector")
        
        await member.add_roles(role)

    #Deleting role on reaction repress    
    @bot.event
    async def on_raw_reaction_remove(payload):
        guild = bot.get_guild(payload.guild_id)
        member = payload.member
        emoji = payload.emoji.name
        
        if emoji == "💻":
            role = discord.utils.get(guild.roles, name = "Dev")
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
        elif emoji == "💸":
            role = discord.utils.get(guild.roles, name = "NFT Collector")
            
            
        if role is not None: 
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None: 
                await member.remove_roles(role)
            else: 
                print("Member not found")
        else: 
            print("Role not found")
        
      
def setup(bot):
  bot.add_cog(Roles(bot))