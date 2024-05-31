import random
import itertools

class SakClass:
    def __init__(self):
        self.letters = self.randomize_sak()

    def randomize_sak(self):
        letters = list("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ" * 2)  # Example: each letter twice
        random.shuffle(letters)
        return letters

    def getletters(self, num=7):
        if len(self.letters) < num:
            num = len(self.letters)
        drawn_letters = [self.letters.pop(random.randint(0, len(self.letters) - 1)) for _ in range(num)]
        return drawn_letters

    def putbackletters(self, letters):
        self.letters.extend(letters)
        random.shuffle(self.letters)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.letters = []

    def __repr__(self):
        return f"Player({self.name})"

    def change_letters(self, sak):
        sak.putbackletters(self.letters)
        self.letters = sak.getletters()

class Human(Player):
    def play(self):
        action = input(f"{self.name}, enter a word, 'change' to change letters, or 'pass' to skip: ").strip().upper()
        return action

class Computer(Player):
    def play(self, valid_words):
        for i in range(7, 1, -1):
            for perm in itertools.permutations(self.letters, i):
                word = "".join(perm)
                if word in valid_words:
                    return word
        return "change" if len(self.letters) > 1 else "pass"

class Game:
    def __init__(self):
        self.sak = SakClass()
        self.player = Human("Human")
        self.computer = Computer("Computer")
        self.load_words()

    def load_words(self):
        with open('greek7.txt', 'r', encoding='utf-8') as file:
            self.words = set(file.read().splitlines())

    def setup(self):
        self.player.letters = self.sak.getletters()
        self.computer.letters = self.sak.getletters()
        print(f"Starting letters for {self.player.name}: {self.player.letters}")
        print(f"Starting letters for {self.computer.name}: {self.computer.letters}")

    def calculate_score(self, word):
        letter_scores = {
            'Α': 1, 'Β': 3, 'Γ': 2, 'Δ': 2, 'Ε': 1, 'Ζ': 4, 'Η': 4, 'Θ': 4,
            'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 3, 'Ν': 1, 'Ξ': 8, 'Ο': 1, 'Π': 3,
            'Ρ': 1, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3
        }
        return sum(letter_scores.get(letter, 0) for letter in word)

    def valid_word(self, word, player_letters):
        if word not in self.words:
            return False
        letters_copy = player_letters.copy()
        for char in word:
            if char in letters_copy:
                letters_copy.remove(char)
            else:
                return False
        return True

    def player_turn(self, player):
        while True:
            action = player.play() if player == self.player else player.play(self.words)
            if action == "PASS":
                return False
            elif action == "CHANGE":
                player.change_letters(self.sak)
                print(f"{player.name} changed their letters. New letters: {player.letters}")
                return False
            elif self.valid_word(action, player.letters):
                score = self.calculate_score(action)
                player.score += score
                print(f"{player.name} played {action} for {score} points. Total score: {player.score}")
                for char in action:
                    player.letters.remove(char)
                player.letters.extend(self.sak.getletters(7 - len(player.letters)))
                print(f"{player.name}'s new letters: {player.letters}")
                return True
            else:
                if player == self.player:
                    print("Invalid word. Try again.")
                else:
                    return False

    def run(self):
        pass_count = 0
        while self.sak.letters or any(self.player.letters) or any(self.computer.letters):
            if not self.player_turn(self.player):
                pass_count += 1
            else:
                pass_count = 0

            if not self.player_turn(self.computer):
                pass_count += 1
            else:
                pass_count = 0

            if pass_count >= 2:
                break

    def end(self):
        print("Game Over")
        print(f"Final Scores: {self.player.name} - {self.player.score}, {self.computer.name} - {self.computer.score}")
        if self.player.score > self.computer.score:
            print(f"The winner is {self.player.name}!")
        elif self.computer.score > self.player.score:
            print(f"The winner is {self.computer.name}!")
        else:
            print("It's a tie!")

### Main program

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.run()
    game.end()