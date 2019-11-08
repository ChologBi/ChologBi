 import discord
 import os

 client = discord.Client()


 @client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game - discord.Game(".도움")
    await client.change_presence(status=discord.Status.online, activity=game)


 @client.event
async del on_message(message):
    if message.content.startswith("안녕")
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("ㅎㅇ")
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("초록")
        await message.channel.send("초록크..?")
    if message.content.startswith("어떰")
        await message.channel.send("좋음")
    if message.content.startswith("심심")
        await message.channel.send("나도 심심")
     
 
 access_token = os.environ["BOT_TOKEN"]
 client.run("access_token")
