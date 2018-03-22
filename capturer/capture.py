import requests
import time
import json
from pprint import pprint
import os.path

url = "https://euw1.api.riotgames.com/lol/platform/v3/champions?tags=all&api_key=RGAPI-fa7c7d07-7c17-4c8d-883a-9047926e59da"
r = requests.get(url)

print r.json()

with open('data/champions.json', 'wb') as handle:
    handle.write(r.content)

data = r.json()
#pprint(data)
#pprint(data["champions"][2])
for champion in data["champions"]:
    if (os.path.isfile('data/champion'+str(champion["id"])+'.json')):
        continue
    time.sleep(1)
    url = "https://euw1.api.riotgames.com/lol/static-data/v3/champions/"+str(champion["id"])+"?tags=all&api_key=RGAPI-fa7c7d07-7c17-4c8d-883a-9047926e59da"
    r = requests.get(url)
    pprint(r.content)
    dataChampion = r.json()
    if not "status" in  dataChampion:
        print "Guardado "+str(champion["id"])
        with open('data/champion'+str(champion["id"])+'.json', 'wb') as handle:
            handle.write(r.content)