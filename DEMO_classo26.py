import time
import random
import math

day = 0
# 0->morning, 1->evening, 2->dusk, 3->night
timeSlot = 3
timeDisplay = ["🌞","☀️ ","⛅","🌙 ", "morning", "evening", "dusk", "night", "🌄", "🌆", "🌇", "🌃"]
action_choice = []
stressPerTime = -4
healthPerTime = 2

# MONEY | STRESS | HEALTH | ADDICTION   (OBSOLETE)
mainstats = {
    "money": 200,
    "stress": 0,
    "health": 60,
    "addiction": 0
}
laststats = {
    "money": 200,
    "stress": 0,
    "health": 60,
    "addiction": 0
}

# MATH, SCIENCE | LANGUAGE, HISTORY, ART | SOCIAL, HEALTH   (OBSOLETE)
studystats = {
    "math": [0, 13],
    "science": [0, 13],
    "language":[0, 8],
    "history":[0, 8],
    "art":[0, 8],
    "social":[0, -2],
    "health":[0, -2]
}

gamblingstats = [100, 100, 200, 50, 200, -100, 1000, 50, -400, -800, 150, 50, -20000]

diarygambling = [["It's my first time doing something like this", "That was so nervewracking!"
                  "But... at the same time it was really thrilling as well", "Not only that, I also made a 100 today!",
                  "That's one step closer to buying that new game!", "Then.. after that I can quit this",
                  "I mean, I KNOW it's bad but like...", "I really need this money you know",
                  "If I ever lose a ton of money at once, I'll stop"],
                  # 100
                  ["Made another 100", "It was a close one, could've lost ton of money from that",
                  "Good thing I managed to win in the end there.."],
                  # 200
                  ["LET'S GO", "200 THAT'S WHAT I'M TALKING ABOUT", "WOO! That's as much money as my last 2 sessions COMBINED!",
                   "Whoever said that third time's a charm, they are soooo right", "I'm feelin good about this",
                   "If I can keep this up then.. maybe I would have enough money to buy whatever I want,",
                   "whenever I want, that would be awesome"],
                    # 50
                    ["Ahh", "It seems luck isn't on my side this time", "At least I still made some money out of it I guess",
                       "Surely I can do better next time tho..", "And it's not like I've lost any money so there's no harm, right?",
                       "I might as well push my luck to see how much I can get out of this"],
                    # 200
                    ["ANOTHER 200", "I'm so good at this", "It was still a pretty close one as usual but.."
                     , "I just keep winning after winning after winning"],
                    # -100
                    ["My very first loss today...", "But it's okay, right?", "It's only a 100", "Not only that but I already made 650 from this",
                     "Maybe I should stop here tho...", "....", "But it's only my first ever loss", "It's not like anyone can win forever",
                     "There gotta be losses here and there", "Well, as long as I don't loss more than I earn, I should be fine!"],
                    # 1000
                    ["OMG OMG OMG OMG", "omg omg omg", "I KNEW it was the right decision to continue", "A 1000....",
                     "I could do so much with this..", "Not just that, but also that's my first 1000 made from this website",
                     "I just keep winning more and more", "My luck just never seem to run out", "I could maybe even become rich with this!"],
                    #50
                    ["Just made another 50", "nothing too special", "it's something at least I guess.."],
                    # -400
                    ["NO!", "UGHH I ALMOST WON THAT!", "I HAVE to get my money back from that"],
                    # -800
                    ["Just one more", "I can win everything back", "Now I REALLY have to get my money back", "I can't just quit right after losing 800",
                     "Even just a little bit of my money back is fine", "..Then after that I'll actually quit!", "For now, I jusy have to win back what I lost"],
                    # 150
                    ["a 150...", "it's still something at least", "Still, I can't just stop now", "I have to at least get a little bit more back"],
                    # 50
                    ["It's not much...", "Although, as long as I keep winning...", "there's no reason to quit, is there..?"],
                    # final
                    ["I lost it all...", "I lost it all and more...", "What am I supposed to do now..?", "20k down, there is not a chance I get get even a fraction of that back",
                     "Everything I had, it's all gone..", "With this debt that I can't pay off", "What am I supposed to do...", "I should've quited on my very first loss",
                     "If only I wasn't so GREEDY!", "I should've known it was going to go down like this", "I should've known...", "There's nothing I can do now..."]
                ]
