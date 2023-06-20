import json

with open('amor.json', 'r') as f:
	data = json.load(f)

#print (data["results"])
#print (type(data))
for pal in data["results"]:
#	print (pal["lexicalEntries"])
	for ent in (pal["lexicalEntries"]):
		print (ent["entries"])

