import requests
import json
import sys

#https://developer.oxforddictionaries.com/admin/applications
#02/jul removí app_id+key
app_id = ''
app_key = ''
language = 'es'
#25/03 https://tecadmin.net/python-command-line-arguments/
#20/04xrevisar https://od-api.oxforddictionaries.com/api/v2/words/es?q=garra&fields=definitions
#word_id = 'corazón'
fields = 'definitions' 
#origword_id = str(sys.argv[1])
#https://stackoverflow.com/questions/2194163/python-empty-argument
if len(sys.argv) == 1:
	print ("Falta la palabra 😼🐮🙃\n")
else:
	word_id = str(sys.argv[1])
	onedesout= '/Users/roberto/OneDrive/Azure/palabras/noexistepal' #texto
	strictMatch = 'false'
	url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

	if (r.status_code) == 200:
		print(r.text) #salida para fep y jq
#lee json
		#https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file
		f = open ('/Users/roberto/t/es.json','a') 
		f.write(r.text)
		f.close
	elif (r.status_code) == 404:
		#print("{} 😬🤨🤔 " .format(r.status_code) + word_id + "\n") # sin el print deja de producir el error del jq
		f = open (onedesout,'a') 
		f.write(word_id+"\n")
		f.close
		quit ()
		#Rprint("json \n" + json.dumps(r.json()))
