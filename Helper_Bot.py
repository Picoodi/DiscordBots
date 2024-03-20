#This is the code for my Helper-Bot. I use it as a bridge between the users and Mods on my Server. So the users can write report messages or help messages to the bot,
#who will help them directly or send theyr requests to mods or server owners.

import discord #diese Library muss vlt. erst im Terminal installiert werden.
from time import *
from datetime import *
from random import randint



class MyClient(discord.Client): #Klasse fuer den Bot
    
    #Bestaetigung des Einloggens des Bots
    async def on_ready(self):
        print("HB hat sich eingelogt.")



         
    async def on_message(self,message):
        
    #this is needed so the bot doesnt answer itself
        if message.author == client.user:
            return



    #Help Anfrage eines User. You can Modifie what the Bot says as u like it
        if message.content.startswith("help"):
            await message.channel.send("Hello Im the Helper Bot of the Bot Server. Im here to help u with whatever u need.")
            await message.channel.send("If u ever need help again just type a message to me starting with <help>")
            await message.channel.send("If u wanna report someone to the server Mods and Owner just write a message to me starting with <report> followed by which person u wanna report and why")
            await message.channel.send("If u wanna know more about the Server and its channels just write a message to me starting with <serverinfo>")



    #This command lets the user write a report message to the mods or server host 
        if message.content.startswith("report"):
            messagecontent = message.content
            await message.channel.send("ur message got send to the serverhost")
            
            channel = client.get_channel()#Channel id DM with Mods or Server Host in the brackets
            await channel.send("Someone wanted to report someone!")
            await channel.send(messagecontent)
            print()
            print( message.author)
            print("Wanted to report someone.  Full Message:")
            print(messagecontent)


      
    #Command will be uptdated in the furture or u can build it yourself
        if message.content.startswith("serverinfo"):
            await message.channel.send("Here you can write what the bot shall say")
        






#Down here insert ur Token from the Discord Developer Portal for your bot
client = MyClient()
client.run("TOKEN")   
