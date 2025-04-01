class GameStats:
    """Rastrear estatísticas para Alien Invasion."""

    def __init__(self, ai_game):
        """Inicializa as estatísticas."""
        
        self.settings = ai_game.settings
        self.reset_stats()

        # Inicia o Alien Invasion em um estado ativo
        self.game_active = False

        
        # Pontuação mais alta deve nunca ser reiniciada
        self.high_score = 0
        # Pontuação atual deve ser reiniciada
        self.score = 0

    def reset_stats(self):
        """Inicializa as estatísticas que podem mudar durante o jogo."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
