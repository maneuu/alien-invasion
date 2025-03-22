import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Classe geral para gerenciar os recursos e o comportamento do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria os recursos do jogo."""
        pygame.init()
        
        # Cria o relógio para controlar a taxa de quadros
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Define o tamanho da tela
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Define a cor de fundo
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            # Verifica os eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # Sai do jogo quando a janela é fechada
            
            # Redesenha a tela a cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)

            # Atualiza a tela para mostrar o que foi desenhado
            pygame.display.flip()
            
            # Controla a taxa de quadros do jogo, limitando a 60 FPS
            self.clock.tick(60)

if __name__ == '__main__':
    # Cria uma instância do jogo e executa
    ai = AlienInvasion()
    ai.run_game()
