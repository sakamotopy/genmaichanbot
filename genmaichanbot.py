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

jsopen1 = open("/home/ubuntu/genmaichanbot/token.json")
jsload1 = json.load(jsopen1)
jsstr1 = json.dumps(jsload1)
token = jsstr1['bot']['token']
print(token)
BOT_TOKEN = ""+token+""

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
		num = random.randint(1,6)
		num2 = random.randint(1,6)
		num3 = random.randint(1,6)
		num4 = random.randint(1,6)
		num5 = random.randint(1,6)
		num6 = random.randint(1,6)		
		oyako = ["親","子"]
		oyaorko = random.choice(oyako)
		oyakoresult = "あなたは「" +oyaorko+ "」です。"

		def chin_result():
			if num == num2 and num == num3 and num != 1:
				return ("ゾロ目！バトル！\n攻撃力"+str(num)+"！")
			elif num == 1 and num2 == 1 and num3 == 1:
				return ("ピンゾロ！無条件勝利！")
			elif num in range(4,6) and num2 == range(4,6) and num3 == range(4,6) and num != num2 and num2 != num3 and num3 != num:
				return("シゴロ！無条件勝利！")
#			elif num == num2 or num2 == num3 or num3 == num:
#				return("")
			elif num in range(1,3) and num2 in range(1,3) and num3 in range(1,3) and num != num2 and num2 != num3 and num2 != num3:
				return("ヒフミ…")
			elif num != num2 and num2 != num3 and num3 != num:
				return("役無し！")
			else:
				return("バトル！")
		
		def chin_result2():
			if num4 == num5 and num4 == num6 and num4 != 1:
				return ("ゾロ目！攻撃力"+ str(num4) +"！")
			elif num4 == 1 and num5 == 1 and num6 == 1:
				return ("ピンゾロ！ちょーつえー！")
			elif num4 in range(4,6) and num5 == range(4,6) and num6 == range(4,6) and num4 != num5 and num5 != num6 and num6 != num4:
				return("シゴロ！")
#			elif num4 == num5 or num5 == num6 or num6 == num4:
#				return("point x1\n>>battle!")
			elif num4 in range(1,3) and num5 in range(1,3) and num6 in range(1,3) and num4 != num5 and num5 != num6 and num5 != num6:
				return("ヒフミ…負け！")
			elif num4 != num5 and num5 != num6 and num6 != num4:
				return("役無し！負け！")
			else:
				return("バトル！")


#		if oyako_choice == "oya":
#			chin_result()
#		elif oyako_choice == "ko":
#			chin_result2()
#		else:
#			pass

		cr = chin_result()
		cr2 = chin_result2()
		chin = str(num)
		chin2 = str(num2)
		chin3 = str(num3)
		chin4 = str(num4)
		chin5 = str(num5)
		chin6 = str(num6)
		chinchiro_1 = '['+chin+']['+chin2+']['+chin3+']\n' + str(cr)
		chinchiro_2 = '['+chin4+']['+chin5+']['+chin6+']\n' + str(cr2)
		await client.send_message(message.channel,oyakoresult + '\n`親 → ' + chinchiro_1+'`' + '\n\n`子 → ' + chinchiro_2+'`')

	if message.content.startswith('omikuji'):
		omikuji = ["おめでとう！！\n超大吉だよ！天才！すごい！！","吉。普通だね！","あっ、、大凶！\nお祓いしときますね…","f**k you"]
		omikuji_r = "{0.author.mention} ".format(message) +"\n"+  random.choice(omikuji)
		await client.send_message(message.channel,omikuji_r)
#	if message.content.startswith('def'):
#		def gorira():
#			go = random.randint(1,100)
#		gorira_ran = gorira()
#		await client.send_message(message.channel,str(gorira_ran))
	if message.content.startswith('にゃんにゃん'):
		await client.send_message(message.channel, 'https://youtu.be/MOSYstIWZug')
	if message.content.startswith('はあと様'):
		await client.send_message(message.channel, 'かわいい！\n'+'https://www.youtube.com/channel/UC1CfXB_kRs3C-zaeTG3oGyg')

	if message.content.startswith('help'):
		a = ('```help      ->    show help```')
		b = ('```ocha      ->    you get a tea```')
		c = ('```yo        ->    genmaichan will says yo!```')
		d = ('```bitcoin   ->    show bitcoin price(currency pair:monacoin,ethereum,nem,pepecash)```')
#		e = ('```priceall  ->    show cryptcurrency price```')
		f = ('```にゃんにゃん->   うおおおおおおおおおお ```')
		g = ('```weather   ->    show weather```')
		h = ('```wiki **   ->    search that word in Wikipedia```')
		i = ('```dice      ->	play dice```')
		j = ('```omikuji   ->	let show your fortune```')

		await client.send_message(message.channel, a+b+c+d+g+h+i+j+f)

client.run(BOT_TOKEN)
