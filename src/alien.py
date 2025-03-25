import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena na frota."""

    def __init__(self, ai_game):
        """Inicializa o alienígena e define sua posição inicial."""
        super().__init__()
        self.screen = ai_game.screen

        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('./assets/images/alienship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alienígena
        self.x = float(self.rect.x)
