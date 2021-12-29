from beautifultable import BeautifulTable


### Functions ###

# Update table

# A function that calculates scores after a game between players
def game_res(winner, g1, looser, g2, ot):
    a=int(g1)
    b=int(g2)
    winner_values = [1, 1, 0, 0, 0, a, b, a-b, 2]
    looser_values = [1, 0, 1, 0, 0, b, a, b - a, 0]
    ot_winner_values = [1, 0, 0, 1, 0, a, b, a-b, 2]
    ot_looser_values = [1, 0, 0, 0, 1, b, a, b-a, 1]

    for i in range(num):
        x=str(i+1)
        win=str(winner)
        loo=str(looser)
        if win==names['player_'+x]:
            for b in range(9):
                if ot==False:
                    all_scores[i][b]+=winner_values[b]
                else:
                    all_scores[i][b]+=ot_winner_values[b]

        if loo==names['player_'+x]:
            for b in range(9):
                if ot == False:
                    all_scores[i][b] += looser_values[b]
                else:
                    all_scores[i][b] += ot_looser_values[b]

    table = BeautifulTable()
    if num == 2:
        table.rows.append(all_scores[0])
        table.rows.append(all_scores[1])
    elif num == 3:
        table.rows.append(all_scores[0])
        table.rows.append(all_scores[1])
        table.rows.append(all_scores[2])
    elif num == 4:
        table.rows.append(all_scores[0])
        table.rows.append(all_scores[1])
        table.rows.append(all_scores[2])
        table.rows.append(all_scores[3])

    table.rows.header = list_of_names
    table.columns.header = hdrs

    print(table)
    return table





### Input 1 ###
# Getting number of users (1-4)
num = 0
n = True
while n == True:
    num = int(input("Enter number of players (1-4): "))

    if num > 0 and num < 5:
        print("Nice. Number of players is set to " + str(num) + "!")
        print()
        n = False
    elif num > 4:
        print("Number of players is too big!")
        n = True
    else:
        print("Invalid input!")
        n = True

### Defintitions ###

matches_played=["  ||| List of matches played |||   "]

# Creating headers
hdrs = ["GP", "W's", "L's", "OTW's", "OTL's", "GF", "GA", "+/-", "P"]

r_length = 10
c_length = num + 1

initial_scores = [0,0,0,0,0,0,0,0,0]

p1_scores = initial_scores.copy()
p2_scores = initial_scores.copy()
p3_scores = initial_scores.copy()
p4_scores = initial_scores.copy()

full_scores = [p1_scores, p2_scores, p3_scores, p4_scores]
all_scores = []

for i in range(num):
    all_scores.append(full_scores[i])

### Input 2 ###
# Getting player names
print("Give names: ")
print()
names = {}
list_of_names=[]
for x in range(num):
    a = str(input("player_" + str(x + 1) + ": "))
    names['player_' + str(x + 1)]=a
    list_of_names.append(a)
print()

# Table of scores
table = BeautifulTable()
if num == 2:
    table.rows.append(all_scores[0])
    table.rows.append(all_scores[1])
elif num == 3:
    table.rows.append(all_scores[0])
    table.rows.append(all_scores[1])
    table.rows.append(all_scores[2])
elif num == 4:
    table.rows.append(all_scores[0])
    table.rows.append(all_scores[1])
    table.rows.append(all_scores[2])
    table.rows.append(all_scores[3])

table.rows.header = list_of_names
table.columns.header = hdrs




print("Let the games begin!")

n = True
count=0
while n:
    print()
    print("  |||  Options Menu  |||  ")
    print()
    print("[1]: Add game result")
    print("[2]: Show scores")
    print("[3]: Exit")
    print()
    ans = int(input("Choose an option: "))
    print()
    count+=1

    if ans == 1:
        name1 = str(input("Who won?: "))
        name2 = str(input("Who lost?: "))
        g1 = int(input("Goals by winner: "))
        g2 = int(input("Goals by looser: "))
        ot = input("Overtime? (y/n): ")

        if ot == "n":
            ot = False
            match_string = "Match no." + str(count) + " : " + name1 + " - " + name2 + " | " + str(g1) + " - " + str(g2)
        else:
            ot = True
            match_string = "Match no." + str(count) + " : " + name1 + " - " + name2 + " | " + str(g1) + " - " + str(g2)+" (OT)"

        matches_played.append(match_string)

        print()
        for i in range(len(matches_played)):
            print(matches_played[i])
        print()


        print("  |||  Scores  |||  ")
        game_res(name1, g1, name2, g2, ot)




    elif ans == 2:
        print("  |||  Scores  |||  ")
        print()
        print(table)
    elif ans > 3 or ans < 1:
        print("Invalid option!")
    else:
        n = False


