from PIL import Image
import json

img = Image.open('map/map_dirt.png').convert('1')
rawData = img.load()
data = {}
block_base = {}

i = 0
for y in range(55):
    for x in range(55):
    	if rawData[x,y] == 0:
	        block_base[str(i)] = {
	        'x' : x - 28,
	        'y' : 0,
	        'z' : y - 28
	        }
        	i += 1
for y in range(55):
    for x in range(55):
    	if rawData[x,y] == 0:
	        block_base[str(i)] = {
	        'x' : x - 28,
	        'y' : 0,
	        'z' : (200/.35641) + y - 28
	        }
        	i += 1
for y in range(55):
    for x in range(55):
    	if rawData[x,y] == 0:
	        block_base[str(i)] = {
	        'x' : x - 28,
	        'y' : 0,
	        'z' : -(200/.35641) + y - 28
	        }
        	i += 1

data['block_base'] = block_base
with open('data.json', 'w') as f:
	json.dump(data, f)
#print(block_base)
