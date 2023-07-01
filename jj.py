#!/usr/bin/env python3

import json
import pprint
import re
import sys
import requests
from colorama import init, Fore, Style

app_id = '0ad00461'
app_key = '2b891c1f26db980883b9cebe61df9ea3'
language = 'es'
fields = 'definitions' 
apath ='/Users/roberto/OneDrive/Azure/palabras/palex.out' 
noexistea = '/Users/roberto/OneDrive/Azure/palabras/noexistepal'
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
    expresion_regular = rf"{palabra}\n([\s\S]*?)\n{palabra}"
    matches = re.findall(expresion_regular, texto)
    return matches

def noexiste(palabra):
	with open(noexistea, 'r') as f:
		texto = f.read()
	if palabra in texto:
		return True
	else:
		return False

if len(sys.argv) < 2:
    print("Palabra requerida. Ejemplo: python",  sys.argv[0], "palabra")
    sys.exit()
else: #buscar si la palabra ya fue buscada
	parametro = sys.argv[1]
	word_id = parametro
	strictMatch = 'false'
	existe = encontrar_definiciones_entre_radical(parametro, apath)	
	for defexiste in existe:
		print(Fore.WHITE + defexiste)
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

