#<copyright>
#  Copyright (c) 2019 Skeyll All Rights Reserved.
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
    removeFlag = 0
    bookFlag = 0
    endFlag = 0
    displayFlag = 0
    # mentionFlag = 0

    if message.content.startswith("rsv"):
       if "list" in message.content: # Call a list
           listFlag = 1
       elif "fin" in message.content: # Remove from book
           removeFlag = 1
       elif "END" in message.content: # Initialize all lists
           endFlag = 1
       elif "!" in message.content: # Call all arrays
           displayFlag = 1
    #   elif "NOT" in message.content:
    #       mentionFlag = 1
       else: # Book
           bookFlag = 1

       if listFlag == 1:
           for Boss in BossNum:
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  await message.channel.send(eval(BookList))
       elif removeFlag == 1:
           for Boss in BossNum:
               if Boss in message.content:
                   BookList = "Booking" + Boss
                   eval(BookList).remove(message.author.display_name)      
           reply = "Did it! >" + message.author.display_name
           await message.channel.send(reply)
       elif endFlag == 1:
           for Boss in BossNum:
                  BookList = "Booking" + Boss
                  eval(BookList).clear()
           reply = "I clear all lists!"
           await message.channel.send(reply)
       elif bookFlag == 1:
           for Boss in BossNum:
               if Boss in message.content:
                  BookList = "Booking" + Boss
                  eval(BookList).append(message.author.display_name)
                  reply = "Book on " + str(Boss) + "! >" + message.author.display_name
                  await message.channel.send(reply)
 #      elif mentionFlag == 1:
 #           mentionList = []
 #           for Boss in BossNum:
 #               if Boss in message.content:
 #                 BookList = "Booking" + Boss
 #                 break
 #           for one in eval(BookList):
 #               mentionList.append(" @" + one + " ")
 #           await message.channel.send(mentionList)
       elif displayFlag == 1: # Display all book list
           for Boss in BossNum:
               BookList = "Booking" + Boss
               await message.channel.send(eval(BookList))

       listFlag =  0
       removeFlag = 0
       bookFlag = 0
       endFlag = 0
       displayFlag = 0
 #      mentionFlag = 0

client.run(TOKEN)