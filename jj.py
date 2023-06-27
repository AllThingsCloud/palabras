import json
import pprint
import re
import sys
import requests

app_id = '0ad00461'
app_key = '2b891c1f26db980883b9cebe61df9ea3'
language = 'es'
fields = 'definitions' 
apath ='/Users/roberto/OneDrive/Azure/palabras/palex.out' 
noexistea = '/Users/roberto/OneDrive/Azure/palabras/noexiste'
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  

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
   # expresion_regular = rf"{palabra}\n([\s\S]*?)\n"
  #  matches = re.findall(expresion_regular, texto)

if len(sys.argv) < 2:
    print("Parámetro requerido. Ejemplo: python mi_programa.py <parametro>")
    sys.exit()
else: #buscar si la palabra ya fue buscada
	parametro = sys.argv[1]
	word_id = parametro
	strictMatch = 'false'
	#nox = noexiste(parametro)
	existe = encontrar_definiciones_entre_radical(parametro, apath)	
	for defexiste in existe:
		print(defexiste)
		sys.exit() #sale si ya existe
	url = url + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
	response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
if response.status_code == 404:
	print(f"{parametro}","no existe")
	sys.exit()

if response.status_code == 200:
	wr = open(apath,'a')
	wr.write(f"{parametro}\n") #la encontró y escribe la cabeza - palabra
	print(parametro)
	data2 = json.loads(response.text)	
	definitions2 = extract_definition(data2)
with open (apath,'a') as file:
	wr = open(apath,'a')
	wr.write(f"{parametro}\n") #cierra el para la regex
	for indice, defi in enumerate(definitions2,1):
		file.write(f"{indice}.{defi}\n")
for indice, defi in enumerate(definitions2,1):
	print(f"{indice}.{defi}")



"""
def extract_definition(data):
	definitions2 = []
	for result in data2["results"]:
		for lexicalEntry in result["lexicalEntries"]:
			for entry in lexicalEntry["entries"]:
				for sense in entry["senses"]:
					definitions2.append(sense["definitions"]) #definitions is/es un campo de los resultados in the JSON output file
	return definitions2	

definitions2 = extract_definition(data2)
for indice, defi in enumerate(definitions2,1):
	print(f"{indice}.{defi}")
#print(parametro)
#wr.write(f"{parametro}\n")
"""


""""
def encontrar_definiciones_entre_radical(filename):
    with open(filename, 'r') as f:
        texto = f.read()

    expresion_regular = r"radical radical\n([\s\S]*?)\nradical"
    matches = re.findall(expresion_regular, texto)
    
    return matches

# Llamar a la función y obtener las definiciones
definiciones = encontrar_definiciones_entre_radical('archivo.txt')

# Imprimir las definiciones encontradas
for definicion in definiciones:
    print(definicion)
"""    


######24/06 no se usa lo de abajo 
"""
def jf (*args):
	for pal in data["results"]:
		for ent in (pal["lexicalEntries"]):
			for senses in (ent["entries"]):
				for defi in (senses["senses"]):
					definition = senses["senses"]
					return definition

				

archivo = jf(data)
archivo_sin_claves = [{'definitions': item['definitions']} for item in archivo]

archivo_formateado = json.dumps(archivo_sin_claves,indent=3, ensure_ascii=False)
texto_sin_llaves = archivo_formateado.replace('{','').replace('}','')
texto_sin_llaves = archivo_sin_claves.replace('{','').replace('}','')
texto_sin_apostro = texto_sin_llaves
texto_sin_apostro = texto_sin_llaves.replace(',','').replace('[','').replace(']','')

definiciones = re.findall(r'"definitions":\s+"(.+)"', texto_sin_apostro)
"""