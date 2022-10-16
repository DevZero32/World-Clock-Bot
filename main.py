import os
import discord
from discord.ext import commands
import json
import time

client = commands.Bot(command_prefix="/",intents = discord.Intents.all())
token = os.environ["token"]


def load_tz():
  with open("timezones.json", "r") as file:
    Timezone = json.loads(file.read())
    return Timezone

def findTz(tz):
  Timezone = load_tz()
  for timezone in Timezone:
    if timezone["abbr"] == tz:
      return timezone["offset"]



@client.command()
async def stime(ctx,arg):
  offset = int(arg)
  epochtime = round(time.time())
  for hour in range(offset):
    epochtime = epochtime + 3600
  await ctx.send(f"<t:{round(time.time())}:t>")




@client.command()
async def date(ctx,tz,Rtime):
  offset = findTz(tz)
  print(offset)
  epochtime = round(time.time())
  for hour in range(offset):
    epochtime = epochtime + 3600
  await ctx.send(f"<t:{round(time.time())}:D>")




@client.command()
async def week(ctx,arg):
  offset = int(arg)
  epochtime = round(time.time())
  for hour in range(offset):
    epochtime = epochtime + 3600
  await ctx.send(f"<t:{epochtime}:F>")













client.run(token)