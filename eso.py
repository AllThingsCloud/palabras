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
import json

if len(sys.argv) < 2:
    print("Palabra requerida. Ejemplo: python",  sys.argv[0], "palabra")
    sys.exit()

app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")
h		= os.getenv("HOME")
palh 	= '/palabras/palex.out'
h += palh
language = 'es'
word_id = sys.argv[1]
strictMatch = 'false'

url = 'https://od-api.oxforddictionaries.com:443/api/v2/sentences/' + language + '/' + word_id.lower() + '?strictMatch=' + strictMatch

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

code = r.status_code 
#print("code {}\n".format(r.status_code))
#print("text \n" + r.text)
if (code == 200):
    try:
        data = json.loads(r.text)
        sentences = data['results'][0]['lexicalEntries'][0]['sentences']

        regions_dict = {}

        for sentence in sentences:
         regions = sentence['regions'][0]['text']
         id = sentence['senseIds'][0]
         text = sentence['text']

         if regions in regions_dict:
            regions_dict[regions].append({'ID': id, 'Text': text})
         else:
            regions_dict[regions] = [{'ID': id, 'Text': text}]

        for region, sentences in regions_dict.items():
            print(f"País: {region}")
            for sentence in sentences:
                print(f"\t {sentence['Text']}")
    except (json.JSONDecodeError, KeyError, IndexError):
        print("Invalid JSON response or missing data.")
elif (code == 404):
    print(Fore.CYAN + word_id,":","No tiene ejemplos","\n")