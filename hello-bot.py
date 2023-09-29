import discord
from googlesearch import search

TOKEN = "MTE1Njk0NDEyMDcyODc4OTAyMw.Grrjzf.yB3inbx3wFPsZEmP8F3fIT8vdvZYm-liON6r-k"
CHANNELID = "1156943911818891286"

client = discord.Client(intents=discord.Intents.all())

ModeFlag = 0

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Startup Success!!!')

@client.event
async def on_message(message):
    global ModeFlag

    if message.author.bot:
        return
    
    if ModeFlag == 1:
        ModeFlag = 0
        search_key = message.content
        count = 0
        # 日本語で検索した上位5件を順番に表示
        for url in search(search_key, lang="jp",num = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
               break

    if message.content.startswith("hello"):
        m = "こんにちは、" + message.author.name + "さん"
        await message.channel.send(m)

    if message.content == '!google': #google検索機能 https://qiita.com/o-chang/items/e45fb7074654f8eb26ea
        ModeFlag = 1
        await message.channel.send('検索するワードをチャットで発言してね')

client.run(TOKEN)