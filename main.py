import keep_alive
import discord
from discord.ext import commands
import os
import datetime
import pytz
import asyncio
import json
# from discord.ext import tasks
# import datetime as dt
# import aiohttp
# import pandas as pd
# import re
# from bs4 import BeautifulSoup as bs
# import requests
# import urllib.request
# from pathlib import Path

# print('我沒壞，笑死')


#獲取時區
def now_time():
  current_time = datetime.datetime.now()
  timezone = pytz.timezone('Asia/Taipei')
  localized_time = current_time.astimezone(timezone)
  return localized_time.strftime("%Y-%m-%d %H:%M")


#宣告token
token = os.environ['token']

# print('這裡應該也沒有壞掉，笑死')

#intents 偵測意向
intents = discord.Intents.all()
#clientdiscord.Client(intents=intents)

#導入json檔
with open("data/setting.json", mode="r", encoding="utf-8") as jfile:
  jdata = json.load(jfile)
#jdata["欲索引之標題"]

#宣告.json索引的名稱
"Channel_Name：console_taco,Link：https://bit.ly/3SMfU3a"
cID_C = int(jdata["chanelID_Console"])
SBoC = jdata["String_Bot_online_Console"]
SBoCN = jdata["String_Bot_online_Console_None"]
SBoCT = jdata["String_Bot_online_Console_True"]
MBoD = jdata["Msg_Bot_online_Discord"]

# 宣告指令前綴[t!]
bot = commands.Bot(command_prefix='t!', intents=intents)


#online 上線
@bot.event
async def on_ready():
  # print('活著')
  print(SBoC)
  # online_record = open('online_record.txt', 'a', encoding='utf-8')
  # online_record.write(f"{now_time()}\n")
  # online_record.close()  2024/04/29 因掛線註解
  call_channel = bot.get_channel(cID_C)
  #await call_channel.send("報告老闆，已經備好料可以開店了")  #有空修改成embed格式
  if call_channel is None:  #確認頻道狀態
    print(SBoCN)
  else:
    print(SBoCT, call_channel)
    await call_channel.send(MBoD)


# print('那這裡還活著嗎')


@bot.command()
async def load(ctx, extension):
  await bot.load_extension(f"cogs.{extension}")
  await ctx.send(f"已載入{extension}")


@bot.command()
async def unload(ctx, extension):
  await bot.unload_extension(f"cogs.{extension}")
  await ctx.send(f"已卸載{extension}")


@bot.command()
async def reload(ctx, extension):
  await bot.reload_extension(f"cogs.{extension}")
  await ctx.send(f"已重新載入{extension}")


"從楊那裡copy過來的，要修改"
"已修改完畢 12/15 1130 BY 秋菜"


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f'抱歉，能請您再說一次您需求嗎？')
  elif isinstance(error, commands.CommandNotFound):
    await ctx.reply(f'抱歉，我無法理解您想表達的意思。')
  else:
    await ctx.reply(f'抱歉，我無法理解您想表達的意思。{error}')


async def load_extensions():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
  async with bot:
    await load_extensions()
    await bot.start(token)


# for cog in [p.stem for p in Path(".").glob("./cogs/*.py")]:
#   bot.load_extension(f'cogs.{cog}')
#   print(f'Loaded {cog}.')
# print('Done.')

if __name__ == "__main__":
  asyncio.run(main())

keep_alive.keep_alive()
bot.run(token)