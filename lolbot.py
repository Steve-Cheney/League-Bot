from datetime import datetime
import discord
import os
from discord import Embed
from discord import Client
import asyncio


client = discord.Client()  # creates instance of the client

@client.event
async def on_ready(): # when the client is ready
  print('We have logged in as {0.user}.'.format(client)) # print the user name that it is logged in as

# define global vars
party_list = set()
global_message_id = 0
global_channel_id = 0
init_user_id = 0
timeouttime = 15 # set message time out time
users = []

@client.event
async def on_message(message):
  if message.author == client.user: # ignore msgs from bot
    return

  if message.content.startswith('/league'):
    #await message.channel.send('Hello!')
    init_user_id = message.author.id
    users = [message.author]
    players = ""
    print("-------------vvv   New Call  vvv-------------")
    #userlist = list(users)
    #user0 = ""
    #for each in userlist:
    #  user0.append(str(each.display_name) + "\n")
    await message.channel.send("<@&625536281803227136>")
    embed = Embed(description = "👍=You're in, ♻️=Refresh, ❌=Cancel", color=0xDBA21E, timestamp = datetime.utcnow())

    fields = [("#", "1\n2\n3\n4\n5", True),
              ("Name", users[0].display_name, True),
              ]

    for name, value, inline in fields:
      embed.add_field(name=name, value = value, inline = inline)
      embed.set_author(name = "Who wants to play league?", icon_url="https://preview.redd.it/itq8rpld8va51.png?width=256&format=png&auto=webp&s=9701ba6228c29bf2d7e3dfffd45b9a3562507289")
      embed.set_footer(text="Bot called at")

    embedMsg = await message.channel.send(embed=embed)
    global_message_id = embedMsg.id
    global_channel_id = embedMsg.channel.id
    print(global_message_id)
    print(global_channel_id)
    await embedMsg.add_reaction("👍")
    await embedMsg.add_reaction("♻️")
    await embedMsg.add_reaction("❌")
    messageSent = global_message_id
    channel = global_channel_id

    def check1(reaction, user):
      if user.id != 846183956306853919:
        return str(reaction.emoji) == '👍'
    timeout1 = False
    count = 0


    while(count <5 and timeout1 == False):
      try:
        reaction, user = await client.wait_for('reaction_add',check=None, timeout=timeouttime)
      except asyncio.TimeoutError:
        await message.channel.send('Last search timedout')
        timeout1 = True
      else:
        if user.id!=846183956306853919 and str(reaction.emoji) == '❌':
          await message.channel.send('*Latest League search has been cancelled*')
          timeout1 = True
          print("Cancelled")
        if str(reaction.emoji) == '♻️':
          users = [message.author]
          await embedMsg.edit(embed=embed)
          print("You hit the X button")
        if str(reaction.emoji) == '👍':
          #await message.channel.send(user.display_name)
          if user not in users and user.id != 846183956306853919:
            users.append(user)
            count += 1
          for user in users:
            print(user, " + ")

          embednew = Embed(description = "👍=You're in, ♻️=Refresh, ❌=Cancel", color=0xDBA21E, timestamp = datetime.utcnow())
          players = ""
          for each in users:
            players += each.display_name + "\n"
          fields2 = [("#", "1\n2\n3\n4\n5", True),
                    ("Name", players, True),
                    ]

          for name, value, inline in fields2:
            embednew.add_field(name=name, value = value, inline = inline)
            embednew.set_author(name = "Who wants to play league?", icon_url="https://preview.redd.it/itq8rpld8va51.png?width=256&format=png&auto=webp&s=9701ba6228c29bf2d7e3dfffd45b9a3562507289")
            embednew.set_footer(text="Bot called at")
          await embedMsg.edit(embed=embednew)





client.run(os.getenv('TOKEN')) #log into
