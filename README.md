# Brawlhalla Elo Tracker for Streamers
This program was designed for streamers to always show elo somewhere on their stream overlay. 
It also shows the net elo gain or net elo loss from when the program was launched (ideally at the the beginning of the stream)
This program requires a BrawlhallaAPI key which can be obtained at http://dev.brawlhalla.com. 

# Setup
1. Download or clone the python file
2. Launch the python file from the command line using python elotracker.py bracket playerID apiKey
  <br>ex 1v1: python elotracker.py 1s 1145296 A73JF9JEK1HH4HEFIK1
  <br>ex 2v2: python elotracker.py 2s 1145296 A73JF9JEK1HH4HEFIK1
3. If you selected 2s the program will grab all of your 2s teams and ask you to enter the playerID of the second player. It will output the team names and the ID of the second player if you dont know the second players ID.
4. The program will start by getting a baseline ELO and will update every 1 minute.
5. This information will be put into a text file called "brawlelo.txt". You can use it as a text source in OBS to show it on your stream and it will be updated once per minute.

## Important Note
The Brawlhalla API will output your highest legend ELO or your overall ELO depending on which one is higher (for 1s mode). This can cause your ELO change to be incorrect.
Unfortunately there is nothing I can really do to fix this.
