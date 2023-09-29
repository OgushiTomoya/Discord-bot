# Discord-bot
README書き方  https://docs.github.com/ja/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

9/28

Discord bot制作開始

clientのintents部分難あり，Discordのウェブサイトの方での設定で許可する必要あり

・helloというと返事が返ってくる機能

9/29

・google検索を追加　https://qiita.com/o-chang/items/e45fb7074654f8eb26ea

`if ModeFlag == 1:`部分を`if message.content == '/google'`の後ろに置くと，/googleで検索されてしまう

hello機能の返事内容を，ユーザ名(makiron0910)から表示名(サーバーでの名前)に変更

・phasmo機能を追加（ジャーナル）　作業時間：4時間

ゴーストの証拠部分のコピペ作業が残ってる

リストの定義とかを別のファイルで定義出来たらコードの情報量少なくできるかも