gImpact = 0

diarystudy = {
    "math": ["ugh my head is spinning", "I'm starting to regret going to such a competitive school..."],
    "science": ["these topics are quite interesting yet so complex", "an object at rest stays at rest, so why mustn't I rest too huh.. so unfair"],
    "language":["", "hah, this is tiresome.."],
    "history":["learned a lot about our past", "lives were tough in the past, it still is now.."],
    "art":["I am so artful!", "I think I'm starting to get art block.."],
    "social":["the industrial revolution and its consequences", "we live in a society.."],
    "health":["I should keep what I learned in mind to lead a healthy life", "yet studying this much cannot be healthly.."]
}

diaryplay = {
    []
}
gamingSkill = 0
newGameBonus = 1

diaryday = {
    2: ["Yesterday a new game just realeased but my next allowance is in 6 days and I'm almost out of money",
        "I wonder if there's a way I can get money fast", "*searching online for way to make quick bucks*",
        "ooohh would ya look at that, onlinecasino.net huh..", "bet I could earn quick cash to buy this game then stop before I get addicted",
        "  --!unlocked online [gambling] option!--"],
    3: ["They said there's going to be a quiz next Monday", "If I remember correctly, the subjects on the quizes are Math, and History",
        "(!Dev note: the system for randomizing subject for day 8 does not exist, but it should!)", "I should get ready for it",
        "After all, it would be really bad if I fail the first quiz at this school", "Especially with how competitive it is...",
        "  --!NEW OBJECTIVE: reach 40 knowledge in Math and History by day 8!--  "],
    21: ["Hey so...", "The exam is coming up next week", "I really should try my best on it"]
}

diarylog = ["  --sometime ago--  ", "Hey I found this digital diary app thingy", "cool, right? I could write down about my days and stuffs in here"]

ending_list = ["GAMBLING ADDICT", "REHABILITATION"]
game_ending = ""

