import discord 
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot=commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'tu bot {bot.user} esta en linea')
    
@bot.command()
async def contaminacion_f(ctx):
    q = "Contaminacion Fisica: objetos, envases plásticos, bolsas, y todo tipo de materiales producidos por el hombre que flotan en las aguas de ríos, lagos y otras fuentes de agua, así como tierra que ha sido arrastrada por la lluvia desde áreas deforestadas._Estos contaminantes pueden cambiar el color, el sabor, la temperatura y el olor del agua, afectando a organismos que viven en ella o perdiendo su calidad para consumo humano."
    await ctx.send(q)

@bot.command()
async def contaminacion_q(ctx):
    a= "Contaminacion Quimica: sustancias químicas que se encuentran en el agua, como metales pesados, pesticidas, productos químicos industriales y otros contaminantes que pueden ser tóxicos para los organismos acuáticos y para los seres humanos._Estos contaminantes pueden afectar la salud de los organismos acuáticos y de las personas que consumen agua contaminada."
    await ctx.send(a)

@bot.command()
async def contaminacion_b(ctx):
    b= "Contaminacion Biologica: organismos vivos, como bacterias, virus y parásitos, que pueden contaminar el agua._Estos contaminantes pueden causar enfermedades en los seres humanos y en los organismos acuáticos."
    await ctx.send(b)                                                                

@bot.command()
async def img_reflexiva(ctx):
    with open("imagenes/imgf1.jpg", "rb") as file:
        picture = discord.File(file)
        await ctx.send(file=picture)

@bot.command()
async def mem_contaminacion(ctx):
    p= random.randint(1,2)
    if p == 1:
        with open("imagenes/memc1.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    elif p == 2:
        with open("imagenes/memc2.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    else:
        await ctx.send("error")

token=""

bot.run(token)