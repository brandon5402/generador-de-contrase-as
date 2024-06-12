import discord
from discord.ext import commands
from botlog import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def contra(ctx):
    await ctx.send(gen_pass(10))

bot.run("MTI0NjQ3ODMxNTM0NzM4MjMxMg.GvT9W1.YonjZWG5Aap2Npa8Jl6EwUGfvPbdD6zXoE01x0")