import random
import itertools

class SakClass:
    """
    Κλάση που αναπαριστά το σακουλάκι με τα γράμματα.
    """
    def __init__(self):
        """
        Αρχικοποίηση του σακουλιού με γράμματα.
        """
        self.letters = self.randomize_sak()

    def randomize_sak(self):
        """
        Ανακατεύει τα γράμματα στο σακουλάκι.
        Επιστρέφει:
            λίστα: Ανακατεμένα γράμματα.
        """
        letters = list("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ" * 2)  # Παράδειγμα: κάθε γράμμα δύο φορές
        random.shuffle(letters)
        return letters

    def getletters(self, num=7):
        """
        Τραβάει γράμματα από το σακουλάκι.
        Παράμετροι:
            num (int): Ο αριθμός των γραμμάτων που θα τραβηχτούν.
        Επιστρέφει:
            λίστα: Τα γράμματα που τραβήχτηκαν.
        """
        if len(self.letters) < num:
            num = len(self.letters)
        drawn_letters = [self.letters.pop(random.randint(0, len(self.letters) - 1)) for _ in range(num)]
        return drawn_letters

    def putbackletters(self, letters):
        """
        Επιστρέφει γράμματα πίσω στο σακουλάκι.
        Παράμετροι:
            letters (λίστα): Τα γράμματα που θα επιστραφούν.
        """
        self.letters.extend(letters)
        random.shuffle(self.letters)

class Player:
    """
    Κλάση που αναπαριστά έναν παίκτη.
    """
    def __init__(self, name):
        """
        Αρχικοποίηση παίκτη.
        Παράμετροι:
            name (str): Το όνομα του παίκτη.
        """
        self.name = name
        self.score = 0
        self.letters = []

    def __repr__(self):
        """
        Αναπαράσταση του παίκτη ως συμβολοσειρά.
        Επιστρέφει:
            str: Αναπαράσταση του παίκτη.
        """
        return f"Player({self.name})"

    def change_letters(self, sak):
        """
        Αλλάζει τα γράμματα του παίκτη με νέα από το σακουλάκι.
        Παράμετροι:
            sak (SakClass): Το σακουλάκι με τα γράμματα.
        """
        sak.putbackletters(self.letters)
        self.letters = sak.getletters()

class Human(Player):
    """
    Κλάση που αναπαριστά έναν ανθρώπινο παίκτη.
    """
    def play(self):
        """
        Ζητάει από τον παίκτη να εισάγει μια λέξη, 'change' για αλλαγή γραμμάτων ή 'pass' για να παραλείψει τη σειρά του.
        Επιστρέφει:
            str: Η ενέργεια του παίκτη.
        """
        action = input("ΛΕΞΗ: ").strip().upper()
        return action

class Computer(Player):
    """
    Κλάση που αναπαριστά τον υπολογιστή ως παίκτη.
    """
    def play(self, valid_words):
        """
        Επιλέγει μια έγκυρη λέξη από τα διαθέσιμα γράμματα του υπολογιστή.
        Παράμετροι:
            valid_words (σύνολο): Το σύνολο των έγκυρων λέξεων.
        Επιστρέφει:
            str: Η λέξη που επιλέχθηκε ή 'change'/'pass' αν δεν υπάρχει έγκυρη λέξη.
        """
        for i in range(7, 1, -1):
            for perm in itertools.permutations(self.letters, i):
                word = "".join(perm)
                if word in valid_words:
                    return word
        return "CHANGE" if len(self.letters) > 1 else "PASS"

