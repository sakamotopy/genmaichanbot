#cording:utf-8
import discord
from zaifapi import ZaifPublicApi
import json
import requests
import wikipedia
import random
import csv
import datetime
import urllib
import urllib3.request
from bs4 import BeautifulSoup
import lxml
import sys
import codecs
import time

zaif = ZaifPublicApi()

client = discord.Client()

BOT_TOKEN = "NDI2NDIxNDMzOTM0MDIwNjA4.Dkjrhg._WLb2_TxFw-__HqKRSwpJ8-RmOY"

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
#		douzo = '(@.@)oU {0.author.mention}'.format(message)
		await client.send_message(message.channel, '(@.@)oU')
	if message.content.startswith('thank'):
		await client.send_message(message.channel, 'sure :)')
	if message.content.startswith('yo'):
		msg = 'yo! {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg )
	if message.content.startswith('bitcoin'):
		btc_jpy = int(zaif.last_price('btc_jpy')["last_price"])
		await client.send_message(message.channel,'Bitcoin Price  : '+str(btc_jpy)+ ' yen')
	if message.content.startswith('monacoin'):
		mona_jpy = int(zaif.last_price('mona_jpy')["last_price"])
		await client.send_message(message.channel,'Monacoin Price : '+str(mona_jpy)+' yen')
	if message.content.startswith('pepecash'):
		pepecash_jpy = float(zaif.last_price('pepecash_jpy')["last_price"])
		await client.send_message(message.channel,'Pepecash Price : '+str(pepecash_jpy)+' yen')
	if message.content.startswith('ethereum'):
		eth_jpy = int(zaif.last_price('eth_jpy')["last_price"])
		await client.send_message(message.channel,'Ethereum Price : '+str(eth_jpy)+ ' yen')
	if message.content.startswith('nem'):
		xem_jpy = float(zaif.last_price('xem_jpy')["last_price"])
		await client.send_message(message.channel,'Nem(xem) Price : '+str(xem_jpy)+' yen')
	if message.content.startswith('weather'):
		json_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
		payload = {'city':'130010'}
		response = requests.get(json_url, params=payload)
		json = response.json()
		weather = json['description']['text']
		await client.send_message(message.channel,weather )

#	if message.content.startswith('priceall'):
#		price_all = btc_jpy +"/n"+ eth_jpy +"/n"+ xem_jpy +"/n"+ mona_jpy +"/n"+ pepecash_jpy
#		await client.send_message(message.channel,price_all)

	if message.content.startswith('json '):
		wikipedia.set_lang('ja')
		wikiinput = message.content[5:]
		wikipage = wikipedia.page(wikiinput)
		html_wikiurl = wikipage.url

		html = urllib.request.urlopen(html_wikiurl)
		soup = BeautifulSoup(html,"html.parser")

		title_tag = soup.title
		title = title_tag.string

#		print()
		m = html_wikiurl +'\n'+ title +'\n'
		await client.send_message(message.channel,m )

	if message.content.startswith('wiki '):
		wikipedia.set_lang('ja')
		search_text = message.content[5:]
		search_response = wikipedia.search(search_text)
		search_page = wikipedia.page(search_response[0])
		wi = search_page.content[0:100]
		wiwi = search_page.url
		mwiki = 'https://ja.m.wikipedia.org/wiki/'+message.content[5:]
		await client.send_message(message.channel,wi+'....\n'+ mwiki )
	if message.content.startswith('test '):
		wikiurl = 'https://ja.m.wikipedia.org/wiki/'+message.content[5:]
		await client.send_message(message.channel,wikiurl)


	if message.content.startswith('dango'):
		await client.send_message(message.channel, ':dango:' )
	if message.content.startswith('dice'):
		num = random.randint(1,6)
		dice1 = ":game_die: --> "
		await client.send_message(message.channel,dice1+str(num) )
	if message.content.startswith('chinchiro'):
#		def chin_result():
		num = random.randint(1,6)
		num2 = random.randint(1,6)
		num3 = random.randint(1,6)
#			oyako = ["oya","ko"]
#			orako_choice = ramdom.choice(oyako)
		def chin_result():
			if num == num2 and num == num3 and num != 1:
				return ("point x3\n")
			elif num == 1 and num2 == 1 and num3 == 1:
				return ("point x5\n>>you win!!")
			elif num in range(4,6) and num2 == range(4,6) and num3 == range(4,6) and num != num2 and num2 != num3 and num3 != num:
				return("point x2\n>>you win!")
			elif num == num2 or num2 == num3 or num3 == num:
				return("point x1\n>>battle!")
			elif num in range(1,3) and num2 in range(1,3) and num3 in range(1,3) and num != num2 and num2 != num3 and num2 != num3:
				return("point x-1\n>>you lose...")
			elif num != num2 and num2 != num3 and num3 != num:
				return("point x-1\n>>you lose.")
			else:
				return("point x -1\n>>battle!")
#		if oyako_choice == "oya":
#			chin_result()
#		elif oyako_choice == "ko":
#			chin_result()
#		else:
#			pass
		cr = chin_result()
		chin = str(num)
		chin2 = str(num2)
		chin3 = str(num3)
		await client.send_message(message.channel,'['+chin+']['+chin2+']['+chin3+']\n' + str(cr))

	if message.content.startswith('omikuji'):
		omikuji = ["very good luck :)","good luck :>","bad luck :(","f**k you"]
		omikuji_r = "{0.author.mention} ".format(message) +"\n"+  random.choice(omikuji)
		await client.send_message(message.channel,omikuji_r)
#	if message.content.startswith('def'):
#		def gorira():
#			go = random.randint(1,100)
#		gorira_ran = gorira()
#		await client.send_message(message.channel,str(gorira_ran))
	if message.content.startswith('help'):
		a = ('```help      ->    show help```')
		b = ('```ocha      ->    you get a tea```')
		c = ('```yo        ->    genmaichan will says yo!```')
		d = ('```bitcoin   ->    show bitcoin price(currency pair:monacoin,ethereum,nem,pepecash)```')
#		e = ('```priceall  ->    show cryptcurrency price```')
#		f = ('``` ```')
		g = ('```weather   ->    show weather```')
		h = ('```wiki **   ->    search that word in Wikipedia```')
		i = ('```dice      ->	play dice```')
		j = ('```omikuji   ->	let show your fortune```')

		await client.send_message(message.channel, a+b+c+d+g+h+i+j)

client.run(BOT_TOKEN)
