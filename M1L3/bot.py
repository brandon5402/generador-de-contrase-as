import discord
from botlog import gen_pass, gen_emodji, flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$contra'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$contra'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$flip'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$emoji'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)

client.run("MTI0NjQ3ODMxNTM0NzM4MjMxMg.GvT9W1.YonjZWG5Aap2Npa8Jl6EwUGfvPbdD6zXoE01x0")