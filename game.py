from Const import *
from Snake import *
from Apple import *
import os
from Menu import *
from AI1 import *

# show game over animation using sprite technique
def GameOver(scrn):
    try:
        # load image and scale to fit screen size
        spritesheet = pygame.image.load(os.path.join('graph', 'gameover.png')).convert()
        spritesheet = pygame.transform.scale(spritesheet, (SCREEN_WITH * 24, SCREEN_HEIGHT))
    except:
        raise(UserWarning, "Unable to load sprite image file")

    t = 100
    for i in range(24):
        subImage = spritesheet.subsurface(SCREEN_WITH*i,0,SCREEN_WITH,SCREEN_HEIGHT)
        scrn.blit(subImage, (0,0))
        pygame.time.delay(t)
        pygame.display.update()

def IsValidApple(apple, snake):
    appleRect = apple.getRect()
    print appleRect
    snakeRects = snake.getRects()
    for rect in snakeRects:
        if RectIntersect(appleRect, rect):
            return False
    return True

class Top:
    def __init__(self,pygame,screen,snake,apple):
        self.pygame = pygame
        self.screen = screen
        self.snake = snake
        self.apple = apple
        self.state = 'menu'
        self.direction = None
        dirpath = 'graph'
        p1vsp2 = pygame.image.load(os.path.join(dirpath,'P1VSP2.png')).convert()
        pvsc = pygame.image.load(os.path.join(dirpath, 'NewGame.png')).convert()
        quitPic = pygame.image.load(os.path.join(dirpath, 'Quit.png')).convert()
        cpPic = pygame.image.load(os.path.join(dirpath, 'CP.png')).convert()

        self.menu = Menu(pygame,screen,SCREEN_WITH,SCREEN_HEIGHT,[pvsc,cpPic,p1vsp2,quitPic],['pvsc','cp','p1vsp2','quit'])

        self.apple_eaten = False
        self.score = 0

        self.t_start = time.time()
        self.best_s = 0
        self.text = pygame.font.Font(None,30)

        self.ai1=AI1(snake,apple)

    def Update(self,time_passed,key=None,pos=None):
        if self.state == 'menu':
            self.menu.ShowMenu()
            getM = self.menu.MouseDown(pos)
            if getM=='pvsc':
                self.state = 'gaming'
                self.snake.Reset()
            elif getM=='cp':
                self.state ='cp'
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

            if self.apple_eaten:
                self.apple.SetApple()
                while not IsValidApple(self.apple, self.snake):
                    self.apple.SetApple()
            self.apple.ShowApple()

            (snake_dead, self.apple_eaten) = self.snake.ForJade(time_passed, self.apple.GetApplePos(), direction)

            if snake_dead:
                self.state = 'over'

            if self.apple_eaten:
                self.score += 10
            self.screen.blit(self.text.render(str(self.score), 1, (255, 255, 255)), (0, 0))
            d_t = max(d_t, 1)
            tmp_s = int(100 * self.score / d_t)
            self.best_s = max(self.best_s, tmp_s)
            self.screen.blit(self.text.render(str(tmp_s), 1, (255, 255, 255)), (0, 20))
            self.screen.blit(self.text.render("best score : " + str(self.best_s), 1, (255, 255, 255)), (0, 40))
        elif self.state == 'cp':
            direction = self.ai1.GetDirection(time_passed)

            if self.apple_eaten:
                self.apple.SetApple()
                while not IsValidApple(self.apple, self.snake):
                    self.apple.SetApple()
            self.apple.ShowApple()

            (snake_dead, self.apple_eaten) = self.snake.ForJade(time_passed, self.apple.GetApplePos(), direction)
            #print direction,snake_dead
            print '========================='
            if snake_dead:
                self.state = 'over'
        elif self.state == 'over':
            # GameOver(screen)
            self.apple.ShowApple()
            self.snake.ForJade()
            self.state = 'over'
        else:
            print "error in Top Update"



pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT), 0, 32) 
pygame.display.set_caption("Snake!")
applePic = pygame.image.load(os.path.join('graph', 'apple.png')).convert()

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


