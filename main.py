import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="uc!")

hello_message = ['hello']

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(aliases=['clean', 'cleaning', 'cls'], brief="Clear chat from message. 10 Messages by default", usage="clear <amount=10>")
async def clear(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Was deleted {amount} messages...")



"""
@bot.command(name="очистить", brief="Очистить чат от сообщений, по умолчанию 10 сообщений", usage="clear <amount=10>")
async def clear(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Was deleted {amount} messages...")"""


bot.run(DISCORD_TOKEN)
