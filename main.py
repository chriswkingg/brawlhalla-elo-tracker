import requests as r

username = "twitch.tv/lawlbottv"
reigon = "us-e"
apiKey = ""

request = r.get(url = "https://api.brawlhalla.com/rankings/1v1/" + reigon + "/1", params = {'name':username, "api_key":apiKey})
print(request.json().split(','))