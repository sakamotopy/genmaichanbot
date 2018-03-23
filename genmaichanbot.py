



#cording:utf-8
import discord
client = discord.Client()

BOT_TOKEN = "NDI2NDIxNDMzOTM0MDIwNjA4.DZVv8w.vIEuXbezmvRlu5zXmo9WoMhZAAk"

@client.event
async def on_ready():
	print('Logged in as')
	print('BOT-NAME :', client.user.name)
	print('BOT-ID	:', client.user.id)
	print('-------')

@client.event
async def on_message(message):
	if client.user == message.author:
		return
	if message.content.startswith('ocha'):
		await client.send_message(message.channel, '(@.@)oU')

	if message.content.startswith('thank'):
		await client.send_message(message.channel, 'sure :)')


client.run(BOT_TOKEN)
# genmaichanbot
# genmaichanbot
