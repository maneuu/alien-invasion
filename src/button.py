import pygame.font

class Button:
    """Classe para criar um botão, para o jogo."""

    def __init__(self, ai_game, msg):
        """Inicializa os atributos do botão."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Define as dimensões e propriedades do botão
        self.width, self.height = 200, 50
        self.button_color = (38, 38, 38)  # Preto
        self.text_color = (255, 255, 255)  # Branco
        self.font = pygame.font.SysFont(None, 48)

        # Cria o retângulo do botão e centraliza-o na tela
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão deve ser preparada apenas uma vez
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Converte a mensagem em uma imagem renderizada e centraliza o texto no botão."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Desenha o botão e exibe a mensagem."""
        # Desenha o botão
        self.screen.fill(self.button_color, self.rect)
        # Desenha a mensagem no botão
        self.screen.blit(self.msg_image, self.msg_image_rect)