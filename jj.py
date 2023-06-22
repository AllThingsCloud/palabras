import json
import pprint
import re

#jq '.results[].lexicalEntries[0].entries[0].senses[0].definitions[0]'
with open('amor.json', 'r') as f:
	data = json.load(f)

def jf (*args):
	for pal in data["results"]:
		for ent in (pal["lexicalEntries"]):
			for senses in (ent["entries"]):
				for defi in (senses["senses"]):
					definition = senses["senses"]
					#print(defi) #imprime
					#return senses
					return definition
				
r = jf(data)
#print (r)

pprint.pprint(r)