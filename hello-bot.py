import discord

TOKEN = "MTE1Njk0NDEyMDcyODc4OTAyMw.Grrjzf.yB3inbx3wFPsZEmP8F3fIT8vdvZYm-liON6r-k"
CHANNELID = "1156943911818891286"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Startup Success!!!')

@client.event
async def on_message(message):
    if message.content.startswith("hello"):
        m = "こんにちは、" + message.author.name + "さん"
        await message.channel.send(m)

client.run(TOKEN)