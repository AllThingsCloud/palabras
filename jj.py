import json
import pprint
import re
import sys
import requests

app_id = '0ad00461'
app_key = '2b891c1f26db980883b9cebe61df9ea3'
language = 'es'
fields = 'definitions' 

if len(sys.argv) < 2:
    print("Parámetro requerido. Ejemplo: python mi_programa.py <parametro>")
    sys.exit()
else: #buscar si la palabra existe
	parametro = sys.argv[1]
	word_id = parametro
	strictMatch = 'false'
	url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
	response = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	#jf = open('/Users/roberto/OneDrive/Azure/palabras/jj.json','a') 
	#jf.write(response.text)
	#jf.close
if response.status_code == 200:
	data = json.loads(response.text)	
	data2 = json.loads(response.text)	
	print(parametro)

#nombre_archivo = parametro
#parametro = data

def extract_definition(data):
	definitions2 = []
	for result in data2["results"]:
		for lexicalEntry in result["lexicalEntries"]:
			for entry in lexicalEntry["entries"]:
				for sense in entry["senses"]:
					definitions2.append(sense["definitions"]) #definitions is/es un campo de los resultados in the JSON output file
	return definitions2	

definitions2 = extract_definition(data)

for indice, defi in enumerate(definitions2,1):
	print(f"{indice}.{defi}")
print(parametro)

with open ('jpal.txt','a') as file:
	for indice, defi in enumerate(definitions2,1):
		file.write(f"{indice}.{defi}\n")



######24/06 no se usa lo de abajo 
 
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
#texto_sin_llaves = archivo_sin_claves.replace('{','').replace('}','')
texto_sin_apostro = texto_sin_llaves
texto_sin_apostro = texto_sin_llaves.replace(',','').replace('[','').replace(']','')

definiciones = re.findall(r'"definitions":\s+"(.+)"', texto_sin_apostro)
