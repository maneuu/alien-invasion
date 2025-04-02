import pygame.font 
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """Uma classe para mostrar informações sobre o jogo."""

    def __init__(self, ai_game):
        """Inicializa os atributos de pontuação."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Configura a fonte para mostrar a pontuação.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 38)

        # Prepara a imagem da pontuação inicial.
        self.prep_score()
        # Prepara a imagem da pontuação mais alta.
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada."""
        # Arredonda a pontuação para o múltiplo de 10 mais próximo.
        # Isso é feito para evitar que a pontuação fique muito longa.
        # Por exemplo, 1234 se torna 1230.
        # Isso ajuda a manter a pontuação mais legível.
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}".replace(",", ".")
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Exibe a pontuação na parte superior da tela.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        # Desenha a pontuação mais alta na tela.
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # Desenha o nível na tela.
        self.screen.blit(self.level_image, self.level_rect)
        # Desenha as naves restantes na tela.
        self.ships.draw(self.screen)
    
    def prep_high_score(self):
        """Transforma a pontuação mais alta em uma imagem renderizada."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {high_score:,}".replace(",", ".")
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Centraliza a pontuação mais alta na parte superior da tela.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20
    
    def check_high_score(self):
        """Verifica se há uma nova pontuação mais alta."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_ships(self):
        """Mostra quantas naves restam."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * (ship.rect.width + 10)
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """Transforma o nível atual em uma imagem renderizada."""
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Coloca o nível abaixo da pontuação.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10