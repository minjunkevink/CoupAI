class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.coins = 0
class Game:
    def __init__(self, players):
        self.deck = [Card(role) for role in ["Duke", "Assassin", "Captain", "Ambassador", "Contessa"] * 3]
        self.players = [Player(name) for name in players]
        self.current_player_index = 0

    def shuffle_deck(self):
        # Randomly shuffle the deck
        pass

    def deal_cards(self):
        # Deal cards to each player
        pass

    def next_turn(self):
        # Advance to the next player's turn
        pass

    def play(self):
        # Main game loop
        pass

    # Other methods for game actions (income, coup, etc.) and checking game state
