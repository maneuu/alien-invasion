import pygame.font 

class Scoreboard:
    """Uma classe para mostrar informações sobre o jogo."""

    def __init__(self, ai_game):
        """Inicializa os atributos de pontuação."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Configura a fonte para mostrar a pontuação.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuação inicial.
        self.prep_score()
        # Prepara a imagem da pontuação mais alta.
        self.prep_high_score()

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