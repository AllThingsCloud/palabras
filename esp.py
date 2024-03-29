#!/usr/bin/env python3

import json
import pprint
import re
import sys
import requests
from colorama import init, Fore, Style
from dotenv import load_dotenv 
import os
load_dotenv()

app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")
h		= os.getenv("HOME")
palh 	= '/palabras/palex.out'
h += palh
language = 'es'
fields = 'definitions' 
apath = h
noexistea = '/Users/roberto/palabras/noexistepal'
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def extract_definition(data):
	definitions2 = []
	for result in data2["results"]:
		for lexicalEntry in result["lexicalEntries"]:
			for entry in lexicalEntry["entries"]:
				for sense in entry["senses"]:
					definitions2.append(sense["definitions"]) #definitions is/es un campo de los resultados in the JSON output file
	return definitions2	

def encontrar_definiciones_entre_radical(palabra, filename):
    with open(filename, 'r') as f:
        texto = f.read()
    #expresion_regular = rf"{palabra}\n([\s\S]*?)\n{palabra}"
    expresion_regular = rf"\b{palabra}\b\n([\s\S]*?)\n\b{palabra}\b"
    matches = re.findall(expresion_regular, texto)
    return matches

def noexiste(palabra):
	with open(noexistea, 'r') as f:
		texto = f.read()
		palex = texto.split()
	if palabra in palex:
		return True
	else:
		return False

if len(sys.argv) < 2:
    print("Palabra requerida. Ejemplo: python",  sys.argv[0], "palabra")
    sys.exit()
else: #buscar si la palabra ya fue buscada
	parametro = sys.argv[1]
	word_id = parametro
	strictMatch = 'true'
	nxp = noexiste(parametro)
	if nxp == True: print (Fore.MAGENTA + sys.argv[1],": ya fue buscada y no existe");sys.exit() #si ya fue buscada sale y no la busca otra vez
	existe = encontrar_definiciones_entre_radical(parametro, apath)	
	for defexiste in existe:
		print(Fore.WHITE + defexiste);print(Fore.RESET + sys.argv[1])
		sys.exit() #sale si ya existe
	url = url + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
	response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
if response.status_code == 404:
	print(f"{parametro}","no existe")
	nx = open(noexistea,'a')
	nx.write(f"{parametro}\n")
	sys.exit()

if response.status_code == 200:
	wr = open(apath,'a')
	wr.write(f"{parametro}\n") #la encontró y escribe la cabeza - palabra
	print(Fore.LIGHTCYAN_EX + parametro)
	data2 = json.loads(response.text)	
	definitions2 = extract_definition(data2)
	h = histogram(parametro)
	print(h)
with open (apath,'a') as file:
	wr = open(apath,'a')
	wr.write(f"{parametro}\n") #cierra el para la regex
	for indice, defi in enumerate(definitions2,1):
		file.write(f"{indice}.{defi}\n")
for indice, defi in enumerate(definitions2,1):
	print(f"{indice}.{defi}")
	#

