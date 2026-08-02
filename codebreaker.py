import random as r
import os
from datetime import datetime

save_files = ["save1.txt", "save2.txt", "save3.txt"]

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #print intro
    intro()

    while True:
        menu()
        choice = input("Choice: ")

        if choice == "1": #print rules
            rules()

        elif choice == "2": #print new game
            new_game()

        elif choice == "3": #get past game
            load_game_menu()

        elif choice == "4": #end program
            print("Goodbye")
            break

        else: #prompt again
            print("Please enter 1, 2, 3, or 4.")



#intro for when program called
def intro():
    print("While exploring an unknown island, you discovered a mysterious locked treasure box.")
    print("The box contains a valuable secret, but it is protected by a complex")
    print("password lock. Only someone with sharp logic and problem-solving skills")
    print("can uncover the correct combination.")
    print()
    print("Will you break the code and unlock the hidden treasure?")

#create solution as string
def generate_solution(min_len, max_len):
    length = r.randint(min_len, max_len) #program inputs length
    num = '' #empty

    #add randomly generated number one by one into one string
    for _ in range(length):
        temp_num = r.randint(0, 5)  
        random_str = str(temp_num)
        num += random_str 

    #return full number (solution of game)
    return (num)

#print menu options
def menu():
    print("\nMenu:")
    print("--------------------------------------------------------------------------")
    print("   1: Rules")
    print("   2: New Game")
    print("   3: Load Game")
    print("   4: Quit")

#print rules
def rules():
    print("\nRules:")
    print("--------------------------------------------------------------------------")
    print("1. You get 10 guesses to break the lock.\n")
    print("2. Guess the correct code to win the game.\n")
    print("3. Codes can be either 4, 5, or 6 digits in length.\n")
    print("4. Codes can only contain digits 0, 1, 2, 3, 4, and 5.\n")
    print("5. Clues for each guess are given by a number of red and white pins.\n")
    print("   5-a. The number of red pins in the R column indicates the number of digits")
    print("      in the correct location.")
    print("   5-b. The number of white pins in the W column indicates the number of")
    print("      digits in the code, but in the wrong location.")
    print("   5-c. Each digit of the solution code or guess is only counted once in the")
    print("      red or white pins.")

#calculate r/w by comparing user input and solution
def clue(ans, guess):
    red = 0 #in position
    white = 0 #not in position

    #default array with 0
    sol_used = [0] * len(ans)
    g_used = [0] * len(guess)
    places = len(ans)

    #red
    for i in range(len(guess)):
        if i < places and guess[i] == ans[i]: #if answer in correct place
            red += 1
            g_used[i] = 1
            sol_used[i] = 1
            

    #skip
    for j in range(len(guess)):
        if g_used[j] == 1:
            continue

        #white
        for s in range(places):
            if sol_used[s] == 1:

                continue

            if guess[j] == ans[s]: #if number in guess, in ans
                white += 1
                g_used[j] = 1
                sol_used[s] = 1

                break

    #give numbers for board
    return (red, white)

#print and update board
def print_board(answer, guesses, clues, show_ans):
    print("  =+=================+====+=")
    row = "    "

    #show answer?
    if show_ans != 0: #yes
        symbols = []
        for i in range(6):
            if i < len(answer):
                symbols.append(answer[i])
            else:
                symbols.append("o")

    else: #no
        symbols = ["o"] * 6 

    row = row + "  ".join(symbols) #combines number

    print(f"{row} | R W  ")
    print("  =+=================+====+=")

    #print rows (10 guesses)
    for row_ind in range(10, 0, -1):
        index = row_ind - 1

        if index < len(guesses):
            guess = guesses[index]
            clue = clues[index] #list of r/w

            align = []
            for i in guess:
                align.append(i)
            while len(align) < 6:
                align.append("o")

            line = "    " + "  ".join(align) #printable line with alignment fix

            #print line with guess + r/w
            print(f"{line} | {clue[0]} {clue[1]}  ")

        else:
            print("    o  o  o  o  o  o | 0 0  ")

    print("  =+=================+====+=")


#test cases for all user input scenerios
def decide(solution, guesses, clues):
    guess = input("What is your guess (q to quit, s to save and quit): ")

    #quit
    if guess == "q" or guess == "Q":
        print("Ending Game.")
        return "leave"
    #save
    if guess == "s" or guess == "S":
        save_game_menu(solution, guesses, clues)
        return "save"
    
    if len(guess) < 4 or len(guess) > 6:
        print(f'Your guess was "{guess}". Invalid guess type!', end="")

        if len(guess) < 4:
            print(" Your guess is too short.")
            print("Guess lengths must be between 4 and 6.")
        else:
            print("\nGuess lengths must be between 4 and 6.")

        return "continue_no_board"
    
    #not number
    if not guess.isdigit():
        print(f'Your guess was "{guess}". Invalid guess type! The guess must be only numbers!')
        return "continue_no_board"

    #not in range
    if any(d not in "012345" for d in guess):
        print(f'Your guess was "{guess}". Invalid guess type! The guess must be only numbers 0 through 5.')
        return "continue_no_board"
    
    
    r, w = clue(solution, guess)
    guesses.append(guess)
    clues.append((r, w))

    #guess right
    if guess == solution:
        print_board(solution, guesses, clues, 1)
        print("You did it! You cracked the code and unlocked the treasure box!")
        print("Inside, you discover the valuable secret hidden within.")
        print("  ...")
        print("The treasure is yours. Congratulations, codebreaker!")
        print("Ending Game.", end ="")
        print()
        return "win"

