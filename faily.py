with open('1.txt', 'a') as f:
    f.write('456')
import json
data = [1,2,3,4,5]
with open('1,json', 'a') as f:
	json.dump(data,f)