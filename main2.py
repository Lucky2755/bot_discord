import discord, random, time, os, requests
from discord.ext import commands
from bot_logic import gen_pass
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(1286715618183348380)
    if channel:
        await channel.send("buonsalve, sono boh 2.0") 
    print(f"accesso effettuato con successo a {bot.user}")
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] ACCESSO ESEGUITO CON SUCCESSO A '{bot.user}'"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n\n\n{log};")
    




@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RICEVUTO COMANDO '/ciao'"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    time.sleep(0.5)
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RISPOSTA EFFETTUATA CON SUCCESSO"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")


@bot.command()
async def heh(ctx, count_heh = 20):
    await ctx.send("he" * count_heh)
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RICEVUTO COMANDO '/he'"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    time.sleep(0.5)
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RISPOSTA EFFETTUATA CON SUCCESSO"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")


@bot.command()
async def stop(ctx):
    await ctx.send("alla prossima!")
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RICEVUTO COMENDO '/stop'"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    
    time.sleep(0.5)
    
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RISPOSTA EFFETTUATA CON SUCCESSO"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    
    time.sleep(0.5)
    
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] SPEGNIMENTO IN CORSO..."
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")

    time.sleep(0.5)
    
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] SPEGNIMENTO EFFETTUATO CON SUCCESSO"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")

    exit()

@bot.command()
async def moneta(ctx):
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RICEVUTO COMANDO '/moneta'"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    await ctx.send("lancio della moneta in corso....")
    time.sleep(0.5)
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RISPOSTA EFFETTUATA CON SUCCESSO"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    time.sleep(1)
    l = "TESTA!", "CROCIE!"
    x = random.choice(l)
    await ctx.send(x)
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] {x}"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    

@bot.command()
async def comandi(ctx):
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RICEVUTO COMANDO '/comandi'"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    time.sleep(0.5)
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] SCRITTURA COMANDI IN CORSO..."
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    await ctx.send("posso eseguire i seguenti comandi:")
    time.sleep(1)
    await ctx.send("/ciao")
    time.sleep(1)
    await ctx.send("/heh")
    time.sleep(1)
    await ctx.send("/stop")
    time.sleep(1)
    await ctx.send("/moneta")
    time.sleep(1)
    await ctx.send("/gen")
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] SCRITTURA COMANDI COMPLETATA"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")

@bot.command()
async def gen(ctx):
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RICEVUTO COMANDO '/gen'"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    lunghezza_password = random.randint(10, 20)
    x = gen_pass(lunghezza_password) 
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] GENERAZIONE PASSWORD IN CORSO..."
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")
    await ctx.send(f"La tua nuova password è: {x}")
    data_corrente=datetime.now()
    log = f"[{data_corrente.strftime('%Y-%m-%d %H:%M:%S')}] RISPOSTA EFFETTUATA CON SUCCESSO"
    with open("/Users/davidebaroncelli/Documents/corso python/bot discord/logs.txt", "a") as logs:
        logs.write(f"\n{log};")


@bot.command()
async def meme(ctx):
    immagini = os.listdir("/Users/davidebaroncelli/Documents/corso python/bot discord/meme")
    m=random.choice(immagini)
    with open(f"/Users/davidebaroncelli/Documents/corso python/bot discord/meme/{m}", "rb") as meme1:
        img = discord.File(meme1)
    await ctx.send(file=img)



@bot.command('duck')
async def duck(ctx):
    def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def cani(ctx):
    immagini = os.listdir("/Users/davidebaroncelli/Documents/corso python/bot discord/cani")
    m=random.choice(immagini)
    with open(f"/Users/davidebaroncelli/Documents/corso python/bot discord/cani/{m}", "rb") as cane:
        img = discord.File(cane)
    await ctx.send(file=img)




        

bot.run("")