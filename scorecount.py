Playeronescore=0
Playertwoscore=0

NoOfGamesInMatch=int(input('how many games?'))

for NoOfGamesPlayed in range(NoOfGamesInMatch):
    PlayerOneWins =input('did player 1 win y/n?').upper()
    if PlayerOneWins =='Y':
        Playeronescore+=1
    else:
        Playertwoscore+=1

print(Playeronescore, Playertwoscore)
