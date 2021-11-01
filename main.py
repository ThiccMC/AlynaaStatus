# Import stuff heh
import discord
from mcstatus import MinecraftServer
from MaxEmbeds import EmbedBuilder

# Start server, with commands and stuff.
server = MinecraftServer.lookup('simpmc.net')
serverpe = MinecraftServer.lookup('simpmc.net:25568')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!!status'):
        try:
            status=server.status()
            await message.channel.send('Yay, **SimpMC** is **online**!')
        except:
            await message.channel.send('Oops, **SimpMC** **is currently offline**!')

    if message.content.startswith('!!stasus'):
        try:
            status=server.status()
            await message.channel.send('Sussy baka, **SimpMC** is **online**!')
        except:
            await message.channel.send('Oops so sus, **SimpMC** **is currently offline**!')

    if message.content.startswith('!!statú'):
        try:
            status=server.status()
            await message.channel.send('Unikey user huh? Nevermind, **SimpMC** is **online**!')
        except:
            await message.channel.send('Unikey user huh? Nevermind, wait... **SimpMC** **is currently offline**!')

## remave ping cuz if i hosted it on the same machine. ping = 0.xx ms => useless
    if message.content.startswith('!!players'):
        try:
            player = server.status()
            playerpe = serverpe.status()
            embed = EmbedBuilder (
              title = "SimpMC Networks Player Counts",
              color = discord.Color.dark_gold(),
              fields = [["PE Players", "{0}".format(playerpe.players.online), True], ["PC Players", "{0}".format(player.players.online), True]],
              thumbnail = 'https://media.discordapp.net/attachments/788051866495090732/899160844447940668/wiggle-waving.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            await message.channel.send('Oops, **SimpMC** is currently **offline**!')
  

## errr, useless cuz bungee doesnt show it iirc

client.run('')
