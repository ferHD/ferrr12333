import discord
import youtube_dl
from discord.ext import commands

TOKEN = 'NDMyNTUzMzg1MjA4NzA5MTIx.DqNsHA.k-_fm8rYRJuvYm6HQOBJbULVInk'
client = commands.Bot(command_prefix = '*')

players = {}

@client.event
async def on_ready():
    print('Bot Online.')

    @client.command(pass_context=True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

    @client.coomands(pass_context=True)
    async def play(ctx, url):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

client.run(TOKEN)
