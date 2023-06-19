from classes import Human, Computer, Game

# Create players
human_player = Human("Stavros")
computer_player = Computer("PC")

# Add players to the game
players = [human_player, computer_player]

# Create and setup the game
game = Game(players)
game.setup()

# Run the game
game.run()
