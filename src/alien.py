import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena na frota."""

    def __init__(self, ai_game):
        """Inicializa o alienígena e define sua posição inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('./assets/images/alienship.bmp')
        self.image = pygame.transform.scale(self.image, (39,30))
        self.rect = self.image.get_rect()
        # 79 60
        #  39,30
        # 26,20

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alienígena
        self.x = float(self.rect.x)

    def check_edges(self):
        """Devolve True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        # Se o alienígena estiver na borda direita ou esquerda
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move o alienígena para a direita ou para a esquerda."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
