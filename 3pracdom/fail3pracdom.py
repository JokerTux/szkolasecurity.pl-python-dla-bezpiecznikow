'''

Znajdź otwarte API czegoś co cię interesuje np. sportu lub strony z ocenami filmów.
Możesz znaleźć takie API tutaj: https://github.com/public-apis/public-apis.
Stwórz skrypt, który pobiera z tego API interesujące Cię dane i przetwarza je w jakiś sposób.
Skrypt musi wykonywać przynajmniej dwa zapytania do API i zawierać minimum jedną pętlę lub instrukcję if.
Przykład: najczęściej wygrywający kierowca formuły 1 w ciągu ostatnich dwóch sezonów.

Fail ! Api ktore wybralem bylo w postaci JSON`a ,dlugo zajelo mi zrozumienie
,ze BS bedzie zlym parserem JSON`a ale napisalem do ludzi na forum polskiego pythona:
'https://pl.python.org/forum/index.php?topic=12815.0' ktorzy szybko mnie z bledu wyciagneli.

Nauczylem sie czegos nowego , wiem cos wiecej na temat parsowania Jsona 
"Fail nie jest taki zly jak go maluja ;)! "

'''

import json
import requests


def Pln_to_eur():
	#Sciaga API w postaci .json()
	resp = requests.get('https://v6.exchangerate-api.com/v6/193c8f8b3c7a3a10179f0652/latest/EUR').json()
	#Encoding JSON file
	read = json.dumps(resp)
	#Printing and pointing (filtering) at the values what we need
	print(json.loads(read)['conversion_rates']['PLN'])

def Pln_to_chf():
	resp = requests.get('https://v6.exchangerate-api.com/v6/193c8f8b3c7a3a10179f0652/latest/CHF').json()
	read = json.dumps(resp)
	print(json.loads(read)['conversion_rates']['PLN'])


def Pln_to_usd():
	resp = requests.get('https://v6.exchangerate-api.com/v6/193c8f8b3c7a3a10179f0652/latest/USD').json()
	read = json.dumps(resp)
	print(json.loads(read)['conversion_rates']['PLN'])
	

if __name__ == '__main__':
	print('Kurs Euro(€): ')
	Pln_to_eur()

	print('Kurs Dolara($): ')
	Pln_to_usd()

	print('Kurs Franka szwajcarskiego: ')
	Pln_to_chf()