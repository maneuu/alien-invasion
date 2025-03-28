class GameStats:
    """Rastrear estatísticas para Alien Invasion."""

    def __init__(self, ai_game):
        """Inicializa as estatísticas."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Inicia o Alien Invasion em um estado ativo
        self.game_active = False

        # Pontuação máxima
        self.high_score = 0

    def reset_stats(self):
        """Inicializa as estatísticas que podem mudar durante o jogo."""
        self.ships_left = self.settings.ship_limit
