import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

bot = commands.Bot(command_prefix = '+', case_insensitive=True)
bot.remove_command('help')



@bot.event
async def on_ready():
       print("hey!i am ready to go")


@bot.event    
async def on_message(message):
    for x in message.mentions:
        if(x==bot.user):
            await message.channel.send(f"hey  did someone mention me?")

    await bot.process_commands(message)



#the bot is made with python version 3.8. you can use this source code to make your own project or you can learn from this code
#made by GAMER.IO_PC EXPERT#2004 
#id - 734364106848469074
#give your token in bot and host it or run it by your local network
#type python main.py to run it in local host


@bot.command(pass_context = True)
async def ping(ctx):
    await ctx.send(f'**Here is your Ping:** `{round(bot.latency * 1000)}ms`')  

@bot.command(aliases=['av'])
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(
        
        color = discord.Color.red()
        
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)


@bot.command(aliases=['user'])    
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)




@bot.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=2):
        await ctx.channel.purge(limit=amount)
        ok = await ctx.send("cleared messages")
        await ctx.delete(ok)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


@bot.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*,reason= "No reason Provided"):
        await member.kick(reason=reason)
        await ctx.send(member.name + " has been kicked from the server, Because of "+reason)


@bot.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,reason= "No reason Provided"):
        await member.ban(reason=reason)
        await ctx.send(member.name + " has been banned from the server, Because of "+reason)



@bot.command(pass_context=True)
async def add(ctx, member: discord.Member = None, role: discord.Role = None):
    await ctx.add_roles(member, role)
    print(f'{member} was given {role}.')


@bot.command(aliases=['server'])
async def serverinfo(ctx, guild: discord.Guild = None):
    guild = ctx.message.guild
    roles =[role for role in guild.roles]
    text_channels = [text_channels for text_channels in guild.text_channels]
    embed = discord.Embed(title=f'{guild.name} information ', timestamp=ctx.message.created_at, color=discord.Color.red())
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Number of Channels:", value=f"{len(text_channels)}")
    embed.add_field(name="Number of Role:", value=f"{len(roles)}")
    embed.add_field(name="Number of Booster:", value=guild.premium_subscription_count)
    embed.add_field(name="Number of Members:", value=guild.member_count)
    embed.add_field(name="Year of foundation:", value=guild.created_at)
    embed.add_field(name="Server Owner:", value=guild.owner)
    embed.set_footer(text=f"command used by {ctx.author}.", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)



@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.message.delete()
    await ctx.send(mesg)



@bot.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*, member):
	banned_user = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')


	for ban_entry in banned_user:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
			return




    
@bot.command()
@commands.has_permissions(administrator=True)
async def dmuser(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)
    await ctx.send(f"Sent Message to {member}")

    

bot.run("your bot token here")                
