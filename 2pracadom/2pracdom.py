'''
Praca domowa:
Napisz skrypt, przefiltruje plik ffuf.out i zostawi jedynie ściezki z rozszerzeniem .php,
w których nazwie pliku (nie folderu) znajduje się słowo „admin” lub „user”
'''

import re

if __name__ == '__main__':
	def PhpFilter():	
		# Open 'fuff.log' and read the file
		with open('ffuf.log', 'r') as infile:		
			logs = infile.read()
			# Splits for a better view.
			for log in logs.split('\n'):
				log = log.replace(',', ' ')
				log_split = log.split(' ')
				
				path = log_split[0]
				status_code = log_split[2]
				size = log_split[5]
				#print(f'{path}|{status_code}|{size}')
				
				#Searching for filenames				
				keyword = re.search('/*(admin|user)[^/]*\.php$', path)
				try:
					if keyword:
						print(path)
				except:
					print("Nothing found")			
	try:	
		PhpFilter()
	except:
		print("oooops something went wrong...")			
	finally:
		print("https://szkolasecurity.pl/python/")
		print("https://www.linkedin.com/in/gniedziela/")		
