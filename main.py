from classes import Game

def main():
    """
    Κύρια συνάρτηση που εκτελεί το παιχνίδι Scrabble.
    """
    game = Game()
    game.setup()
    game.run()
    try:
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting gracefully...")
    finally:
        game.end()

if __name__ == "__main__":
    main()
