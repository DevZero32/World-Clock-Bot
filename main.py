import os
import discord
from discord.ext import commands
import json
import time
import datetime
import calendar

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
  return "Not found"

async def epoch(Rtime,day,month,year,offset,ctx):
  hours = int(Rtime[0:2])
  mins = int(Rtime[3:])

  if hours > 23 or hours < 0 or mins < 0 or mins > 59:
    await ctx.send(f"Time error")
    return
  if not year.isnumeric() or not month.isnumeric():
    await ctx.send(f"How to use: `/date [timezone] [year] [month] [day] ")
    return
  year = int(year)
  if year >= 2038:
    await ctx.send(f"Maxium year reached.")
    return
  month = int(month)
  day = int(day)
  if offset < 0:
    hours = hours + offset
  else:
    hours = hours - offset
  mins = int(mins)

  date_time = datetime.datetime(year,month,day,hours,mins,0,0)
  epochtime = round(time.mktime(date_time.timetuple()))
  return epochtime

@client.command()
async def default(ctx,tz,Rtime,day,month,year):
  offset = findTz(tz)
  epochtime = await epoch(Rtime,day,month,year,offset,ctx)
  await ctx.send(f"`<t:{epochtime}>`")
  
@client.command()
async def shorttime(ctx,tz,Rtime,day,month,year):
  offset = findTz(tz)
  epochtime = await epoch(Rtime,day,month,year,offset,ctx)
  await ctx.send(f"`<t:{epochtime}:t>`")

@client.command()
async def longtime(ctx,tz,Rtime,day,month,year):
  offset = findTz(tz)
  epochtime = await epoch(Rtime,day,month,year,offset,ctx)
  await ctx.send(f"`<t:{epochtime}:F>`")

@client.command()
async def shortdate(ctx,tz,Rtime,day,month,year):
  offset = findTz(tz)
  epochtime = await epoch(Rtime,day,month,year,offset,ctx)
  await ctx.send(f"`<t:{epochtime}:d>`")

@client.command()
async def longdate(ctx,tz,Rtime,day,month,year):
  offset = findTz(tz)
  epochtime = await epoch(Rtime,day,month,year,offset,ctx)
  await ctx.send(f"`<t:{epochtime}:D>`")

@client.command()
async def relative(ctx,tz,Rtime,day,month,year):
  offset = findTz(tz)
  if offset == "Not found":
    await ctx.send("Timezone not found.")
  epochtime = await epoch(Rtime,day,month,year,offset,ctx)
  await ctx.send(f"`<t:{epochtime}:R>`")

@client.command()
async def commands(ctx):
  main = """
**How to use**

`/default {24 hour digital time} {day} {month} {year}`

**Commands**

/default  = November 28, 2018 9:01 / AM

/relative  = 3 years ago

/shorttime = 9:01 / AM 
  
/longtime = Wednesday, November 28, 2018 9:01 / AM

/shortdate = 	11/28/2018 or 28/11/2018

/longdate = November 28, 2018 or 	28 November 2018
"""
  
  embed = discord.Embed(title="Commands",description=main,color=discord.Colour.blue())
  await ctx.send(embed=embed)

client.run(token)