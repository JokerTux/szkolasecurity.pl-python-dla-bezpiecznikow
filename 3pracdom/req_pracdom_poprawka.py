'''Jeżeli to możliwe, to lepiej uniknąć wykorzystania chromium - jest to bardzo kosztowne jeżeli chodzi o zasoby Twojego kompa
i zajmuje trochę czasu. Jeżeli po prostu wyciągasz dane z HTMLa,to wystarczy zrobić request modułem requests i przekazać to do beautifulsoap 
i dalej wyciągnąć je w podobny sposób jak to robisz teraz. Chromium dobrze jest używać, jeżeli istotne jest dla Ciebie, żeby JavaScript na stronie
działał (jak tak było tu, to użycie było uzasadnione), kiedy musisz zrobić screenshota, itp.'''


from bs4 import BeautifulSoup
import requests
import re


if __name__ == '__main__':

	USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
	#url = "https://muonline.webzen.com/en/news/events"
	url = "https://szkolasecurity.pl/python/"
	headers = {"user_agent":USER_AGENT}

	try:
		r = requests.get(url,headers)
		#bs4 needs an html output to parse, transform the request into html.
		html = r.text
		soup = BeautifulSoup(html, 'lxml')
		cena_html = soup.find('p', 'brz-css-rusol')
		cena_html = cena_html.get_text(strip=True)
		cena_html = str(cena_html)
		cena = re.findall('[0-9]+', cena_html)
		cena = cena[0]
		print('Aktualna cena za kurs PythonDlaBezpiecznikow wynosi :'+ cena + 'zł')



	except:
		print("Something went wrong or the server is offline ")	

	finally:
		print(url)
		r.close()

