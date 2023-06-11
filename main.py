import json
import discord
import time
import random
import threading

fconfig = open('config.json', 'r')
config = json.load(fconfig)
fconfig.close();

intents = discord.Intents.default()
intents.message_content = True

threadStarted = False
client = discord.Client(intents=intents)

def play_pipe():
	source = discord.FFmpegOpusAudio('pipe.mp3')
	vClient.play(source)
	if vClient.is_connected():
		threading.Timer(random.randrange(30, 300), play_pipe).start()

@client.event
async def on_ready():
	print(f'Logged on as {client.user}')

@client.event
async def on_message(message):
	global threadStarted, vClient
	if message.content.startswith('|') and threadStarted is False:
		threadStarted = True
		vChannel = message.author.voice.channel
		vClient = await vChannel.connect()
		vClient.stop()
		threading.Timer(random.randrange(30, 300), play_pipe).start()

client.run(config['token'])