import json

with open('amor.json', 'r') as f:
	data = json.load(f)

for pal in data["results"]:
	for ent in (pal["lexicalEntries"]):
		for senses in (ent["entries"]):
			definition= senses["senses"]
			print(definition)
			#print (senses["senses"])
            
			#for definitions in (senses["definitions"]):
			#	print(json.dump(definitions,indent=1))

