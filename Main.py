import discord
from discord.ext import commands
import random
import asyncio
import os
import inspect

bot = commands.Bot(command_prefix="*")
bot.remove_command("help")

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="watching Dark Oufa's server | Playing Fortnite"))
	print("Logged in as")
	print(bot.user.name)
	print(bot.user.id)
	
@bot.event
async def on_member_join(member):
	server = member.server
	channel = bot.get_channel("667003683262824468")
	embed = discord.Embed(title="👋 {} just joined {}".format(member.name, server.name), description="Welcome! to {} {}! Enjoy your stay here!".format(server.name, member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member Count", value=member.server.member_count)
	await bot.send_message(channel, embed=embed)

@bot.event
async def on_member_remove(member):
	channel = bot.get_channel("667003683262824468")
	embed = discord.Embed(title="👋 {} just left the server.".format(member.name), description="Goodbye! {} hope to see you again".format(member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member Count", value=member.server.member_count)
	await bot.send_message(channel, embed=embed)
	
@bot.command(name="mute", pass_context=True)
@commands.has_permissions(kick_members=True, administrator=True)
async def _mute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("Usage: `{}mute [member] [reason]`".format(ctx.prefix))
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Muted")
	await bot.add_roles(user, role)
	embed = discord.Embed(title="Mute", description=" ", color=0xFFA500)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_mute.error
async def mute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(name="unmute", pass_context=True)
@commands.has_permissions(kick_members=True, administrator=True)
async def _unmute(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say("Usage: `{}unmute [member] [reason]`".format(ctx.prefix))
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Muted")
	await bot.remove_roles(user, role)
	embed = discord.Embed(title="Unmute", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_unmute.error
async def unmute_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

@bot.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def _kick(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say('Usage: `{}kick [member] [reason]`'.format(ctx.prefix))
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	await bot.kick(user)
	embed = discord.Embed(title="Kick", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_kick.error
async def kick_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
  
@bot.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members=True)
async def _ban(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say('Usage: `{}ban [member] [reason]`'.format(ctx.prefix))
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.ban_members:
		return False
	reason = arg
	author = ctx.message.author
	await bot.ban(user)
	embed = discord.Embed(title="Ban", description=" ", color=0xFF0000)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	
@_ban.error
async def ban_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `ban_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(name="warn", pass_context=True)
@commands.has_permissions(manage_messages=True, kick_members=True)
async def _warn(ctx, user: discord.Member = None, *, arg = None):
	if user is None:
		await bot.say('Usage: `{}warn [member] [reason]`'.format(ctx.prefix))
		return False
	if arg is None:
		await bot.say("please provide a reason to {}".format(user.name))
		return False
	if user.server_permissions.kick_members:
		return False
	reason = arg
	author = ctx.message.author
	server = ctx.message.server
	embed = discord.Embed(title="Warn", description=" ", color=0x00ff00)
	embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
	embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
	embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
	await bot.say(embed=embed)
	await bot.send_message(user, "You have been warned for: {}".format(reason))
	await bot.send_message(user, "from: {} server".format(server))
	
@_warn.error
async def warn_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have requirement permission to use this command `kick_members`.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
	
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True, ban_members=True, administrator=True)
async def unban(ctx, user:int):
	try:
		who=await bot.get_user_info(user)
		await bot.unban(ctx.message.server, who)
		await bot.say("User has been unbanned")
	except:
		await bot.say("Something went wrong")
		
def user_is_me(ctx):
	return ctx.message.author.id == "601622622957994006"		

@bot.command(name='eval', pass_context=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await bot.say(await res)
    else:
        await bot.delete_message(ctx.message)
        await bot.say(res)
	
@bot.command(pass_context=True)
@commands.check(user_is_me)
async def leave(ctx, *args):
	server = bot.get_server(*args)
	await bot.leave_server(server)
	
@bot.command()
@commands.check(user_is_me)
async def servers():
    for server in bot.servers:
        embed = discord.Embed(description="Server Name: {}, Server ID: {}".format(server.name, server.id))
        await bot.say(embed=embed)
	
@bot.command(name="clean", pass_context=True, no_pm=True)
@commands.has_permissions(manage_messages=True)
async def _clean(ctx, amount=100):
    channel = ctx.message.channel
    messages = [ ]
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    msg = await bot.say(f"{amount} message has been deleted.")
    await asyncio.sleep(5)
    await bot.delete_message(msg)
	
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member = None):
	if user is None:
		user = ctx.message.author
	roles = [role for role in user.roles]
	embed = discord.Embed(colour=user.colour, timestamp=ctx.message.timestamp)
	embed.set_author(name=user)
	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
	embed.add_field(name="ID:", value=user.id)
	embed.add_field(name="Guild name:", value=user.display_name)
	embed.add_field(name="Created at:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
	embed.add_field(name="Joined at:", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
	embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
	embed.add_field(name="Top role:", value=user.top_role.mention)
	await bot.send_message(ctx.message.channel, embed=embed)
	
@bot.command(name="kill", pass_context=True)
async def _kill(ctx, user: discord.Member = None):
	if user is None:
		await bot.say("Usage: `{}kill [member] [reason]`".format(ctx.prefix))
		return False
	author = ctx.message.author
	embed = discord.Embed(title="Yandere Push", url="https://i.imgur.com/Yok3zm8.gif", description="Oof", color=0x00ff00)
	embed.set_Image(url="https://i.imgur.com/Yok3zm8.gif")
	await bot.say(embed=embed)

bot.run(os.environ['BOT_TOKEN'])
