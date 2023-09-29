import discord
from googlesearch import search
import asyncio

TOKEN = "MTE1Njk0NDEyMDcyODc4OTAyMw.Grrjzf.yB3inbx3wFPsZEmP8F3fIT8vdvZYm-liON6r-k"
#CHANNELID = "1156943911818891286"

client = discord.Client(intents=discord.Intents.all())

ModeFlag = ''
phasmo_evidence = '・EMFレベル5' + '　　　　　　　　       ' + '・D.O.T.Sプロジェクター\n' + '・紫外線' + '　　　　　　　　　　　　' + '・ゴーストオーブ\n' + '・ゴーストライティング' + '　　　　　' + '・スピリットボックス\n' + '・氷点下の温度'
phasmo_end = '幽霊調査を終了するには' + '\N{Ghost}' + 'にリアクションをつけてね！'
phasmo_evidence_reactions = ['\N{Antenna with Bars}', '\N{Large Purple Circle}', '\N{Memo}', '\N{Video Camera}', '\N{Radio}', '\N{Thermometer}', '\N{Large Green Circle}']
Spirit = ['\N{Antenna with Bars}', '\N{Memo}', '\N{Radio}']
Wraith = ['\N{Antenna with Bars}', '\N{Radio}', '\N{Large Green Circle}']
Phantom = ['\N{Large Purple Circle}', '\N{Radio}', '\N{Large Green Circle}']
Poltergeist = ['\N{Large Purple Circle}', '\N{Memo}', '\N{Radio}']
Banshee = ['\N{Large Purple Circle}', '\N{Video Camera}', '\N{Large Green Circle}']
Jinn = ['\N{Antenna with Bars}', '\N{Large Purple Circle}', '\N{Thermometer}']
Mare = ['\N{Memo}', '\N{Video Camera}', '\N{Radio}']
Revenant = ['\N{Memo}', '\N{Video Camera}', '\N{Thermometer}']
Shade = []
Demon = []
Yurei = []
Oni = []
Hantu = []
Yokai = []
Goryo = []
Myling = []
Onryo = []
Twins = []
Raiju = []
Obake = []
Mimic = []
Moroi = []
Deogen = []
Theye = ['\N{Memo}', '\N{Video Camera}', '\N{Large Green Circle}']
phasmo_ghost = [Spirit, Wraith, Phantom, Poltergeist, Banshee, Jinn, Mare, Revenant, Shade, Demon, Yurei, Oni, Hantu, Yokai, Goryo, Myling, Onryo, Twins, Raiju, Obake, Mimic, Moroi, Deogen, Theye]
phasmo_ghost_jp = ['スピリット', 'レイス', 'ファントム', 'ポルターガイスト', 'バンシー', 'ジン', 'メアー', 'レブナント', 'シェード', 'デーモン', '幽霊', '鬼', 'ハントゥ', '妖怪', '御霊', 'マイリング', '怨霊', 'ツインズ', '雷獣', '化け狐', 'ミミック', 'モーロイ', 'デオヘン', 'セーイ']

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

    #if message.author == client.user:
    #    return
    
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

    if message.content == '/google': #google検索機能 https://qiita.com/o-chang/items/e45fb7074654f8eb26ea
        ModeFlag = 'google'
        await message.channel.send('検索するワードをチャットで発言してね')

    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '/phasmo': #phasmophobiaのジャーナル機能 リアクションカウント機能：https://teratail.com/questions/lpnb85ouqbvhfj
        #ModeFlag = 'phasmo'
        await message.channel.send('幽霊調査開始！')
        phasmo_evidence_message = await message.channel.send(phasmo_evidence)
        for i in range(7):
            await phasmo_evidence_message.add_reaction(phasmo_evidence_reactions[i])
        phasmo_end_message = await message.channel.send(phasmo_end)
        await phasmo_end_message.add_reaction('\N{Ghost}')

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.content == phasmo_end and user != client.user:
        message = await phasmo_evidence_message.channel.fetch_message(phasmo_evidence_message.id)
        evidence_list = []
        await reaction.message.channel.send('今回出た証拠は、')
        for i in range(7):
            if message.reactions[i].count != 1:
                evidence_list.append(phasmo_evidence_reactions[i])
                await reaction.message.channel.send(phasmo_evidence_reactions[i])
        await reaction.message.channel.send('今回のゴーストは...')
        print(evidence_list)
        for i in range(24):
            if evidence_list == phasmo_ghost[i]:
                await reaction.message.channel.send(phasmo_ghost_jp[i] + '！')

        
client.run(TOKEN)