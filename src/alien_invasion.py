import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        
        """ 
        //=================== Para rodar em tela cheia ===================\\
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        """

        pygame.display.set_caption("Alien Invasion")
        # Cria uma espaçonave
        self.ship = Ship(self)
        # Cria um grupo no qual serão armazenados os projéteis
        self.bullets = pygame.sprite.Group()
        # Cria um grupo de alienígenas
        self.alien = pygame.sprite.Group()

        self._create_fleet()
        
        
    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            self._check_events() # Verifica eventos
            self.ship.update() # Atualiza a posição da espaçonave
            # Atualiza a posição dos projéteis e se livra dos projéteis antigos
            self._update_bullets()
            self._update_screen() # Atualiza a tela
            self.clock.tick(60)  # Controla a taxa de quadros do jogo, limitando a 60 FPS


    def _check_events(self):
        """Responde a eventos de pressionamento de teclas e de mouse."""
        # Verifica os eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Sai do jogo quando a janela é fechada
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            

    def _check_keydown_events(self, event):
        """Responde a pressionamentos de tecla."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
                sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a solturas de tecla."""
        if event.key == pygame.K_RIGHT:
          self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
          self.ship.moving_left = False

    def _fire_bullet(self):
        """Cria um novo projétil e o adiciona ao grupo de projéteis."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
        # Atualiza a posição dos projéteis
        self.bullets.update()
        # Livra-se dos projéteis que desapareceram
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Cria a frota de alienígenas."""
        # Cria um alienígena
        alien = Alien(self)
        self.alien.add(alien)   

    def _update_screen(self):
        """Atualiza as imagens na tela e alterna para a nova tela."""
        # Redesenha a tela a cada passagem pelo loop
        self.screen.fill(self.settings.bg_color) 
        # Desenha todos os projéteis atrás da espaçonave e dos alienígenas
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme() # Desenha a espaçonave na tela
        self.alien.draw(self.screen) # Desenha o alienígena
        pygame.display.flip() # Atualiza a tela para mostrar o que foi desenhado


if __name__ == '__main__':
    # Cria uma instância do jogo e executa
    ai = AlienInvasion()
    ai.run_game()
