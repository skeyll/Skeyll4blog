#<copyright>
#  Copyright (c) 2019 Skeyll All Rights Reserved.
#  https://skeyll.hateblo.jp/entry/PrincessConnect
#  Released under the MIT license.
#  see https://opensource.org/licenses/MIT
#</copyright>

import discord

TOKEN = 'TOKENID'

client = discord.Client()

BossNum = ["1","2","3","4","5"]
# If someone reserve an attack, add to this list.
Booking1 = []
Booking2 = []
Booking3 = []
Booking4 = []
Booking5 = []

@client.event
async def on_message(message):
    listFlag = 0
    bookFlag = 0
    endFlag = 0
    displayFlag = 0
    
    if message.content.startswith("rsv"):
       if "list" in message.content: # Call a list
           listFlag = 1
       elif "END" in message.content: # Initialize all lists
           endFlag = 1
       elif "!" in message.content: # Call all arrays
           displayFlag = 1
       else: # Book
           bookFlag = 1

       if listFlag == 1:
           for Boss in BossNum:
               tmpList = []
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  tmpList = [x[0] for x in eval(BookList)]
                  await message.channel.send(tmpList)
           listFlag =  0

       elif endFlag == 1:
           for Boss in BossNum:
                  BookList = "Booking" + Boss
                  eval(BookList).clear()
           reply = "予約を全削除"
           await message.channel.send(reply)
           endFlag = 0

       elif bookFlag == 1:
           bossCount = 0
           for Boss in BossNum:
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  eval(BookList).append([message.author.display_name, str(message.author.mention)])
                  bossCount += 1
           if bossCount >= 1:
               reply = str(bossCount) + "件の予約 >" + message.author.display_name
               await message.channel.send(reply)
           bookFlag = 0

       elif displayFlag == 1: # Display all book list
           for Boss in BossNum:
               tmpList = []
               BookList = "Booking" + Boss
               tmpList = [x[0] for x in eval(BookList)]
               await message.channel.send(tmpList)
           displayFlag = 0

    elif message.content.startswith("fin"):
        for Boss in BossNum:
               if Boss in message.content:
                   BookList = "Booking" + Boss
                   eval(BookList).remove([message.author.display_name,str(message.author.mention)]) 
        reply = "削除完了 >" + message.author.display_name
        await message.channel.send(reply)

    elif message.content.startswith("ment"):
        for Boss in BossNum:
            tmpList = []
            if Boss in message.content:
                  BookList = "Booking" + Boss
                  tmpList = [x[1] for x in eval(BookList)]
                  await message.channel.send(tmpList)
    
    elif message.content.startswith("cmd"):
        await message.channel.send("予約:rsv 1-5 / 予約表示:rsv list 1-5 / 予約全表示:rsv! / 予約削除:fin 1-5 / 予約全削除:rsv END / 通知:ment 1-5")
         

client.run(TOKEN)