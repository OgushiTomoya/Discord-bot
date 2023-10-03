import discord
from googlesearch import search
import asyncio
import os
from dotenv import load_dotenv

import phasmo

load_dotenv()

client = discord.Client(intents=discord.Intents.all())

ModeFlag = ''

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
    global phasmo_evidence_message

    if message.author == client.user:
        return
    
    if ModeFlag == 'google':
        ModeFlag = ''
        search_key = message.content
        count = 0
        # 日本語で検索した上位5件を順番に表示
        for url in search(search_key, lang="jp",num = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
               break

    if message.content.startswith("hello"):
        m = "こんにちは、" + message.author.display_name + "さん"
        await message.channel.send(m)

    if message.content == '/google': #google検索機能
        ModeFlag = 'google'
        await message.channel.send('検索するワードをチャットで発言してね')

    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '/phasmo': #phasmophobiaのジャーナル機能
        #ModeFlag = 'phasmo'
        await message.channel.send('幽霊調査開始！')
        phasmo_evidence_message = await message.channel.send(phasmo.evidence)
        for i in range(7):
            await phasmo_evidence_message.add_reaction(phasmo.evidence_reactions[i])
        phasmo_end_message = await message.channel.send(phasmo.end)
        await phasmo_end_message.add_reaction('\N{Ghost}')

    if message.content == '/map':
        await message.channel.send('https://phasmo.karotte.org/maps/10-ridgeview-court/10-ridgeview-court.svg')

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.content == phasmo.end and user != client.user:
        message = await phasmo_evidence_message.channel.fetch_message(phasmo_evidence_message.id)
        evidence_list = []
        await reaction.message.channel.send('今回出た証拠は、')
        for i in range(7):
            if message.reactions[i].count != 1:
                evidence_list.append(phasmo.evidence_reactions[i])
                await reaction.message.channel.send(phasmo.evidence_reactions[i])
        print(evidence_list)
        for i in range(24):
            if evidence_list == phasmo.ghost_name[i]:
                await reaction.message.channel.send('今回のゴーストは...　　　' + phasmo.ghost_name_jp[i] + '！')
                break
            if i == 23:
                await reaction.message.channel.send('条件に合うゴーストはいないなぁ...')

        
client.run(os.getenv('TOKEN'))