import json


ar = []
f = open('mat.txt', encoding='utf-8')
for i in f:
    slovo = i.strip()
    ar += [slovo]

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)







