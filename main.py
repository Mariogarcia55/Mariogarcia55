import discord 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot=commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'tu bot {bot.user} esta en linea')
    
@bot.command()
async def cold(ctx):

    await ctx.send("\U0001F4D4")

@bot.command()
async  def repetir(ctx, *, mensaje: str):
    await ctx.send(mensaje)

@bot.command()
async def saludo(ctx,*, mensaje: str):
    
    mensaje = mensaje.lower().strip()

    if "hola" in mensaje:
        await ctx.send("Hola! ¿Cómo estás?")
    
    elif "Que onda" in mensaje:
        await ctx.send("¡Hola , que tral!")
    else:
        await ctx.send("No entendi tu saludo, pero hola!")

@bot.command()
async def messi(ctx):
    await ctx.send("Es el mejor jugador de la historia")

@bot.command()
async def despedida(ctx,*, m: str):
    
    m = m.lower().strip()

    if "adios" in m:
        await ctx.send("Que te vaya bien!")
    
    elif "chao" in m:
        await ctx.send("adiosssss")
    else:
        await ctx.send("No entendi tu mensaje, pero adios!")

@bot.command()
async def suma(ctx, a: int, b: int):
    resultado = a + b
    await ctx.send(f"El resultado de la suma es: {resultado}")

@bot.command()
async def divicion(ctx, a: int, b: int):
    if b != 0:
        res = a / b
        await ctx.send(f"El resultado de la division es: {res}")
        
    else:
        await ctx.send("No se puede dividir entre cero.")

token=""

bot.run(token)
