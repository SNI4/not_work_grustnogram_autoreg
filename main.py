import requests, faker, random, time
import config as cfg
from threading import Thread
from datetime import datetime

fake_en = faker.Faker(locale="en_US")

def main():
	try:
		global mes_id
		email = requests.post('https://web2.10minemail.com/mailbox', headers={
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
		}).json()

		rnd_pass = fake_en.password(cfg.length, cfg.special_chairs, cfg.digits, cfg.uppercase, cfg.lowercase)
		reg = requests.post('https://api.grustnogram.ru/users', headers={
			'Connection': 'keep-alive',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Yandex";v="22"',
			'DNT': '1',
			'sec-ch-ua-mobile': '?0',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Accept': 'application/json',
			'sec-ch-ua -platform': "Windows"}, data={

			'nickname': f'{fake_en.user_name()}{random.randint(1, 9999)}',
			'email': email['mailbox'],
			'password': rnd_pass,
			'password_confirm': rnd_pass})

		time.sleep(3)

		get_message = requests.get('https://web2.10minemail.com/messages', headers={
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
			'authorization': email['token']
		}).json()['messages']

		for i in get_message:
			mes_id = i['_id']
		mes_req = requests.get(f'https://web2.10minemail.com/messages/{mes_id}', headers={
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
			'authorization': email['token']
		}).json()

		account_activate = requests.post('https://api.grustnogram.ru/activate', headers={
			'Connection': 'keep-alive',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Yandex";v="22"',
			'DNT': '1',
			'sec-ch-ua-mobile': '?0',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Accept': 'application/json',
			'sec-ch-ua -platform': "Windows"}, data={

			'code': mes_req['bodyHtml'][268:-96]
		})
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print(f'{current_time} | [+]account reg successful[+]')
		with open('tokens1.txt', 'a') as tokfile:
			tokfile.write(account_activate.json()["data"]["access_token"] + '\n')
		with open('emailpass.txt', 'a') as logfile:
			logfile.write(f'{email["mailbox"]}:{rnd_pass}\n')
	except Exception as error:
		print(error)


def loop1():
	while True:
		main()
def loop2():
	while True:
		main()
def loop3():
	while True:
		main()
def loop4():
	while True:
		main()
def loop5():
	while True:
		main()
def loop6():
	while True:
		main()
def loop7():
	while True:
		main()
def loop8():
	while True:
		main()
Thread(target=loop1).start()
Thread(target=loop2).start()
Thread(target=loop3).start()
Thread(target=loop4).start()
Thread(target=loop5).start()
Thread(target=loop6).start()
Thread(target=loop7).start()
Thread(target=loop8).start()