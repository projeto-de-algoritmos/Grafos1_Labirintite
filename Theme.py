import json

class Theme():
	def __init__(self, path):
		file = open(path)
		data = json.load(file)
		self.theme_name = data["theme_name"]

		data = data["colors"]
		self.created = data["created"]
		self.filler = data["filler"] 
		self.visited = data["visited"] 
		self.wall = data["wall"] 
		self.queued = data["queued"]
		self.path = data["path"]
		self.character = data["character"] 
		self.goal = data["goal"] 

		file.close()

def define_theme(theme):
	file = open("theme.json", "w")
	file.write(json.dumps(theme, indent = 4))
	file.close()

def get_colors():
	theme = Theme("theme.json")
	return theme

def next_theme():
	file = open("colors.json")
	actual = get_colors().theme_name
	data = json.load(file)["all_colors"]
	file.close()

	i = 0
	for i in range(len(data)):
		if data[i]["theme_name"] == actual:
			if(i == len(data) - 1):
				define_theme(data[0])
				return data[0]["theme_name"]
			define_theme(data[i+1])
			return data[i+1]["theme_name"]