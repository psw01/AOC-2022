myScore = 0

scores = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
    "WIN" : 6,
    "DRAW" : 3,
    "LOSE": 0
}

def getDraw(n):
    global me
    me = n

def getWin(n):
    global me
    if(n == "A"): me = "Y"
    if(n == "B"): me = "Z"
    if(n == "C"): me = "X"


def getLose(n):
    global me
    if(n == "A"): me = "Z"
    if(n == "B"): me = "X"
    if(n == "C"): me = "Y"


def checkWIN(elves, me):
    if(me == elves): return "DRAW"
    if(me == 1 and elves != 2): return "WIN"
    if(me == 2 and elves != 3): return "WIN"
    if(me == 3 and elves != 1): return "WIN"
    return "LOSE" 


def cheatV2(n, me):
    match me:
        case "X":
            if(n == "A"): return "Z"
            if(n == "B"): return "X"
            if(n == "C"): return "Y"
        case "Y":
            return n
        case "Z":
            if(n == "A"): return "Y"
            if(n == "B"): return "Z"
            if(n == "C"): return "X"

with open('./day2.txt') as f:
    for line in f:
        elves, me = line.strip().split()
        # print(elves, me)
        me = cheatV2(elves, me)
        # print(elves, me)
        # print("Score: ", scores[checkWIN(scores[elves], scores[me])] + scores[me])
        # print(checkWIN(scores[elves], scores[me]))
        # print('-'*69)
        myScore += scores[checkWIN(scores[elves], scores[me])] + scores[me]

print('myScoreIs ', myScore)