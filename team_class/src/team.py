class Team:

    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self._points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_added):
        return self.players.count(player_added) > 0

    def get_points(self):
        return self._points

    def play_game(self, game_won):
        if game_won:
            self._points += 3