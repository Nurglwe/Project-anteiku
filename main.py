import discord, requests, tools, os
from discord.ext import commands
from bs4 import BeautifulSoup

intents = discord.Intents.all() # Imports all the Intents
intents.members=True
client = commands.Bot(command_prefix="->",intents=intents)

#do discord stuff or import my discord tools

@client.event
async def on_ready():
  print("ready")


@client.command()
async def ping (ctx):
  await ctx.channel.send("Pong")

@client.command()
@commands.has_role("Mod")
async def pulltheobjects(ctx):
  derp = tools.alltheobject(client)
  await ctx.channel.send("Alliop,{},{}".format(str(derp.guild.id), str(derp.delc.id)))

@client.command()
async def wikisearch(ctx):
  await ctx.channel.send("If only it were this easy")

@client.command()
async def charbranches(ctx):
  re = requests.get('https://tokyoghoul.fandom.com/wiki/Category:Characters')
  print(re.status_code)
  r = BeautifulSoup(re.content,'html.parser')
  scp=r.find(class_="mw-content-ltr")
  scp=scp.find_all(class_="category-page__member-link")
  names = ""
  for item in scp:
    names="{}, {}".format(names,item.text)

  await ctx.channel.send(names[1:int(len(names)/2)])
  await ctx.channel.send(names[int(len(names)/2):])
  
@client.command()
async def locbranches(ctx):
  re = requests.get('https://tokyoghoul.fandom.com/wiki/Category:Locations')
  print(re.status_code)
  r = BeautifulSoup(re.content,'html.parser')
  scp=r.find(class_="mw-content-ltr")
  scp=scp.find_all(class_="category-page__member-link")
  names = ""
  for item in scp:
    names="{}, {}".format(names,item.text)

  await ctx.channel.send(names[1:])

@client.command()
async def getall(ctx):
  await ctx.channel.send('Please fucking kill me')

token=os.getenv("TOKEN")    
client.run(token)

