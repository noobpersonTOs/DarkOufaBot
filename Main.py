import discord
from discord.ext import commands
import os

@bot.event
async def on_ready():
  print("Logged in as")
  print(bot.user.name)
  print(bot.user.id)
  
@bot.command()
async def wave(ctx):
  await ctx.send("Hi 👋")
  
bot.run(os
