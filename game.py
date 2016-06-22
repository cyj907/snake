from Const import *
from Snake import *







pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT), 0, 32) 
pygame.display.set_caption("Snake!")





clock = pygame.time.Clock()
t0 = clock.tick()


snake_zhs = Snake(pygame,screen)

direction =None
applePos=None

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            key = event.key
            if key == K_UP :
                direction=0
            elif key == K_DOWN:
                direction=1
            elif key == K_LEFT:
                direction=2
            elif key == K_RIGHT :
                direction=3
            else:
                direction =None
            
    time_passed = clock.tick(30)
    snake_zhs.ForJade(time_passed,applePos,direction)
    pygame.display.update()
    
