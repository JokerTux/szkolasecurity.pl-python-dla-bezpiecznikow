import re

if __name__ == '__main__':
	def PhpFilter():	
		# Open 'fuff.log' and read the file
		with open('ffuf.log', 'r') as infile:		
			logs = infile.read()
			# Splits for a better look
			for log in logs.split('\n'):
				log = log.replace(',', ' ')
				log_split = log.split(' ')
				
				path = log_split[0]
				status_code = log_split[2]
				size = log_split[5]
				
				#print(f'{path}|{status_code}|{size}')
				user = re.search('user.php$', path)
				admin = re.search('admin.php$', path)

				# Whats a better way to write this 4 lines ?
				if user:
					print(path)
				if admin:
					print(path)			
		
	PhpFilter()			









	
		

		
			
