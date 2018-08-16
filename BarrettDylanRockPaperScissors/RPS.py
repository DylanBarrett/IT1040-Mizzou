import random
import pickle

class GameStatus():

    def __init__(self, name):
        self.tie = 0

        self.playerWon = 0

        self.pcWon = 0

        self.name = name

    def get_round(self):

        return self.tie + self.playerWon + self.pcWon + 1

# Displays program information, starts main play loop

def main():

    print("Welcome to a game of Rock, Paper, Scissors!")

    print("What would you like to choose?")

    print("")

    game_status = welcomemenu()

    while True:
        play(game_status)

        endGameSelect(game_status)

def welcomemenu():
    while True:
        print("[1]: Start New Game")

        print("[2]: Load Game")

        print("[3]: Quit")

        print("")

        menuselect = int(input("Enter your choice: "))

        if int(menuselect) in [1, 2, 3]:

            break

        else:

            print("Wrong choice. select again.")

    if menuselect == 1:

        name = input("What is your name?: ")

        print(("Hello %s.") % name)

        print("Let's play!")

        game_status = GameStatus(name)

    elif menuselect == 2:

        while True:

            name = input("What is your name?: ")

            try:

                user_file = open('%s.rsp' % name, 'r')

            except IOError:

                print(("Sorry there is no game found with name %s") % name)

                continue

            break

        print(("Welcome back %s.") % name)

        print("Let's play!")

        game_status = pickle.load(user_file)

        displayScoreBoard(game_status)

        user_file.close()

    elif menuselect == 3:

        print("Bye!!!")

        exit()

        return

    return game_status

def play(game_status):

    playerChoice = int(playerMenu())

    pcChoice = pcGenerate()

    outcome = evaluateGame(playerChoice, pcChoice)

    updateScoreBoard(outcome, game_status)

def playerMenu():
    print("Select a choice: \n [1]: Rock \n [2]: Paper \n [3]: Scissors\n")

    menuSelect = int(input("What will it be? "))

    while not validateInput(menuSelect):

        invalidChoice(menuSelect)

        menuSelect = input("Enter a correct value: ")

    return menuSelect

def validateInput(menuSelection):

    if menuSelection in [1, 2, 3]:

        return True

    else:

        return False

def pcGenerate():

    pcChoice = random.randint(1,3)

    return pcChoice

# Calculate ties,wins,lose

def evaluateGame(playerChoice, pcChoice):

    rsp = ['rock', 'paper', 'scissors']

    win_statement = ['Rock breaks scissors', 'Paper covers rock', 'Scissors cut paper']

    win_status = (playerChoice - pcChoice) % 3

    print(("You have chosen %s") % rsp[playerChoice - 1])

    what_to_say =(("Computer has chose %s") % rsp[pcChoice - 1])

    if win_status == 0:

        what_to_say +=(" as Well. TIE!")

    elif win_status == 1:

        what_to_say +=((". %s. You WIN!") % win_statement[playerChoice - 1])

    else:

        what_to_say +=((". %s. You LOSE!") % win_statement[pcChoice - 1])

    print(what_to_say)

    return win_status

# Update track of ties, player wins, and computer wins
def updateScoreBoard(outcome, game_status):

    if outcome == 0:

        game_status.tie += 1

    elif outcome == 1:

        game_status.playerWon += 1

    else:

        game_status.pcWon += 1

# If user input is invalid, let them know.

def invalidChoice(menuSelect):

    print(menuSelect,("is not a valid option. Please select 1-3"))

# Print the scores before terminating the program.

def displayScoreBoard(game_status):
    print("")

    print("Statistics:")

    print(("Ties: %d") % game_status.tie)

    print(("Player Wins: %d") % game_status.playerWon)

    print(("Computer Wins: %d") % game_status.pcWon)

    if game_status.pcWon > 0:

        print(("Win/Loss Ratio: %f") % (float(game_status.playerWon) / game_status.pcWon))

    else:

        print("Win/Loss Ratio: Always Win.")

    print(("Rounds: %d") % game_status.get_round())

def endGameSelect(game_status):
    print("")

    print("[1]: Play again")

    print("[2]: Show Statistics")

    print("[3]: Save Game")

    print("[4]: Quit")

    print("")

    while True:

        menuselect = int(input("Enter your choice: "))

        if menuselect in [1, 2, 3, 4]:

            break

        else:

            print("Wrong input.")

    if menuselect == 2:

        displayScoreBoard(game_status)

        endGameSelect(game_status)

    elif menuselect == 3:

        def load_users(self):
            try:
                f = open("%s.rsp" % game_status.name, 'wb')

                pickle.dump(game_status, f)

                f.close()
            except:
                print("error loading make sure file is valid")
            

        print("Your game is saved successfully.")

        endGameSelect(game_status)

    elif menuselect == 4:

        print("Bye!!!")
        exit()

main()
