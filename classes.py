import random

class SakClass:
    """Class representing the sack of letters in the game."""

    def __init__(self, letters):
        """
        Initialize the SakClass object.

        Args:
            letters (list): List of letters in the sack.
        """
        self.letters = letters

    def add_letter(self, letter):
        """
        Add a letter to the sack.

        Args:
            letter (str): The letter to add.
        """
        self.letters.append(letter)

    def remove_letter(self, letter):
        """
        Remove a letter from the sack.

        Args:
            letter (str): The letter to remove.
        """
        self.letters.remove(letter)

    def shuffle(self):
        """Shuffle the letters in the sack."""
        random.shuffle(self.letters)


class Player:
    """Base class representing a player in the game."""

    def __init__(self, name):
        """
        Initialize the Player object.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.score = 0
        self.letters = []

    def __repr__(self):
        """
        Return a string representation of the Player object.

        Returns:
            str: String representation of the player.
        """
        return f"Player(name={self.name}, score={self.score}, letters={self.letters})"

    def play(self, sak):
        """
        Play a turn in the game.

        Args:
            sak (SakClass): The sack of letters in the game.
        """
        raise NotImplementedError("Method 'play' must be implemented in derived classes.")


class Human(Player):
    """Class representing a human player in the game."""

    def play(self, sak):
        """
        Play a turn in the game as a human player.

        Args:
            sak (SakClass): The sack of letters in the game.
        """
        word = input("Enter your word: ")
        if self.validate_word(word, sak):
            self.update_score(word)
            self.update_letters(word, sak)
        else:
            print("Invalid word. Try again.")

    def validate_word(self, word, sak):
        """
        Validate the entered word.

        Args:
            word (str): The word entered by the player.
            sak (SakClass): The sack of letters in the game.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        # Add logic to validate word based on game rules and available letters in the sack
        return True

    def update_score(self, word):
        """
        Update the player's score based on the played word.

        Args:
            word (str): The word played by the player.
        """
        # Add logic to calculate score based on word length, bonus tiles, etc.
        self.score += len(word)

    def update_letters(self, word, sak):
        """
        Update the player's letters based on the played word.

        Args:
            word (str): The word played by the player.
            sak (SakClass): The sack of letters in the game.
        """
        # Add logic to remove used letters from player's letters and replenish from the sack
        for letter in word:
            self.letters.remove(letter)
            sak.add_letter(letter)


class Computer(Player):
    """Class representing a computer player in the game."""

    def play(self, sak):
        """
        Play a turn in the game as a computer player.

        Args:
            sak (SakClass): The sack of letters in the game.
        """
        word = self.generate_word(sak)
        self.update_score(word)
        self.update_letters(word, sak)

    def generate_word(self, sak):
        """
        Generate a word to be played by the computer player.

        Args:
            sak (SakClass): The sack of letters in the game.

        Returns:
            str: The generated word.
        """
        # Add logic to generate word based on available letters and game strategy
        return ""

    def update_score(self, word):
        """
        Update the player's score based on the played word.

        Args:
            word (str): The word played by the player.
        """
        # Add logic to calculate score based on word length, bonus tiles, etc.
        self.score += len(word)

    def update_letters(self, word, sak):
        """
        Update the player's letters based on the played word.

        Args:
            word (str): The word played by the player.
            sak (SakClass): The sack of letters in the game.
        """
        # Add logic to remove used letters from player's letters and replenish from the sack
        for letter in word:
            self.letters.remove(letter)
            sak.add_letter(letter)


class Game:
    """Class representing the game itself."""

    def __init__(self, players):
        """
        Initialize the Game object.

        Args:
            players (list): List of Player objects participating in the game.
        """
        self.players = players
        self.score_board = {}
        self.dictionary = set()

    def setup(self):
        """Perform necessary actions to set up the game."""
        self.load_dictionary()

    def load_dictionary(self):
        """Load the dictionary of valid words from a file."""
        with open("dictionary.txt", "r") as file:
            for line in file:
                self.dictionary.add(line.strip())

    def run(self):
        """Execute the main loop of the game."""
        for player in self.players:
            self.score_board[player] = 0

        sak = SakClass(["A", "B", "C", "D", "E"])  # Example initial letters in the sack

        while not self.is_game_over():
            for player in self.players:
                print(f"Player {player.name}'s turn:")
                player.play(sak)

        self.end()

    def is_game_over(self):
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        # Add logic to check game-ending conditions, such as all players passing their turn
        return False

    def end(self):
        """Perform necessary actions to end the game."""
        # Add logic to display final scores, declare winner, save game statistics, etc.
        print("Game Over")
        print("Final Scores:")
        for player, score in self.score_board.items():
            print(f"{player.name}: {score}")
