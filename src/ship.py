import pygame

class Ship:
    """Uma classe para gerenciar a espaçonave."""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('./assets/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)