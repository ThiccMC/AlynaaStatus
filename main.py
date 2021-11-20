# Import stuff heh
## discord.py
import discord
## keep_alive.py
import keep_alive
## some other stuff
from mcstatus import MinecraftServer
from decouple import config
from MaxEmbeds import EmbedBuilder

# keep_alive to receive ping.
keep_alive.keep_alive()

# Start server, with commands and stuff.
server = MinecraftServer.lookup(config('ADDRESS'))
skyblock = MinecraftServer.lookup(config('SKYBLOCKADDRESS'))
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Made with <3 by QuanTrieuPCYT')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.t status'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Oh hey, Thicc SMP is online :D",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "thiccsmp.qtpc.tech", True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Unfortunately, Thicc SMP went offline :(",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)

    if message.content.startswith('.t stasus'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Sussy baka, Thicc SMP is online :D",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "thiccsmp.qtpc.tech", True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Man, so sus, and Thicc SMP went offline :(",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops so sus, **Thicc SMP** **is currently offline**!')

    if message.content.startswith('.t statú'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Telex user huh? Nevermind, Thicc SMP is online :D",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "thiccsmp.qtpc.tech", True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Telex user huh? Welp, Thicc SMP is offline :(",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)

    if message.content.startswith('.t stasú'):
        try:
            status = server.status()
            embed = EmbedBuilder(
                title="Sussy baka, Thicc SMP is online :D",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["IP (Java + Bedrock)", "thiccsmp.qtpc.tech", True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Man, so sus, and Thicc SMP is offline :(",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)

            #await message.channel.send('Unikey user huh? Nevermind, wait... **Thicc SMP** **is currently offline**!')

    ## remave ping cuz if i hosted it on the same machine. ping = 0.xx ms => useless
    if message.content.startswith('.t players'):
        try:
            player = server.status()
            playerskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Thicc SMP Playercount",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["SMP", "{0}/50".format(player.players.online), True], ["SkyBlock", "{0}/50".format(playerskyblock.players.online), True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Thicc SMP is offline :(",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Thicc SMP** is currently **offline**!')

    if message.content.startswith('.t playẻ'):
        try:
            player = server.status()
            playerskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Telex user? Anyways here is the Thicc SMP Playercount",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["SMP", "{0}/50".format(player.players.online), True], ["SkyBlock", "{0}/50".format(playerskyblock.players.online), True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Telex user? Nevermind, Thicc SMP is offline :(",
                description="Powered by AlynaaStatus",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Thicc SMP** is currently **offline**!')

    ## remave ping cuz if i hosted it on the same machine. ping = 0.xx ms => useless (from typical)
    # ping is still here as i also want to get the ping from my webserver when the mainserver is off (in the near future)

    if message.content.startswith('.t ping'):
        try:
            latency = server.ping()
            latencyskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Thicc SMP Latency from Replit",
                description="Powered by AlynaaStatus, hosted on Replit",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["SMP Latency (ms)", "{0} from Replit.".format(latency), True], ["SkyBlock Latency (ms)", "{0} from Replit.".format(latencyskyblock), True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Thicc SMP is offline and I can't check the latency :(",
                description="Powered by AlynaaStatus, hosted on Replit",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Thicc SMP** is currently **offline**!')

    if message.content.startswith('.t latency'):
        try:
            latency = server.ping()
            latencyskyblock = skyblock.status()
            embed = EmbedBuilder(
                title="Thicc SMP Latency from Replit",
                description="Powered by AlynaaStatus, hosted on Replit",
                color=discord.Color.from_rgb(0, 255, 255),
                fields=[["SMP Latency (ms)", "{0} from Replit.".format(latency), True], ["SkyBlock Latency (ms)", "{0} from Replit.".format(latencyskyblock), True]],
                thumbnail='https://cdn.discordapp.com/emojis/878887184915136542.gif'
            ).build()
            await message.channel.send(embed=embed)
        except:
            # no need for player status variables as it went offline already.
            embed = EmbedBuilder(
                title="Thicc SMP is offline and I can't check the latency :(",
                description="Powered by AlynaaStatus, hosted on Replit",
                color=discord.Color.from_rgb(244, 41, 65),
                fields=[["Try checking us out later!", ":AlynaCri:", True]],
                thumbnail='https://cdn.discordapp.com/emojis/880069948821622844.png'
            ).build()
            await message.channel.send(embed=embed)
            #await message.channel.send('Oops, **Thicc SMP** is currently **offline**!')

client.run(config('TOKEN'))
