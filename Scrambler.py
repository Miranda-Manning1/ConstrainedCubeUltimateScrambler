# By Miranda Manning
# Written in 2020

import random
import sys

# scramble with green on top and yellow on front

# input four letters:
# 1 (L): F or B
# 2 (U): F, L, or B
# 3 (R): F or B
# 4 (D): F, L, or B
# example starting state input: FLBL

total_turns = 32 # how many turns to do total

while True:
    start_state = input("Starting state: ")
    state = list(start_state)
    
    if start_state.lower() == "quit":
        sys.exit()
        
    scram = ""

    while scram.count(' ') - 1 < total_turns:
        poss_turns = [["F"], ["F'"], ["F2"]]
        
        # L layer
        if state[0] == "B":
            poss_turns.append(["L'", "F", 0])
        else:
            poss_turns.append(["L", "B", 0])
            
        # U layer
        if state[1] == "B":
            poss_turns.append(["U'", "L", 1])
            poss_turns.append(["U2'", "F", 1])
        elif state[1] == "L":
            poss_turns.append(["U", "B", 1])
            poss_turns.append(["U'", "F", 1])
        else:
            poss_turns.append(["U", "L", 1])
            poss_turns.append(["U2", "B", 1])
            
        # R layer
        if state[2] == "B":
            poss_turns.append(["R'", "F", 2])
        else:
            poss_turns.append(["R", "B", 2])
        
        # D layer
        if state[3] == "B":
            poss_turns.append(["D", "L", 3])
            poss_turns.append(["D2", "F", 3])
        elif state[3] == "L":
            poss_turns.append(["D", "F", 3])
            poss_turns.append(["D'", "B", 3])
        else:
            poss_turns.append(["D'", "L", 3])
            poss_turns.append(["D2'", "B", 3])
        
        turn = random.choice(poss_turns)
        scram = scram + turn[0] + " "
        
        if "F" not in turn[0]:
            state[turn[2]] = turn[1]
            
        
        # looks through the scramble to cancel out turns
        scram = scram.replace("L L' ", "")
        scram = scram.replace("L' L ", "")
        scram = scram.replace("R R' ", "")
        scram = scram.replace("R' R ", "")
        scram = scram.replace("U U' ", "")
        scram = scram.replace("U' U ", "")
        scram = scram.replace("U2 U2' ", "")
        scram = scram.replace("U2' U2 ", "")
        scram = scram.replace("U U2' ", "U' ")
        scram = scram.replace("U2 U' ", "U ")
        scram = scram.replace("D' D ", "")
        scram = scram.replace("D D' ", "")
        scram = scram.replace("D2 D2' ", "")
        scram = scram.replace("D2' D2 ", "")
        scram = scram.replace("D2' D ", "D' ")
        scram = scram.replace("R' L R ", "L ")
        scram = scram.replace("D' D2 ", "D ")
        scram = scram.replace("F' F' ", "F2 ")
        scram = scram.replace("F F ", "F2 ")
        scram = scram.replace("F F2 ", "F' ")
        scram = scram.replace("F' F2 ", "F ")
        scram = scram.replace("F2 F' ", "F ")
        scram = scram.replace("F2 F ", "F' ")
        scram = scram.replace("F2 F2 ", "")
        scram = scram.replace("F' F ", "")
        scram = scram.replace("F F' ", "")
        scram = scram.replace("D D2' ", "D' ")
        scram = scram.replace("D' D2 ", "D ")
        scram = scram.replace("F F2 ", "F' ")
        scram = scram.replace("D' D' ", "D2' ")
        scram = scram.replace("D D ", "D2 ")
        scram = scram.replace("U' D U ", "D ")
        scram = scram.replace("U' D' U ", "D' ")
        scram = scram.replace("U' U2 ", "U ")
        scram = scram.replace("R L' R' ", "L' ")
        scram = scram.replace("U2' U ", "U' ")
        scram = scram.replace("D' U D' ", "D2' U")
        scram = scram.replace("U D' U' ", "D' ")
        scram = scram.replace("U' D2 U ", "D2 ")
        scram = scram.replace("U D2 U ", "U2 D2 ")
        scram = scram.replace("D2' U' D2 ", "U' ")
        scram = scram.replace("U U ", "U2 ")
        scram = scram.replace("D2 D' ", "D ")
        scram = scram.replace("U D U' ", "D ")
        scram = scram.replace("U' U' ", "U2' ")
        scram = scram.replace("U' D' U2 ", "U D' ")
        scram = scram.replace("D' U2 D2 ", "D U2 ")
        scram = scram.replace("U2' D' U2 ", "D' ")
        scram = scram.replace("D' U2 D' ", "D2' U2 ")
        scram = scram.replace("U2 D' U' ", "U D' ")
        scram = scram.replace("D2' U2' D2 ", "U2' ")
        scram = scram.replace("U2' D2 U ", "U' D2 ")
        scram = scram.replace("D U2' D ", "D2 U2' ")
        scram = scram.replace("U' D' U' ", "U2' D' ")
        scram = scram.replace("D U' D' ", "U' ")
        scram = scram.replace("U' D2' U ", "D2' ")
        scram = scram.replace("D' U2' D2 ", "D U2' ")
        scram = scram.replace("D2' U D ", "D' U ")
        scram = scram.replace("R' L' R ", "L' ")
        scram = scram.replace("L' R L ", "R ")
        scram = scram.replace("L R' L' ", "R' ")
        scram = scram.replace("D2' U D ", "D' U ")
        scram = scram.replace("D2 U D' ", "D U ")
        scram = scram.replace("D2' U D2 ", "U ")
        scram = scram.replace("U2 D U2' ", "D ")
        scram = scram.replace("U D U2' ", "U' D ")
        scram = scram.replace("D' U D2 ", "D U ")
        scram = scram.replace("U D2 U2' ", "U' D2 ")
        scram = scram.replace("D2 U2' D2' ", "U2' ")
        scram = scram.replace("L R L' ", "R ")
        scram = scram.replace("U D2' U2' ", "U' D2' ")
        scram = scram.replace("D U D ", "D2 U ")
        scram = scram.replace("D2 U2' D' ", "D U2' ")
        scram = scram.replace("D U2 D' ", "U2 ")
        scram = scram.replace("U2 D' U2' ", "D' ")
        scram = scram.replace("D' U2' D ", "U2' ")
        scram = scram.replace("U D' U ", "U2 D' ")
        scram = scram.replace("D' U' D2 ", "D U' ")
        scram = scram.replace("D' U D ", "U ")
        scram = scram.replace("D2 U2 D2' ", "U2 ")
        scram = scram.replace("U2 D2' U' ", "U D2' ")
        scram = scram.replace("D U D' ", "U ")
        scram = scram.replace("U2' D2' U2 ", "D2' ")
        scram = scram.replace("D2' U2 D2 ", "U2 ")
        scram = scram.replace("U2 D2 U' ", "U D2 ")
        scram = scram.replace("D2 U' D2' ", "U' ")
        scram = scram.replace("U' D2' U' ", "U2' D2' ")
        scram = scram.replace("U2' D U2 ", "D ")
        scram = scram.replace("D U2' D' ", "U2'" )
        scram = scram.replace("D U D2' ", "D' U ")
        scram = scram.replace("U2 D U' ", "U D ")
        scram = scram.replace("D U' D2' ", "D' U'")
        
        #counting_turns = counting_turns + 1
        
    scram = scram[:-1]
    print(scram)
    print()
