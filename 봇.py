import discord
import os

client = discord.Client()

@client.event
async def on_ready():
        print(client.user.id)
        print("ready")
        game = discord.Game("코딩")
        await client.change_presence(status=discord.Status.idle,activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("그래, 반가워")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await  message.channel.send(file=discord.File(pic))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
