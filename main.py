import disnake
import asyncio

from asyncio import sleep
from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

CENSORED_WORDS = ["Faking", 'negr', 'сволочь', "нафиг"]

# Во что играет бот
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(status=disnake.Status.online, activity=disnake.Game("закрыт в чулане"))
        await sleep(15)

# Выдается роль
@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, name='gtx')
    await member.add_roles(role)

# Запретки
@bot.event
async def on_message(message):
    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content == censored_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} ты там офигел что ли?")


# Команда текста
@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("я готов к работе!")

# Команда текста
@bot.slash_command()
async def about_the_channel(interaction: disnake.AppCmdInter):
    await interaction.send("Это Бот создан для показа моих умений в програмировании на библиотеки ")

# Токен
bot.run("///")
