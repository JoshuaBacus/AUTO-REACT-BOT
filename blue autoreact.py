import discord
from discord.ext    import commands
from discord.ext.commands   import Bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Autoreact ready...')

@bot.event
async def on_message(message):
    if message.channel.id == 701697687514382351: # Hier Server ID einfügen
        await message.add_reaction("🏆") # Hier Emoji einsetzen

bot.run("NzE0ODMxMjk3NjAzOTYwODMy.Xs0b_g.UxFFu0CfVrKL0sQFGs59yTlx4x8") # Hier Token einfügen

#                               BLUE Discord: https://discord.gg/germany
#
#                               BLUE YouTube: https://www.youtube.com/bluek1ng
#
# To-Do
# 1. Channel ID einfügen (Zeile 13)
# 2. Emoji einfügen (zeile 14)
# 3. Bot Token einfügen (Zeile 16)
# 4. Bot starten und Spaß haben
# 5. BLUE Server lieben und boosten! xD
#
#
#                               Python benutzen und Bot erstellen? Einleitung dazu findest du hier: https://youtu.be/RYbHpqHCjrY