#cording:utf-8
import discord
from zaifapi import ZaifPublicApi

zaif = ZaifPublicApi()

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
	if message.content.startswith('yo'):
		await client.send_message(message.channel, 'yo! '+message.author.name )
	if message.content.startswith('bitcoin'):
		btc_jpy = int(zaif.last_price('btc_jpy')["last_price"])
		await client.send_message(message.channel,'Bitcoin Price : '+str(btc_jpy)+ 'yen')
	if message.content.startswith('monacoin'):
		mona_jpy = int(zaif.last_price('mona_jpy')["last_price"])
		await client.send_message(message.channel,'Monacoin Price : '+str(mona_jpy)+' yen')
	if message.content.startswith('help'):
		a = ('```help     ->    show help```')
		b = ('```ocha     ->    you get a tea```')
		c = ('```yo       ->    genmaichan will says yo!```')
		d = ('```bitcoin  ->    show bitcoin price```')
		e = ('```monacoin ->    show monacoin price```')
		await client.send_message(message.channel, a+b+c+d+e)

client.run(BOT_TOKEN)
