class Settings:
    """Uma classe para armazenar todas as configurações do Alien Invasion."""
    
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255,255,255)


        #  Blue Sky 135 206 235
        # Azul escuro 10 10 40
        # Roxo escuro 20 0 40

        # Configurações da espaçonave
        self.ship_speed = 3.5

        # Configuções dos projéteis
        self.bullet_speed = 4.0
        self.bullet_width = 6
        self.bullet_height = 9
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1