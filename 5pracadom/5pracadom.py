'''
Praca domowa

„Stwórz skrypt, który:
1. Pobiera od użytkownika 1 argument wymagany i 1 opcjonalny (argparse)
2. Tworzy słownik z tych danych oraz bezpiecznego sekretu, a następnie zamienia go na stringa (secrets, json)
3. Tworzy skrót SHA256 danych (hashlib)
4. Koduje całość base64
5. Kopiuje zawartość do schowka (pyperclip)”
'''

import argparse
import secrets
import json
from hashlib import sha256
import base64
import pyperclip

#Taking data from user.
parser = argparse.ArgumentParser(description = 'tell me a secret')
parser.add_argument('-s', '--str', type = str, required = True, help = 'secret word to encode')
parser.add_argument('-s2', '--str2', type = str, required = False, help = 'second word')
#Argument parser.
args = parser.parse_args()
#Transforming the args into JSON.
word = json.dumps(args, default = vars)
word = json.loads(word)
#Appending the secret word to JSON dict.
secret_word = secrets.token_hex(32)
security = {'secret':secret_word}
word.update(security)
#sha254 encoding.
secret_key = sha256(str(word).encode())
secret_key = secret_key.hexdigest().encode()
#base64 ecoding.
b64_code = base64.standard_b64encode(secret_key)
b64_code = b64_code.decode()
#check.
print(b64_code)
#Copy.
pyperclip.copy(b64_code)