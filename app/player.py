class Player:
    def __init__(self, symbol, name=None):
        self.symbol = symbol
        self.name = name or symbol
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def record_win(self):
        self.wins += 1

    def record_loss(self):
        self.losses += 1

    def record_draw(self):
        self.draws += 1
