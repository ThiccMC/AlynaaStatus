# Import stuff heh
import discord
import keep_alive
from mcstatus import MinecraftServer
from decouple import config

# keep_alive to receive ping.
keep_alive.keep_alive()

# Start server, with commands and stuff.
server = MinecraftServer.lookup(config('ADDRESS'))
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.t status'):
        try:
            status=server.status()
            await message.channel.send('Yay, **Thicc SMP** is **online**!')
        except:
            await message.channel.send('Oops, **Thicc SMP** **is currently offline**!')

    if message.content.startswith('.t stasus'):
        try:
            status=server.status()
            await message.channel.send('Sussy baka, **Thicc SMP** is **online**!')
        except:
            await message.channel.send('Oops so sus, **Thicc SMP** **is currently offline**!')

    if message.content.startswith('.t statú'):
        try:
            status=server.status()
            await message.channel.send('Unikey user huh? Nevermind, **Thicc SMP** is **online**!')
        except:
            await message.channel.send('Unikey user huh? Nevermind, wait... **Thicc SMP** **is currently offline**!')

    if message.content.startswith('.t ping'):
        try:
            ping=server.status()
            await message.channel.send("Pinging from Replit... **Thicc SMP** replied in **{0}** ms".format(ping.latency))
        except:
            await message.channel.send('Oops, **Thicc SMP** is currently **offline**!')

    if message.content.startswith('.t players'):
        try:
            player = server.status()
            await message.channel.send("**Thicc SMP** has **{0}** players online".format(player.players.online))
        except:
            await message.channel.send('Oops, **Thicc SMP** is currently **offline**!')
  
    if message.content.startswith('.t playẻ'):
        try:
            player = server.status()
            await message.channel.send("Unikey user huh? Nevermind, **Thicc SMP** has **{0}** players online".format(player.players.online))
        except:
            await message.channel.send('Unikey user huh? Nevermind, wait... **Thicc SMP** is currently **offline**!')

    if message.content.startswith('.t player-names'):
        try:
            name = server.query()
            await message.channel.send("**Thicc SMP** has the following players online: **{0}**".format(", ".join(name.players.names)))
        except:
            await message.channel.send('Oops, **Thicc SMP** is currently **offline**!')

client.run(config('TOKEN'))
