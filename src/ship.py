import pygame

class Ship:
    """Uma classe para gerenciar a espaçonave."""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da espaçonave e obtém seu rect
        # self.image = pygame.image.load('./assets/images/ship.bmp')
        # self.rect = self.image.get_rect()
        self.image = pygame.image.load('./assets/images/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (37,50))  # Redimensiona para 60x60 pixels
        self.rect = self.image.get_rect()
        # 75 100
        #  37,50
        


        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.midbottom = self.screen_rect.midbottom
        
        #  Armazena um valor decimal para a posição horizontal da espaçonave
        self.x = float(self.rect.x)

        # Flag de movimento 
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Atualiza a posição da espaçonave com base na flag de movimento."""
        # Atualiza o valor da coordenada x da espaçonave, não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Atualiza o objeto rect a partir de self.x
        self.rect.x = self.x

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)