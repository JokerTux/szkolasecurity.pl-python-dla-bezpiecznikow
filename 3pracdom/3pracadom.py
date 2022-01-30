'''

Znajdź otwarte API czegoś co cię interesuje np. sportu lub strony z ocenami filmów.
Możesz znaleźć takie API tutaj: https://github.com/public-apis/public-apis.
Stwórz skrypt, który pobiera z tego API interesujące Cię dane i przetwarza je w jakiś sposób.
Skrypt musi wykonywać przynajmniej dwa zapytania do API i zawierać minimum jedną pętlę lub instrukcję if.
Przykład: najczęściej wygrywający kierowca formuły 1 w ciągu ostatnich dwóch sezonów.

'''

from selenium import webdriver
from time import sleep
from termcolor import colored

def Check_updates():
	with open('info.txt') as outfile:
		if first_event_title.text in outfile.read():
			print (colored('No new events', 'blue'))
		else:
			print (colored('New event !!', 'red'))	

def Save_info():
	with open('info.txt', 'w') as outfile:
		info = outfile.write(f'{first_event_title.text}, {first_event_date.text}')
		

if __name__ == '__main__':
	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')

	driver = webdriver.Chrome('chromedriver')
	url = "https://muonline.webzen.com/en/news/events"

	try:		
		
		driver.get(url)

		events = driver.find_elements_by_class_name('title')
		first_event_title = events[0]
		second_event_title = events[1]
		dates = driver.find_elements_by_class_name('datetime')
		first_event_date = dates[0]
		second_event_date = dates[1]

		Check_updates()

		print(f'1st event: "{first_event_title.text}", {first_event_date.text}')
		print(f'2nd event: "{second_event_title.text}", {second_event_date.text}')
		
		Save_info()

		# titles = driver.find_elements_by_tag_name('h3')

		# if events and dates is not None:
		# 	for event in events:
		# 		print("New event:\n",event.text)
		# 	for date in dates:
		# 		print("Date:\n",date.text)
	

			# for title in titles:	
			# 	print(title.text)
		# else:
		# 	print("Not found")

	except:
		print("Something went wrong or the server is offline ")		

	finally:
		driver.close()	