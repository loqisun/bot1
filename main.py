import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! I am {bot.user}!')


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

#Для чтения файлов используется встроенная в питоне функция open. Она позволяет открывать файлы в нескольких режимах: ‘w’ - записывает в файл, но перед этим удаляет все, что было в файле;
#‘r’ - открывает файл только для чтения;
#‘a’ - записывает в конец файла, но не удаляет ничего из него;
#‘rb’ - открывает нетекстовый файл для чтения;
#'wb’ - открывает нетекстовый файл для записи.

@bot.command()
async def mem(ctx):
    with open('mem2.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)


@bot.command()
async def help_(ctx):
    await ctx.send('Functions i have:\n'
                   '$hello - bot is greeting you\n'
                   '$add - adds up yo numbers\n'
                   '$heh - write how many times the bot needs to repeat "heh"\n'
    )
                   
bot.run("TOKEN")