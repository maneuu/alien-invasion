class Settings:
    """Uma classe para armazenar todas as configurações do Alien Invasion."""
    
    def __init__(self):
        """ Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        # Configurações da espaçonave
        self.ship_limit = 3
        # Configurações do projétil
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Configurações dos alienígenas
        self.fleet_drop_speed = 10
        # o quão rápido o jogo aumenta a dificuldade
        self.speedup_scale = 1.3
        # o quão rápido a pontuação aumenta
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam durante o jogo."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        
        # fleet_direction = 1 representa direita; -1 representa esquerda
        self.fleet_direction = 1

        # Pontuação
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta as configurações de velocidade e pontuação."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
