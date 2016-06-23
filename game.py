from Const import *
from Snake import *
from Apple import *
from Menu import *


class Top:
    def __init__(self,pygame,screen,snake,apple):
        self.pygame = pygame
        self.screen = screen
        self.snake = snake
        self.apple = apple
        self.state = 'menu'
        p1vsp2 = pygame.image.load('P1VSP2.png').convert()
        pvsc = pygame.image.load('NewGame.png').convert()
        quitPic = pygame.image.load('Quit.png').convert()

        self.menu = Menu(pygame,screen,SCREEN_WITH,SCREEN_HEIGHT,[pvsc,p1vsp2,quitPic],['pvsc','p1vsp2','quit'])

        direction = None
        self.apple_eaten = True
        self.score = 0

        self.t_start = time.time()
        self.best_s = 0
        self.text = pygame.font.Font(None,30)

    def Update(self,time_passed,key=None,pos=None):

        if self.state == 'menu':
            self.menu.ShowMenu()
            getM = self.menu.MouseDown(pos)
            if getM=='pvsc':
                self.state = 'gaming'
            elif getM == 'p1vsp2':
                pass
            elif getM == 'quit':
                self.pygame.quit()
                exit()

        elif self.state == 'gaming':
            if key == K_UP:
                direction = 0
            elif key == K_DOWN:
                direction = 1
            elif key == K_LEFT:
                direction = 2
            elif key == K_RIGHT:
                direction = 3
            else:
                direction = None
            d_t = time.time() - self.t_start
            (snake_dead, self.apple_eaten) = self.snake.ForJade(time_passed, self.apple.SetApple(self.apple_eaten), direction)

            if self.apple_eaten:
                self.score += 10

            self.screen.blit(self.text.render(str(self.score), 1, (255, 255, 255)), (0, 0))

            d_t = max(d_t, 1)
            tmp_s = int(100 * self.score / d_t)
            self.best_s = max(self.best_s, tmp_s)
            self.screen.blit(self.text.render(str(tmp_s), 1, (255, 255, 255)), (0, 20))
            self.screen.blit(self.text.render("best score : " + str(self.best_s), 1, (255, 255, 255)), (0, 40))

        elif self.state == 'over':
            pass
        else:
            print "error in Top Update"




pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT), 0, 32) 
pygame.display.set_caption("Snake!")
applePic = pygame.image.load('apple.png').convert_alpha()

snake_zhs = Snake(pygame,screen)
apple_public = Apple(pygame,screen,applePic)
top = Top(pygame,screen,snake_zhs,apple_public)

clock = pygame.time.Clock()

t0 = clock.tick()

while True:
    screen.fill((0,0,0))
    key = None
    mousePos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            key = event.key
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()

    top.Update(clock.tick(30),key,mousePos)

    pygame.display.update()
    
