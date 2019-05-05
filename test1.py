import json

def main():
	data = load("./dataTesting.json")
	dataString = loop(data)
	store(dataString)

def loop(data):
	temp = ""
	for i in data:
		for k,v in i.iteritems():
			temp += "%s=%s;" %(k,v)
		temp += "\n"
	return temp

def store(stringData):
	print(stringData)

#read
def load(fileName):
	with open(fileName, "r+") as f:
  		data = json.load(f)
  		return data

if __name__ == '__main__':
	main()
