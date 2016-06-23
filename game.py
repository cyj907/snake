from Const import *
from Snake import *
from Apple import *
import os

# show game over animation using sprite technique
def GameOver(scrn):
    try:
        # load image and scale to fit screen size
        spritesheet = pygame.image.load(os.path.join('graph', 'gameover.png')).convert()
        spritesheet = pygame.transform.scale(spritesheet, (SCREEN_WITH * 24, SCREEN_HEIGHT))
    except:
        raise(UserWarning, "Unable to load sprite image file")

    FPS = 100
    for i in range(24):
        subImage = spritesheet.subsurface(SCREEN_WITH*i,0,SCREEN_WITH,SCREEN_HEIGHT)
        scrn.blit(subImage, (0,0))
        pygame.time.delay(FPS)
        pygame.display.update()





pygame.init()
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT), 0, 32) 
pygame.display.set_caption("Snake!")
applePic = pygame.image.load(os.path.join('graph', 'apple.png')).convert()


snake_zhs = Snake(pygame,screen)
apple_public = Apple(pygame,screen,applePic)
test = pygame.font.Font(None,30)
clock = pygame.time.Clock()

t0 = clock.tick()
direction =None
apple_eaten = True
score = 0

t_start = time.time()
best_s = 0

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
    d_t=time.time()-t_start
    time_passed = clock.tick(30)
    (snake_dead,apple_eaten)=snake_zhs.ForJade(time_passed,apple_public.SetApple(apple_eaten),direction)

    if snake_dead:
        GameOver(screen)
        break

    if apple_eaten:
        score+=10
    screen.blit(test.render(str(score),1,(255,255,255)), (0, 0))

    d_t=max(d_t,1)
    tmp_s=int(100*score/d_t)
    best_s=max(best_s,tmp_s)
    screen.blit(test.render(str(tmp_s),1,(255,255,255)), (0, 20))
    screen.blit(test.render("best score : "+str(best_s),1,(255,255,255)), (0, 40))
    pygame.display.update()
    
