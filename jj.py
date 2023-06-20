import json

with open('amor.json', 'r') as f:
	data = json.load(f)

print (data["results"])

#results[].lexicalEntries[]
