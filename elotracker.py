import requests as r
import sched, time, sys

#Global vars
s = sched.scheduler(time.time, time.sleep)
firstID = ""
secondID = ""
apiKey = ""
currentElo = 0
startingElo = 0

#Writes to file and prints so the user knows when its updated
def writeElo():
    global startingElo, currentElo
    print("Elo: " + str(currentElo))
    f = open("brawlelo.txt", "w")
    f.write("Current Elo: " + str(currentElo) + " Elo Change: " + str(currentElo - startingElo))
    f.close()

#Function gets called once per min in ones mode
def getOnes():
    global startingElo, currentElo, firstID, apiKey
    currentElo = r.get(url = "https://api.brawlhalla.com/player/" + firstID + "/ranked", params = {"api_key":apiKey}).json()["rating"]
    writeElo()
    s.enter(60, 1, getOnes)

#Function gets called once per min in twos mode
def getTwos():
    global startingElo, currentElo, firstID, secondID, apiKey
    response = r.get(url = "https://api.brawlhalla.com/player/" + firstID + "/ranked", params = {"api_key":apiKey}).json()
    for i in response["2v2"]:
        if(i["brawlhalla_id_two"] == secondID):
            currentElo = i["rating"]
            break
    writeElo()
    
    s.enter(60, 1, getTwos)    

#Gets basline elo and starts program in ones mode
def startOnes():
    global startingElo, currentElo, firstID, apiKey
    startingElo = r.get(url = "https://api.brawlhalla.com/player/" + firstID + "/ranked", params = {"api_key":apiKey}).json()["rating"]
    currentElo = startingElo
    writeElo()
    
    s.enter(60, 1, getOnes)
    s.run()

#Gets basline elo, gets second player id, and starts program in twos mode
def startTwos():
    global startingElo, currentElo, firstID, secondID, apiKey
    response = r.get(url = "https://api.brawlhalla.com/player/" + firstID + "/ranked", params = {"api_key":apiKey}).json()
    for i in response["2v2"]:
        print("Teamname: " + i["teamname"] + " SecondID: " + str(i["brawlhalla_id_two"]))

    secondID = int(input("Enter second ID: "))
    for i in response["2v2"]:
        if(i["brawlhalla_id_two"] == secondID):
            startingElo = i["rating"]
            currentElo = startingElo
            break
    writeElo()
    
    s.enter(60, 1, getTwos)
    s.run()

#Main
if(len(sys.argv) != 4):
    print("Incorrect number of arguments:\n python elotracker.py bracket brawlID apiKey")
    exit()
firstID = sys.argv[2]
apiKey = sys.argv[3]
if(sys.argv[1] == "1s"):
    startOnes()
elif(sys.argv[1] == "2s"):
    startTwos()