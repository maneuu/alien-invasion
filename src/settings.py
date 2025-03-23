class Settings:
    """Uma classe para armazenar todas as configurações do Alien Invasion."""
    
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (20 ,0 ,40) 

        #  Blue Sky 135 206 235
        # Azul escuro 10 10 40
        # Roxo escuro 20 0 40

        # Configurações da espaçonave
        self.ship_speed = 1.5