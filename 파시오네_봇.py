import discord
import asyncio
import random
import requests
import people
import datetime
import random

from bs4 import BeautifulSoup
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
botname = 'Pacione Bot'
embedcolor = 0x62c1cc
bot.remove_command('help')

@bot.event
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!help"))
    print("New log in as {0.user}".format(bot))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'실행 할 수 있는 권한이 없거나 알 수 없는 명령어 입니다.')
    pass

@bot.command(name='h' or 'help', pass_context=True)
async def help(ctx):
    embed  = discord.Embed(title= botname ,timestamp=datetime.datetime.utcnow(), color=embedcolor)
    embed.add_field (value= '봇 명령어 표시', name='!help ', inline=False)
    embed.add_field (value= '룰렛 (제작중)', name='!룰렛', inline=False)
    embed.add_field (value= '사다리타기(제작중)', name='!사다리타기', inline=False)
    embed.add_field (value= '랜덤숫자', name='!랜덤숫자', inline=False)
    embed.add_field (value= '초대 링크', name='!초대링크', inline=False)
    embed.add_field (value= '롤 전적', name='!롤전적', inline=False)
    embed.add_field (value= '2020 LOL World Championship 정보', name='!2020LOL', inline=False)
    embed.add_field (value= '채팅창 청소', name='!clear', inline=False)
    embed.add_field (value= '뮤트(제작중)', name='!', inline=False)
    embed.add_field (value= '진실의 방으로(제작중)', name='!', inline=False)
    embed.add_field (value= '봇 대답 테스트 명령어', name='!ping', inline=False)
    embed.add_field (value= '사용자 정보 보여주기(제작중)', name='!ui', inline=False)
    embed.add_field (value= '서버 정보 보여주기(제작중)', name='!sui', inline=False)
    embed.add_field (value= '사용자 프로필 사진 보여주기(제작중)', name='!avatar', inline=False)
    embed.add_field (value= '봇 사진 보여주기', name='!botavatar', inline=False)
    embed.set_footer (text=f'특정 명령에 대한 자세한 내용을 보려면 !h [명령어]을 입력하세요. 요청자 [{ctx.message.author}] ')
    await ctx.send(embed=embed)
    
@bot.command(name='clear', pass_context=True)
@commands.has_role(749283664533127258)
async def message_clear(ctx, *, amount=1):
    await ctx.channel.purge(limit=amount+1)
    embed  = discord.Embed(title= botname ,timestamp=datetime.datetime.utcnow(), color=embedcolor)
    embed.add_field(value= f'요청자 : {ctx.message.author}', name=f'총 {amount}개의 메세지를 삭제 했습니다.', inline=False)
    await ctx.send(embed=embed)
    
@bot.command(name='ping', pass_context=True)
async def ping(ctx):
    embed  = discord.Embed(title= botname,timestamp=datetime.datetime.utcnow(), color=embedcolor)
    embed.add_field(value= f'{round(bot.latency * 1000)}ms', name='ping(응답 속도)', inline=False)
    await ctx.send(embed=embed)

@bot.command(name='초대링크', pass_context=True)
async def Invitation(ctx):
    embed  = discord.Embed(title= 'Pacione 초대 링크', timestamp=datetime.datetime.utcnow(), color=embedcolor)
    embed.add_field(value= f'요청자 : {ctx.message.author}', name='파시오네의 초대 링크 : https://discord.gg/ztvzGxZ ', inline=False)
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command(name='랜덤숫자', pass_context=True)
async def randomNum(ctx, num1, num2):
    picked = random.randint(int(num1), int(num2))
    embed  = discord.Embed(title= '뽑힌 숫자는 : '+str(picked), color=embedcolor)
    await ctx.send(embed=embed)

@bot.command(name='bot avatar', pass_context=True)
async def avatar(ctx):
    embed  = discord.Embed(title= botname, color=embedcolor)
    embed.add_field(value= f'[링크](https://cdn.discordapp.com/attachments/489337164468060160/743866851397992458/Fa-Q_bot.png)', name='Pacione Bot Avatar', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/489337164468060160/743866851397992458/Fa-Q_bot.png')
    await ctx.send(embed=embed)

@bot.command(name='2020LOL')
async def LOL(ctx):
    embed  = discord.Embed(title= '2020 LOL World Championship', color=embedcolor)
    embed.add_field(value= f'wadawd', name=f'[2020 LOL World Championship](https://lolesports.com/)', inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/754765689729843310/754765707916476506/worldsannouncement-1600x900-v1.0.jpg")
    await ctx.send(embed=embed)

    
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
