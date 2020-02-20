import discord
from discord.ext import commands

client = commands.Bot(command_prefix='~')
# discord에서 사용할 명령어 접두사를 말합니다. ex) ~help
client.remove_command('help')
# help를 새로 만들기 위해 기본 명령어인 help를 제거합니다.

token = "Njc5NDg5MzU3NzczNzk5NDM0.Xk0UAA.ZNMdF03CtUyVo1javrhY-2NBxzk"


# input your Token을 지우고 여러분의 토큰을 넣어주세요.

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('코딩'))
    print("Bot status :: online")


# 봇이 켜지면, 봇의 상태메시지를 TestBot으로 바꾼 후, 콘솔에 로그를 찍습니다.

@client.event
async def on_message(message):
        if message.content.startswith("안녕"):
            await message.channel.send("그래~반가워~")

        if message.content.startswith("Love you"):
            await message.channel.send("Me too")

        


client.run(token)