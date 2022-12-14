#!/usr/bin/env python

import asyncio
from aioimaplib import aioimaplib
import requests


#Mailüberprüfung wird unendlich ausgeführt bis der Process von Cronjobs geschlossen wird
async def check_mailbox(host, user, password):
	while True:
		#Login zum Exchange Server
		imap_client = aioimaplib.IMAP4_SSL(host=host)
		await imap_client.wait_hello_from_server()

		await imap_client.login(user, password)
		await imap_client.select()
		#Mailbox durchsuchen nach dem 'unSeen' Attribut
		search, lines = await imap_client.search('unSeen', charset='US-ASCII')
		mailcount = (len(lines[0]))

		#Wenn ein Mail nicht gelesen wurde schick ein http request an den smartsocket
		if mailcount> 0:
			requests.get('http://10.18.20.158/control?cmd=GPIO,12,1')
		else:
			requests.get('http://10.18.20.158/control?cmd=GPIO,12,0')
		await imap_client.logout()


while True:
	if __name__ == '__main__':
		loop = asyncio.get_event_loop()
		loop.run_until_complete(check_mailbox('SI-EX-02', 'task.planer', 'pjjz3*Ab'))
	
