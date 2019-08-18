import discord

TOKEN = 'TOKENID'

client = discord.Client()

# int
CHANNEL_ID = 611804709115658265

from collections import OrderedDict
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

    if message.content.startswith("rsv"):
       if "list" in message.content: #Display list
           listFlag = 1
       elif "fin" in message.content: # Remove a book
           removeFlag = 1
       elif "END" in message.content: # Initialize Book Lists
           endFlag = 1
       elif "!" in message.content:
           displayFlag = 1
       else: # Book to a list
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
                   eval(BookList).remove(message.author.name)      
           reply = "Did it! >" + message.author.name
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
                  eval(BookList).append(message.author.name)
                  reply = "Book on " + str(Boss) + "! >" + message.author.name
                  await message.channel.send(reply)
       elif displayFlag == 1: # Display all book list
           for Boss in BossNum:
               BookList = "Booking" + Boss
               await message.channel.send(eval(BookList))

       listFlag =  0
       removeFlag = 0
       bookFlag = 0
       endFlag = 0
       ddisplayFlag = 0

client.run(TOKEN)