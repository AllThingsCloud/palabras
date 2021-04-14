import requests
import json
import sys

# TODO: replace with your own app_id and app_key
app_id = '0ad00461'
app_key = '2b891c1f26db980883b9cebe61df9ea3'
language = 'es'
#25/03 https://tecadmin.net/python-command-line-arguments/
#word_id = 'corazón'
fields = 'definitions' 
#origword_id = str(sys.argv[1])
#https://stackoverflow.com/questions/2194163/python-empty-argument
if len(sys.argv) == 1:
	print ("Falta la palabra 😼🐮🙃\n")
else:
	word_id = str(sys.argv[1])
	strictMatch = 'false'
	url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

	if (r.status_code) == 200:
		#original print("text \n" + r.text)
		#originalprint("\n" + r.text)
		print(r.text)
#json lee
		alist = json.dumps(r.json())
		#print(alist)
		print(alist[0])
		#print(alist[0]['word'])
		#https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file
		f = open ('/Users/roberto/t/es.json','a') 
		f.write(r.text)
		f.close
	elif (r.status_code) == 404:
		print("{} 😬🤨🤔 " .format(r.status_code) + word_id + "\n")
		#Rprint("json \n" + json.dumps(r.json()))
