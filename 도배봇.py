import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/')

a = 1

@client.event
async def on_message(message):
    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

@client.event
async def on_message(message):
    global a
    if message.content.startswith("!도배"):
        도배 = message.content[3:]
        while a > 0:
            await message.channel.send(도배)
            if a == 0:
                break

    if message.content == '도배멈춰':
        a = a - 1
        await message.channel.send("도배멈춰!")

@client.event
async def on_message_edit(before, after):
	await before.channel.send(before.content + "->" + after.content)
	return

@client.event
async def on_message_delete(message):
	await message.channel.send("메세지 삭제 감지(" + str(message.author) + "): " + message.content)
	return


client.run('ODYxMTcxNDQ0MjY3MzUyMDc0.YOF6aA.hfsh50j4yT7NKMdZ810JT--BA98')
