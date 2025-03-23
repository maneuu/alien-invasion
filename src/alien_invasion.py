import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar os recursos e o comportamento do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria os recursos do jogo."""
        pygame.init()
        
        # Cria o relógio para controlar a taxa de quadros
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Define o tamanho da tela
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Cria uma espaçonave
        self.ship = Ship(self)

        
        
    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            # Verifica eventos
            self._check_events()
            # Atualiza a posição da espaçonave
            self.ship.update()
            # Atualiza a tela
            self._update_screen()
            # Controla a taxa de quadros do jogo, limitando a 60 FPS
            self.clock.tick(60)

    def _check_events(self):
        """Responde a eventos de pressionamento de teclas e de mouse."""
        # Verifica os eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Sai do jogo quando a janela é fechada
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move a espaçonave para a direita
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move a espaçonave para a esquerda
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Para o movimento da espaçonave
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    # Para o movimento da espaçonave
                    self.ship.moving_left = False

    def _update_screen(self):
        """Atualiza as imagens na tela e alterna para a nova tela."""
        # Redesenha a tela a cada passagem pelo loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() # Desenha a espaçonave na tela
        # Atualiza a tela para mostrar o que foi desenhado
        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e executa
    ai = AlienInvasion()
    ai.run_game()
