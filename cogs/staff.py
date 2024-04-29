import discord
from discord.ext import commands
import os
import asyncio
import json
from core.classes import Cog_Extension
from pathlib import Path



with open("data/url.json", mode = "r", encoding = "utf-8") as ufile :
   udata = json.load(ufile)


class staff(Cog_Extension):
  #staff_manage 後臺管理
  @commands.command()
  async def staff_manage(self, ctx):
      embed = discord.Embed(title="小圭の塔可專賣店",
                              url=udata["rick_roll"],
                              description="非本店相關人士，請勿使用上述指令",
                              color=0x4dd5a8)
      embed.set_thumbnail(url=udata["taco_staff"])
      embed.add_field(name="t!assist", value="開啟協助表格", inline=False)
      embed.add_field(name="t!taco_menu", value="開啟塔可菜單", inline=False)
      embed.add_field(name="t!drinks_menu", value="開啟飲料菜單", inline=False)
      embed.add_field(name="t!greet", value="招呼客人用", inline=False)
      embed.add_field(name="t!serve", value="上菜時用", inline=False)
      embed.add_field(name="t!clear", value="清除訊息用", inline=False)
      await ctx.message.delete()
      await ctx.send(embed=embed)

  #assist 協助
  @commands.command()
  async def assist(self, ctx):
      embed = discord.Embed(title="小圭の塔可專賣店",
                            url=udata["rick_roll"],
                            description="歡迎使用本bot的教學功能,以下將教您如何使用指令點餐",
                            color=0x4dd5a8)
      embed.set_thumbnail(url=udata["taco_staff"])
      embed.add_field(name="t!assist", value="開啟本清單", inline=False)
      embed.add_field(name="t!taco_menu", value="開啟塔可菜單", inline=False)
      embed.add_field(name="t!drinks_menu", value="開啟飲料菜單", inline=False)
      await ctx.send(embed=embed)
  
  #greet 招呼
  @commands.command()
  async def greet(self, ctx):
      await ctx.message.delete()
      await ctx.send(f'歡迎來到小圭的塔可店!')

  #serve 上菜
  @commands.command()
  async def serve(self,ctx):
      await ctx.message.delete()
      await ctx.send(f'上菜囉~小心燙!')
  
  #clear 清除訊息
  @commands.command()
  async def clear(self,ctx, num : int):
      await ctx.channel.purge(limit = num + 1)
      await ctx.send(f'報告店長已為您清除 {num} 則訊息。')


async def setup(bot):
  await bot.add_cog(staff(bot))