# 10 guesses
    if len(guesses) == 10:
        print_board(solution, guesses, clues, 1)
        print("You hear the lock beep and display: OUT OF TRIES!")
        print("  ...")
        print("The treasure box remains locked, and the secret is lost forever.")
        print("  ...")
        print("Your codebreaking mission has failed.")
        print("Ending Game.", end = "")
        print()
        print()
        return "lose"
        
    return "valid"

#load new game
def new_game():
    print("\nNew Game:")
    print("--------------------------------------------------------------------------")

    #new code
    solution = generate_solution(4, 6)
    guesses = []
    clues = []

    print_board(solution, guesses, clues, 0)

    while True:
        result = decide(solution, guesses, clues)

        if result == "valid":
            print_board(solution, guesses, clues, 0)

        if result in ["leave", "save", "win", "lose"]:
            return

        
#save game
def save_game(ans, guesses, clues, slot, player_name):
    timestamp = datetime.now().isoformat(timespec="seconds")
    #save as answer\n --> guess/clue pairs
    with open(save_files[slot], "w") as f:
        f.write(player_name + "\n")
        f.write(timestamp + "\n")
        f.write(ans + "\n")
        for g, c in zip(guesses, clues):
            f.write(f"{g} {c[0]} {c[1]}\n")

#show the menu when requesting save game
def save_game_menu(ans, guesses, clues):
    print("\nFiles:")
    print("--------------------------------------------------------------------------")
    #access saved file if there, else print empty
    for i, file in enumerate(save_files, start=1):
        if os.path.exists(file) and os.path.getsize(file) > 0:

            #first line = player name and second line = timestamp
            with open(file, "r") as f:
                lines = f.read().splitlines() #read file details
                if len(lines) >= 2:
                    name, timestamp = lines[0], lines[1]
                    print(f"   {i}: {name} - Time: {timestamp}")

        else:
            print(f"   {i}: empty")
    
    while True: 
        slot = input("What save would you like to overwrite (1, 2, 3, or c to cancel): ")
        #cancel
        if slot.lower() == "c":
            print("cancelled")
            return
        
        #user decides to save in specific slot
        if slot in ["1","2","3"]:
            slot_idx = int(slot) - 1
        
        #start process of saving
            while True:
                #ask user for name
                name = input("What is your name (no special characters): ")
                if not name.replace(" ","").isalnum():
                    print("That is an invalid name.")
                    continue
                save_game(ans, guesses, clues, slot_idx, name)
                print(f"Game saved in slot {slot} as {name}.")
                print("Ending Game.")
                return
            
        print("Please pick a valid save file.")

#access old game saved as txt file
def load_slot(slot):
    file = save_files[slot]
    #if file user is trying to access is empty --> prompt again
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        print("That file is empty!")
        return None
    
    with open(file, "r") as f:
        lines = f.read().strip().splitlines()
    player_name = lines[0]
    timestamp = lines[1]
    ans = lines[2]
    guesses, clues = [], []

    for line in lines[3:]:
        g, r, w = line.split()
        guesses.append(g)
        clues.append((int(r), int(w)))

    return ans, guesses, clues, player_name, timestamp

#load previous saved game menu
def load_game_menu():
    print("\nFiles:")
    print("--------------------------------------------------------------------------")

    #same verfication loop in save game, 
    for i, file in enumerate(save_files, start=1):
        if os.path.exists(file) and os.path.getsize(file) > 0:
            with open(file, "r") as f:
                name = f.readline().strip()
                timestamp = f.readline().strip()
            print(f"   {i}: {name} - Time: {timestamp}")
        else:
            print(f"   {i}: empty")

    while True:
        slot = input("What save would you like to load (1, 2, 3, or c to cancel): ")
        if slot.lower() == "c":
            print("cancelled")
            return
            
        if slot in ["1","2","3"]:
            slot_idx = int(slot)-1
            data = load_slot(slot_idx)
            #empty
            if data is None:
                continue
            
            #assign variables in order of data(function return variables)
            solution, guesses, clues, player_name, timestamp = data

            #continue game
            print("\nResume Game:")
            print("--------------------------------------------------------------------------")
            print_board(solution, guesses, clues, 0)

            #same verfiication loop as in new game
            while True:
                result = decide(solution, guesses, clues)
                if result == "valid":
                    print_board(solution, guesses, clues, 0)
                if result in ["leave", "save", "win", "lose"]:
                    return
        print("Please pick a valid save file.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