class Game:
    """
    Κλάση που αναπαριστά το παιχνίδι Scrabble.
    """
    def __init__(self):
        """
        Αρχικοποίηση του παιχνιδιού.
        """
        self.sak = SakClass()
        self.player = Human("Stavros")
        self.computer = Computer("PC")
        self.load_words()

    def load_words(self):
        """
        Φορτώνει τις έγκυρες λέξεις από το αρχείο 'greek7.txt'.
        """
        with open('greek7.txt', 'r', encoding='utf-8') as file:
            self.words = set(file.read().splitlines())

    def setup(self):
        """
        Ετοιμάζει το παιχνίδι και δίνει τα αρχικά γράμματα στους παίκτες.
        """
        self.player.letters = self.sak.getletters()
        self.computer.letters = self.sak.getletters()
        print(f"Starting letters for {self.player.name}: {self.player.letters}")
        print(f"Starting letters for {self.computer.name}: {self.computer.letters}")

    def calculate_score(self, word):
        """
        Υπολογίζει το σκορ μιας λέξης.
        Παράμετροι:
            word (str): Η λέξη της οποίας το σκορ υπολογίζεται.
        Επιστρέφει:
            int: Το σκορ της λέξης.
        """
        letter_scores = {
            'Α': 1, 'Β': 3, 'Γ': 2, 'Δ': 2, 'Ε': 1, 'Ζ': 4, 'Η': 4, 'Θ': 4,
            'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 3, 'Ν': 1, 'Ξ': 8, 'Ο': 1, 'Π': 3,
            'Ρ': 1, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3
        }
        return sum(letter_scores.get(letter, 0) for letter in word)

    def valid_word(self, word, player_letters):
        """
        Ελέγχει αν μια λέξη είναι έγκυρη και μπορεί να σχηματιστεί με τα διαθέσιμα γράμματα του παίκτη.
        Παράμετροι:
            word (str): Η λέξη που ελέγχεται.
            player_letters (λίστα): Τα διαθέσιμα γράμματα του παίκτη.
        Επιστρέφει:
            bool: Αν η λέξη είναι έγκυρη.
        """
        if word not in self.words:
            return False
        letters_copy = player_letters.copy()
        for char in word:
            if char in letters_copy:
                letters_copy.remove(char)
            else:
                return False
        return True

    def display_turn_info(self, player):
        """
        Εμφανίζει τις πληροφορίες για τη σειρά του παίκτη.
        Παράμετροι:
            player (Player): Ο παίκτης που παίζει τη σειρά του.
        """
        print("************************************************************")
        print(f"       *** Παίκτης: {player.name}     *** Σκορ: {player.score}")
        print(f"       >>> Γράμματα: {player.letters}")
        print("************************************************************")

    def player_turn(self, player):
        """
        Διαχειρίζεται τη σειρά ενός παίκτη.
        Παράμετροι:
            player (Player): Ο παίκτης που παίζει τη σειρά του.
        Επιστρέφει:
            bool: Αν ο παίκτης έπαιξε επιτυχώς μια λέξη.
        """
        self.display_turn_info(player)
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
                if player.name == "PC":
                    print(f"ΛΕΞΗ: {action}")
                print(f"Πόντοι Λέξης: {score}")
                for char in action:
                    player.letters.remove(char)
                player.letters.extend(self.sak.getletters(7 - len(player.letters)))
                self.display_turn_info(player)
                return True
            else:
                if player == self.player:
                    print("Invalid word. Try again.")
                else:
                    return False

    def run(self):
        """
        Εκτελεί τη ροή του παιχνιδιού.
        """
        pass_count = 0
        try:
            while self.sak.letters or any(self.player.letters) or any(self.computer.letters):
                if not self.player_turn(self.player):
                    pass_count += 1
                else:
                    pass_count = 0

                if pass_count >= 2:
                    break

                if not self.player_turn(self.computer):
                    pass_count += 1
                else:
                    pass_count = 0

                if pass_count >= 2:
                    break
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting gracefully...")

    def end(self):
        """
        Ανακοινώνει τη λήξη του παιχνιδιού και τους νικητές.
        """
        print("Game Over")
        print(f"Final Scores: {self.player.name} - {self.player.score}, {self.computer.name} - {self.computer.score}")
        if self.player.score > self.computer.score:
            print(f"The winner is {self.player.name}!")
        elif self.computer.score > self.player.score:
            print(f"The winner is {self.computer.name}!")
        else:
            print("It's a tie!")