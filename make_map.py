from PIL import Image
import json

img = Image.open('map/map_dirt.png').convert('1')
rawData = img.load()
data = {}
block_base = {}

i = 0
for y in range(25):
    for x in range(25):
    	if rawData[x,y] == 0:
	        block_base[str(i)] = {
	        'x' : x - 13,
	        'y' : 0,
	        'z' : y - 13
	        }
        	i += 1

data['block_base'] = block_base
with open('data.json', 'w') as f:
	json.dump(data, f)
#print(block_base)
