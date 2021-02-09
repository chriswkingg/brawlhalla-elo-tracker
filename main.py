import requests as r

username = "twitch.tv/lawlbottv"
reigon = "us-e"
apiKey = ""
f = open("brawlelo.txt", "w")

data = r.get(url = "https://api.brawlhalla.com/rankings/1v1/" + reigon + "/1", params = {'name':username, "api_key":apiKey}).json()[0]
currentElo = data["rating"]
startingElo = currentElo

f.write("Current Elo: " + str(currentElo) + " Elo Change: " + str(startingElo - currentElo))
print(data["rating"])