import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

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
        
        # Cria uma instância para armazenar estatísticas do jogo
        self.stats = GameStats(self)
        # Cria uma instância para armazenar as estatísticas do jogo

        self.sb = Scoreboard(self)
     
        # Cria uma espaçonave
        self.ship = Ship(self)
        # Cria um grupo no qual serão armazenados os projéteis
        self.bullets = pygame.sprite.Group()
        # Cria um grupo de alienígenas
        self.alien = pygame.sprite.Group()

        self._create_fleet()
        # Começa o jogo no estado ativo.
        self.game_active = False
        
        # Cria o botão Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            self._check_events() # Verifica eventos
            if self.game_active:
                self.ship.update() # Atualiza a posição da espaçonave
                # Atualiza a posição dos projéteis e se livra dos projéteis antigos
                self._update_bullets()
                # Atualiza a posição dos alienígenas
                self._update_aliens()
            self._update_screen() # Atualiza a tela
            self.clock.tick(60)  # Controla a taxa de quadros do jogo, limitando a 60 FPS


    def _check_events(self):
        """Responde a eventos de pressionamento de teclas e de mouse."""
        # Verifica os eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Sai do jogo quando a janela é fechada
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_play_button(self, mouse_pos):
        """Verifica se o botão Play foi clicado."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()  # Inicia um novo jogo
            self.stats.reset_stats()  # Reinicia as estatísticas do jogo
            self.sb.prep_score()  # Prepara a pontuação para ser exibida

            self.sb.prep_level()  # Prepara o nível para ser exibido
            self.sb.prep_ships()  # Prepara as naves restantes para serem exibidas
        
    def _start_game(self):
        """Inicia um novo jogo."""
        # Reinicia as estatísticas do jogo
        self.stats.reset_stats()
        self.game_active = True

        # Esvazia a lista de alienígenas e de projéteis
        self.alien.empty()
        self.bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        self._create_fleet()
        self.ship.center_ship()

        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

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
        elif event.key == pygame.K_p: # Inicia o jogo quando a tecla P é pressionada
            if not self.game_active:
                self._start_game()

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
        
        # Verifica colisões entre projéteis e alienígenas
        self._check_bullet_alien_collisions()
        
    
    def _check_bullet_alien_collisions(self):
        """Responde a colisões entre projéteis e alienígenas."""
        # Remove qualquer projétil e alienígena que tenham colidido
        collisions = pygame.sprite.groupcollide(self.bullets, self.alien, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
                
        if not self.alien:
            # Destroi os projéteis existentes e cria uma nova frota
            self.bullets.empty()
            self._create_fleet()
            # Aumenta a velocidade do jogo
            self.settings.increase_speed()

            # Aumenta o nível
            self.stats.level += 1
            self.sb.prep_level()  # Prepara o nível para ser exibido

    def _check_aliens_bottom(self):
        """Verifica se algum alienígena alcançou a parte inferior da tela."""
        for alien in self.alien.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Trata esse caso da mesma forma que é feita quando a espaçonave é atingida
                self._ship_hit()  
                break  

    def _update_aliens(self):
        """Verifica se a frota está em uma borda e então atualiza as posições de todos os alienígenas na frota."""
        self._check_fleet_edges()
        self.alien.update()

        # Verifica colisões entre alienígenas e a espaçonave
        if pygame.sprite.spritecollideany(self.ship, self.alien):
            # print("A espaçonave foi atingida!")
            self._ship_hit()
        
        # Verifica se algum alienígena atingiu a parte inferior da tela
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Responde ao fato de a espaçonave ter sido atingida por um alienígena."""
        # Decrementa ships_left
        if self.stats.ships_left > 0:
            # Decrementa ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Esvazia a lista de alienígenas e de projéteis
            self.alien.empty()
            self.bullets.empty()
            # Cria uma nova frota e centraliza a espaçonave
            self._create_fleet()
            self.ship.center_ship()
            # Faz uma pausa
            sleep(1.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)  # Mostra o cursor do mouse
    
            
    def _create_fleet(self):
        """Cria a frota de alienígenas."""
        # Cria um alienígena e continua adicionando alienígenas até que a frota alcance o limite
        # Espaço entre cada alienígena é igual à largura de um alienígena
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):    
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Termina a linha; reseta a posição x e incrementa a posição y
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        """Cria um alienígena e o posiciona na frota."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.alien.add(new_alien)
    
    def _check_fleet_edges(self):
        """Responde apropriadamente se algum alienígena alcançou uma borda."""
        for alien in self.alien.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """Faz toda a frota descer e muda a direção da frota."""
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Atualiza as imagens na tela e alterna para a nova tela."""
        # Redesenha a tela a cada passagem pelo loop
        self.screen.fill(self.settings.bg_color) 
        # Desenha todos os projéteis atrás da espaçonave e dos alienígenas
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme() # Desenha a espaçonave na tela
        self.alien.draw(self.screen) # Desenha o alienígena
        # Desenha a pontuação na tela
        self.sb.show_score()

        # Desenha o botão Play se o jogo não estiver ativo
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip() # Atualiza a tela para mostrar o que foi desenhado


if __name__ == '__main__':
    # Cria uma instância do jogo e executa
    ai = AlienInvasion()
    ai.run_game()
