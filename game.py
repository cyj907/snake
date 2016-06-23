from Const import *
from Snake import *
from Apple import *







pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT), 0, 32) 
pygame.display.set_caption("Snake!")


snake_zhs = Snake(pygame,screen)
apple_public = Apple(pygame,screen)
test = pygame.font.Font(None,30)
clock = pygame.time.Clock()

t0 = clock.tick()
direction =None
apple_eaten = True
score = 0

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
    (snake_dead,apple_eaten)=snake_zhs.ForJade(time_passed,apple_public.SetApple(apple_eaten),direction)
    if apple_eaten:
        score+=10
    screen.blit(test.render(str(score),1,(255,255,255)), (0, 0))
    pygame.display.update()
    
