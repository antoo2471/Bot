import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}\n")

for filename in os.listdir("./plugins"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"plugins.{filename[:-3]}")
            print(f"🔹 Plugin chargé : {filename}")
        except Exception as e:
            print(f"❌ Erreur lors du chargement de {filename} : {e}")

bot.run(TOKEN)