print("You and your family recently moved and you have enrolled into a new school")
time.sleep(1.2)
print("Allowing you to start fresh at a more prestigious but challenging school")
time.sleep(.8)
print("It's your first day of school tomorrow, goodluck")
time.sleep(1)
input("press [ENTER] to proceed\n!!DEV NOTE: This is a developer demo! and does not fully represent the final product, many features and balancing will be missing\n")
IS_PLAYING = True
while IS_PLAYING:
    timeSlot += 1
    # DAY PRINT
    if timeSlot >= 4:
        day += 1
        timeSlot = 0

        dayprint = day
        if day < 10:
            dayprint = " " + str(dayprint)
        print(f"\n\n====================\n       DAY{dayprint}       ", end="\n ")
        for i in range(-2, 3):
            dayprint = day
            if dayprint+i < 0 or dayprint+i > 30:
                dayprint = "  "
            elif dayprint+i < 10:
                dayprint = " " + str(dayprint+i)
            else:
                dayprint += i
            print(dayprint, end="  ")
        print(f"\n          ^         \n====================")
        time.sleep(.8)

        if len(diarylog) >= 15:
            for i in range(len(diarylog)-15):
                del diarylog[0]
        diarylog.append((f"   --day{dayprint}--   "))

    # STAT PRINT
    if mainstats["stress"] < 0:
        mainstats["stress"] = 0
    if mainstats["health"] > 100:
        mainstats["health"] = 100
    if mainstats["addiction"] < 0:
        mainstats["stress"] = 0
    elif mainstats["addiction"] >= 100:
        mainstats["addiction"] = 100
        IS_PLAYING = False
        game_ending = ending_list[1]
        break

    # money display
    cdisplay = ""
    if laststats["money"] != mainstats["money"]:
        cdisplay = mainstats["money"]-laststats["money"]
        if cdisplay > 0:
            cdisplay = "+"+str(cdisplay)
    print(f"You have [{mainstats["money"]} baht] {cdisplay}")
    # stress display
    display = ""
    for _ in range(int(mainstats["stress"]/5)):
        display += "▮"
    for _ in range(int(20 - (mainstats["stress"]/5))):
        display += "▯"
    cdisplay = ""
    if laststats["stress"] != mainstats["stress"]:
        cdisplay = mainstats["stress"]-laststats["stress"]
        if cdisplay > 0:
            cdisplay = "+"+str(cdisplay)
    print(f"stress: {mainstats["stress"]}/100 {display} {cdisplay}")
    # health display
    display = ""
    for _ in range(int(mainstats["health"]/5)):
        display += "▮"
    for _ in range(int(20 - (mainstats["health"]/5))):
        display += "▯"
    cdisplay = ""
    if laststats["health"] != mainstats["health"]:
        cdisplay = mainstats["health"]-laststats["health"]
        if cdisplay > 0:
            cdisplay = "+"+str(cdisplay)
    print(f"health: {mainstats["health"]}/100 {display} {cdisplay}")
    # addiction display
    display = ""
    for _ in range(int(mainstats["addiction"]/5)):
        display += "▮"
    for _ in range(int(20 - (mainstats["addiction"]/5))):
        display += "▯"
    cdisplay = ""
    if laststats["addiction"] != mainstats["addiction"]:
        cdisplay = mainstats["addiction"]-laststats["addiction"]
        if cdisplay > 0:
            cdisplay = "+"+str(cdisplay) 
    print(f"addiction: {mainstats["addiction"]}/100 {display} {cdisplay}")

    if day in diaryday and timeSlot == 0:
        time.sleep(.6)
        for d in diaryday[day]:
            print(d)
            diarylog.append(d)
            time.sleep(1)

    laststats["money"] = mainstats["money"]
    laststats["stress"] = mainstats["stress"]
    laststats["health"] = mainstats["health"]
    laststats["addiction"] = mainstats["addiction"]

    # PROCEED ACTION
    if not (day == 1 and timeSlot == 0):
        input(f"[ENTER] to proceed to {timeDisplay[timeSlot]}{timeDisplay[timeSlot+4]}\n")
    else:
        print("select your next action with [study] [sleep] [play] [go out] [diary]")
        time.sleep(.8)
        print("more action option may be unlocked as day passes")

    print(f"{timeDisplay[timeSlot]}{timeDisplay[timeSlot+4]}{timeDisplay[timeSlot+8]}")
    performed_action = False
    while not performed_action:
        action = input(">")
        # STUDY
        if action == "study" and (timeSlot == 3 or input("Study early? (this will increase stress) (y/n)") == "y"):
            timeMulti = 1
            if timeSlot != 3:
                timeMulti = 1.5
            for s in studystats:
                sign = "+"
                if studystats[s][1] < 0:
                    sign = ""
                if timeMulti > 1 and studystats[s][1] < 0:
                    timeMulti = 0.5
                print(f"{s} {studystats[s][0]}/150: {sign}{math.floor(studystats[s][1]*timeMulti)} stress")
            if gImpact > 0:
                print(f"Gambling Impact: {0.9**gImpact}x knowledge gain")
            action = input("select subject >")
            if action in studystats:
                performed_action = True
                newlog = ""
                if timeSlot == 3:
                    newlog = (f"I studied {action} today, {diarystudy[action][0]}")
                else:
                    newlog = (f"I studied {action} this {timeDisplay[timeSlot+4]}, {diarystudy[action][1]}")
                print(newlog)
                diarylog.append(newlog)
                time.sleep(.5)
                studystats[action][0] += 10*(0.9**gImpact)
                if timeSlot != 3:
                    timeMulti = 1.5
                    if studystats[action][1] < 0:
                        timeMulti = 0.5
                mainstats["stress"] += math.floor(studystats[action][1]*timeMulti)
        # SLEEP
        elif action == "sleep":
            print("sleep until:")
            for t in range(3-timeSlot):
                print(f"{timeDisplay[timeSlot+t+1]}{timeDisplay[timeSlot+4+t+1]} : {(t+1)*-4} stress | + {(t+1)*2} health")
            print(f"{timeDisplay[timeSlot]}tomorrow : {(4-timeSlot)*4} stress | + {(4-timeSlot)*2} health")
            action = input("select time >")
            i = 0
            for t in timeDisplay[5:8]:
                i += 1
                if action == t and timeSlot<i:
                    performed_action = True
                    mainstats["stress"] += (i-timeSlot)*stressPerTime
                    mainstats["health"] += (i-timeSlot)*healthPerTime
                    timeSlot += i-1
                elif action == "tomorrow":
                    performed_action = True
                    mainstats["stress"] += (4-timeSlot)*stressPerTime
                    mainstats["health"] += (4-timeSlot)*healthPerTime
                    timeSlot = 3
        # PLAY
        elif action == "play":
            timeMulti = 1
            if timeSlot == 3:
                timeMulti = 2
            display = ""
            if newGameBonus > 1:
                display = "!NEW GAME BONUS!"
            print(f"Play] some games: -{10*timeMulti*newGameBonus} stress {display}\nBuy new game: -{400} money | +new game bonus!")
            action = input("[play] [buy] >")
            if action == "play":
                performed_action = True
                gamingSkill += 1
                mainstats["stress"] -= 10*timeMulti*newGameBonus
                if newGameBonus > 1:
                    newGameBonus -= 0.5
            elif action == "buy" and newGameBonus > 1:
                if mainstats["money"] >= 400:
                    performed_action = True
                    mainstats["money"] -= 400
                    mainstats["stress"] -= 1
                    newGameBonus = 2.5
                else:
                    print("You can't afford a new game")
        # GO OUT
        elif action == "go out":
            print("sorry, you can't go out yet")
            time.sleep(1)
            print("Because I, the dev of this demo..")
            time.sleep(0.8)
            print("Is starting to feel really really tired")
            time.sleep(1.4)
            print("Try again next update...")
            time.sleep(0.6)
            print("If there's ever one, that is.")
        # !!ONLINE GAMBLING!!
        elif (action == "gambling" or action == "gamble") and day >= 2:
            if input("Gamble on an online casino website?\n+-??? money | +?? addiction\n(y/n) >") == "y":
                mainstats["money"] += gamblingstats[gImpact]
                performed_action = True
                if gamblingstats[gImpact] > 0:
                    mainstats["addiction"] += math.floor(4 + (gImpact/5))
                else:
                    mainstats["addiction"] += gImpact
                for d in diarygambling[gImpact]:
                    print(d)
                    time.sleep(1)
                gImpact+=1
                if gImpact == 12:
                    IS_PLAYING = False
                    game_ending = ending_list[0]
        # DIARY
        elif action == "diary":
            for l in diarylog:
                print(l)
        elif action == "quit":
            IS_PLAYING = False
            break

        #end | end of if-elif chain
        
    #end) | vvv AFTER ACTION

#end)

if game_ending != "":

    print(f"\n\n▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯\n   {game_ending}\n")
if day <= 30:
    print("final day:", day)
adisplay = ""
for _ in range(int(mainstats["addiction"]/5)):
    adisplay += "▮"
for _ in range(int(20 - (mainstats["addiction"]/5))):
    adisplay += "▯"
print(f"money: {mainstats["money"]}$\naddiction [{adisplay} ]")

print("               Thank You For Playing!\n")