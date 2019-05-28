import random
# create a RPS REPL loop
# have a computer AI to play agains
# keep track of the score
# rules: r beats s, s beats p, p beats r

# track the wins, losses and draws
wins = 0
losses = 0
ties = 0
# create a choices list for the AI to use
choices = ["r", "p", "s"]
# REPL loop for the main updates
while True:
    # display the score
    print(f"Score: {wins} - {losses} - {ties}")
    # take input from the user
    cmd = input("\nChose r/p/s: ")
    # AI to peek number choice/number
    ai_choice = choices[random.randrange(3)]

    # logic to  check for win, loss or tie
    if cmd == "s":
        if ai_choice == "r":
            losses += 1
            print("You lose")
        elif ai_choice == "p":
            wins += 1
            print("You win")
        elif ai_choice == "s":
            ties += 1
            print("tou tied")
    if cmd == "p":
        if ai_choice == "s":
            losses += 1
            print("You lose")
        elif ai_choice == "r":
            wins += 1
            print("You win")
        elif ai_choice == "p":
            ties += 1
            print("tou tied")
    if cmd == "r":
        if ai_choice == "p":
            losses += 1
            print("You lose")
        elif ai_choice == "s":
            wins += 1
            print("You win")
        elif ai_choice == "r":
            ties += 1
            print("tou tied")
    # exit conditions
    elif cmd == "q":
        print("Goodbye")
        break
