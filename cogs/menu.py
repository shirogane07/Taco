import discord
from discord.ext import commands
import os
import asyncio
import json
from core.classes import Cog_Extension
from pathlib import Path



with open("data/url.json", mode = "r", encoding = "utf-8") as ufile :
   udata = json.load(ufile)


class menu(Cog_Extension):
  #taco_menu 塔可菜單
  @commands.command()
  async def taco_menu(self, ctx):
      embed = discord.Embed(
          title="小圭の塔可專賣店",
        url=udata["rick_roll"],
          description=
          "所有餐點皆為現點現做，飲品皆為手沖，製作時間稍長，請各位顧客耐心等候。 *本店只接受 @UnbelievaBoat 指令付款",
          color=0x4dd5a8)
      embed.set_thumbnail(url=udata["taco_staff"])
      embed.add_field(name="=====菜單 =====",
                      value="飲料菜單請透過輸入[t!drinks_menu]獲取",
                      inline=False)
      embed.add_field(name="-----塔可 -----", value="*加起司+$10", inline=False)
      embed.add_field(name="蒜煎牛肉", value="$80", inline=True)
      embed.add_field(name="煙燻雞胸", value="$75", inline=True)
      embed.add_field(name="酥炸豬排", value="$70", inline=True)
      embed.add_field(name="經典海鮮", value="$85  (每日的海鮮都不一樣)", inline=True)
      embed.add_field(name="健康蔬菜", value="$70", inline=True)
      embed.add_field(name="菇菇加倍", value="$80", inline=True)
      embed.add_field(name="每日限定", value="$90  (每天都會更換口味)", inline=True)
      embed.set_footer(text="2022/07/24 by店長小圭")
      await ctx.send(embed=embed)

  #drinks_menu 飲料菜單
  @commands.command()
  async def drinks_menu(self, ctx):
      embed = discord.Embed(
          title="小圭の塔可專賣店",
        url=udata["rick_roll"],
          description=
          "所有餐點皆為現點現做，飲品皆為手沖，製作時間稍長，請各位顧客耐心等候。 *本店只接受 @UnbelievaBoat 指令付款",
          color=0x4dd5a8)
      embed.set_thumbnail(url=udata["taco_staff"])
      embed.add_field(name="=====菜單 =====",
                      value="塔可菜單請透過輸入[t!taco_menu]獲取",
                      inline=False)
      embed.add_field(name="-----飲料 -----",
                      value="*部分飲品只能做冷的或熱的，詳情請洽服務人員。",
                      inline=False)
      embed.add_field(name="阿薩姆紅茶", value="$55", inline=True)
      embed.add_field(name="伯爵紅茶", value="$55", inline=True)
      embed.add_field(name="茉香綠茶", value="$55", inline=True)
      embed.add_field(name="桂花清茶", value="$55", inline=True)
      embed.add_field(name="水果冰茶", value="$65", inline=True)
      embed.add_field(name="經典美式", value="$110", inline=True)
      embed.add_field(name="卡布奇諾", value="$120", inline=True)
      embed.add_field(name="焦糖拿鐵", value="$130", inline=True)
      embed.add_field(name="職人手沖", value="$180", inline=True)
      embed.set_footer(text="2022/07/24 by店長小圭")
      await ctx.send(embed=embed)


async def setup(bot):
  await bot.add_cog(menu(bot))