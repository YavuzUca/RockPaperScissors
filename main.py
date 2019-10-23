import random as rnd


class Rps:
    def __init__(self, max_score):
        self.options = ['Rock', 'Paper', 'Scissor']
        self.player_score = 0
        self.computer_score = 0
        self.max_score = max_score

    def player_wins(self):
        print("Player has won")
        self.player_score += 1

    def computer_wins(self):
        print("Computer has won")
        self.computer_score += 1

    def scoreboard(self):
        t = str(self.player_score) + " - " + str(self.computer_score)
        print(t)

    # if player chooses rock
    def choice_rock(self, computer_choice):
        if computer_choice == "Paper":
            self.computer_wins()
        elif computer_choice == "Scissor":
            self.player_wins()

    # if player chooses paper
    def choice_paper(self, computer_choice):
        if computer_choice == "Scissor":
            self.computer_wins()
        elif computer_choice == "Rock":
            self.player_wins()

    # if player chooses scissor
    def choice_scissor(self, computer_choice):
        if computer_choice == "Rock":
            self.computer_wins()
        elif computer_choice == "Paper":
            self.player_wins()

    # here starts the game
    def start(self):
        while self.player_score < self.max_score and self.computer_score < self.max_score:
            player_choice = input("Vul je keuze in: ")
            computer_choice = rnd.choice(self.options)

            if player_choice == computer_choice:
                print("Draw")
                self.scoreboard()

            elif player_choice == "Rock":
                self.choice_rock(computer_choice)
                self.scoreboard()

            elif player_choice == "Paper":
                self.choice_paper(computer_choice)
                # self.scoreboard()

            elif player_choice == "Scissor":
                self.choice_scissor(computer_choice)
                # self.scoreboard()


game = Rps(5)
game.start()