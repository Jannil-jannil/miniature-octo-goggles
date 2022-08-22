#!/usr/bin/env python

import asyncio
from aioimaplib import aioimaplib
import requests



async def check_mailbox(host, user, password):
	while True:
		imap_client = aioimaplib.IMAP4_SSL(host=host)
		await imap_client.wait_hello_from_server()

		await imap_client.login(user, password)
		await imap_client.select()
		search, lines = await imap_client.search('unSeen', charset='US-ASCII')
		mailcount = (len(lines[0]))
		if mailcount> 0:
			requests.get('http://10.18.20.158/control?cmd=GPIO,12,1')
		else:
			requests.get('http://10.18.20.158/control?cmd=GPIO,12,0')
		await imap_client.logout()


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(check_mailbox('SI-EX-02', 'task.planer', 'pjjz3*Ab'))
	
