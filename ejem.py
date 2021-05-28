import requests
import json
import sys

#https://developer.oxforddictionaries.com/admin/applications
app_id = '0ad00461'
app_key = '2b891c1f26db980883b9cebe61df9ea3'
language = 'es'
#25/03 https://tecadmin.net/python-command-line-arguments/
fields = 'examples' 
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
		#original print("text \n" + r.text)
		#originalprint("\n" + r.text)
		print(r.text)
#json lee
		#https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file
		f = open ('/Users/roberto/Onedrive/Azure/palabras/ejemes.json','a') 
		f.write(r.text)
		f.close
	elif (r.status_code) == 404:
		print("{} 😬🤨🤔 " .format(r.status_code) + word_id + "\n")
		#f = open ('/Users/roberto/Onedrive/Azure/palabras/noexistepal','a') 
		f = open (onedesout,'a') 
		f.write(word_id+"\n")
		f.close
		#Rprint("json \n" + json.dumps(r.json()))
