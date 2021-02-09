import requests as r
import sched, time

#Global vars
s = sched.scheduler(time.time, time.sleep)
username = "twitch.tv/lawlbottv"
reigon = "us-e"
apiKey = ""
currentElo = 0
startingElo = 0

#Makes api request and writes elo and change to file
def getElo():
    currentElo = r.get(url = "https://api.brawlhalla.com/rankings/1v1/" + reigon + "/1", params = {'name':username, "api_key":apiKey}).json()[0]['rating']
    f = open("brawlelo.txt", "w")
    f.write("Current Elo: " + str(currentElo) + " Elo Change: " + str(currentElo - startingElo))
    f.close()
    print("Current Elo:", currentElo)
    s.enter(60, 1, getElo)

#Main
startingElo = r.get(url = "https://api.brawlhalla.com/rankings/1v1/" + reigon + "/1", params = {'name':username, "api_key":apiKey}).json()[0]['rating']
currentElo = startingElo
print("Starting Elo:", startingElo)
f = open("brawlelo.txt", "w")
f.write("Current Elo: " + str(currentElo) + " Elo Change: " + str(startingElo - currentElo))
f.close()

#Scheduler to run getElo every minute
s.enter(60, 1, getElo)
s.run()