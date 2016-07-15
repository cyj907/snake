from State import State
from Menu import *
from Direction import Direction
from AI2 import AI2
from Astar import AStar
from AIDFS import AIDFS
from AIBDFS import AIBDFS
from RL import QState
import os

class Game:

    def __init__(self, pygame):
        self.pygame = pygame
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT), 0, 32)
        self.pygame.display.set_caption("Snake!")
        self.applePic = self.pygame.image.load(os.path.join('graph', 'apple.png')).convert()
        self.applePic = self.pygame.transform.scale(self.applePic, (APPLE_WIDTH, APPLE_HEIGHT))
        self.state = State()
        self.clock = pygame.time.Clock()

        t0 = self.clock.tick()
        self.gameOption = 'menu'
        self.direction = None
        dirpath = 'graph'
        p1vsp2 = pygame.image.load(os.path.join(dirpath,'P1VSP2.png')).convert()
        pvsc = pygame.image.load(os.path.join(dirpath, 'NewGame.png')).convert()
        quitPic = pygame.image.load(os.path.join(dirpath, 'Quit.png')).convert()
        cpPic = pygame.image.load(os.path.join(dirpath, 'CP.png')).convert()

        self.menu = Menu(self.pygame, self.screen,
                         SCREEN_WITH, SCREEN_HEIGHT,
                         [pvsc, cpPic, p1vsp2, quitPic],
                         ['pvsc', 'cp', 'p1vsp2', 'quit'])

        self.apple_eaten = False
        self.score = 0

        self.t_start = time.time()
        self.best_s = 0
        self.text = pygame.font.Font(None,30)

        #self.ai1=AI1(snake,apple)
        #self.ai = AI2()
        #self.ai = AIDFS()
        self.ai = AIBDFS()
        self.qfunc = QState.QFunc()

    def Update(self,key=None,pos=None):
        if self.gameOption == 'menu':
            self.menu.ShowMenu()
            getM = self.menu.MouseDown(pos)
            if getM=='pvsc':
                self.gameOption = 'gaming'
                self.state.ResetSnake()
            elif getM=='cp':
                self.gameOption = 'cp'
            elif getM == 'p1vsp2':
                self.gameOption = 'p1vsp2'
                self.qfunc.LoadFile("qvalue.txt")
            elif getM == 'quit':
                self.pygame.quit()
                exit()
        elif self.gameOption == 'gaming':
            if key == K_UP:
                direction = Direction.North
            elif key == K_DOWN:
                direction = Direction.South
            elif key == K_LEFT:
                direction = Direction.West
            elif key == K_RIGHT:
                direction = Direction.East
            else:
                direction = Direction.Stop

            self._DisplayScore()
            self._DisplayState(self.state)

            nextState = self.state.GetNextState(direction)
            snake_dead = nextState.snake.IsDead()
            apple_eaten = nextState.IsAppleEaten()

            print "============================"
            print nextState.snake.GetBodyRects()
            print nextState.snake.rects
            print nextState.snake.body
            print nextState.snake.GetBodyRects2()
            if snake_dead:
                self.gameOption = 'over'
            if apple_eaten:
                self.score += 10
                nextState.IncreaseMovSpeed()
                nextState.GenNewApple()
                nextState.AddSnakeLen()

            self.state = nextState
        elif self.gameOption == 'cp':
            nextDirection = self.ai.GetDirection(self.state)
            nextState = self.state.GetNextState(nextDirection)
            snake_dead = nextState.snake.IsDead()
            apple_eaten = nextState.IsAppleEaten()

            if snake_dead:
                self.gameOption = 'over'
                print self.ai.directions
                print nextState.eatenAppleCount , " eaten"
                print nextDirection
            if apple_eaten:
                self.score += 1
                nextState.IncreaseMovSpeed()
                nextState.GenNewApple()
                nextState.AddSnakeLen()

            self._DisplayScore()
            self._DisplayState(nextState)
            self.state = nextState
        elif self.gameOption == 'p1vsp2':
            nextDirection = self.qfunc.GetBestDir(self.state)
            nextState = self.qfunc.UpdateQValue(self.state,nextDirection)
            if nextState == None:
                print self.state.eatenAppleCount, " eaten"
                print nextDirection
                self.score = 0
                self.state = State()
                return

            apple_eaten = nextState.IsAppleEaten()
            if apple_eaten:
                self.score += 1
                #nextState.IncreaseMovSpeed()
                nextState.GenNewApple()
                #nextState.AddSnakeLen()

            """
            snake_dead = nextState.snake.IsDead()
            apple_eaten = nextState.IsAppleEaten()

            print nextDirection
            if snake_dead:
                self.gameOption = 'over'
                print nextState.eatenAppleCount, " eaten"
                print nextDirection

            if apple_eaten:
                self.score += 1
                #nextState.IncreaseMovSpeed()
                nextState.GenNewApple()
                #nextState.AddSnakeLen()
            """
            self._DisplayScore()
            self._DisplayState(nextState)
            self.state = nextState
        elif self.gameOption == 'over':
            # self._GameOver()
            self._DisplayState(self.state)
            self.gameOption = 'over'
        else:
            print "error in Top Update"


    def Run(self):
        while True:
            try:
                self.screen.fill((0,0,0))
                key = None
                mousePos = None
                for event in self.pygame.event.get():
                    if event.type == self.pygame.QUIT:
                        self.pygame.quit()
                        exit()
                    elif event.type == KEYDOWN:
                        key = event.key
                    elif event.type == self.pygame.MOUSEBUTTONDOWN:
                        mousePos = self.pygame.mouse.get_pos()

                self.clock.tick(50)
                self.Update(key, mousePos)
                self.pygame.display.update()
            except KeyboardInterrupt:
                self.qfunc.Save2File("qvalue.txt")
                break

    def _DisplayScore(self):
        d_t = max(time.time() - self.t_start, 1)
        tmp_s = int(100 * self.score / d_t)
        self.best_s = max(self.best_s, tmp_s)
        self.screen.blit(self.text.render(str(tmp_s), 1, (255, 255, 255)), (0, 20))
        self.screen.blit(self.text.render("best score : " + str(self.best_s), 1, (255, 255, 255)), (0, 40))
        self.screen.blit(self.text.render(str(self.score), 1, (255, 255, 255)), (0, 0))

    def _DisplayState(self, state):
        # Draw Snake Body
        SnakeRects = state.snake.GetBodyRects()
        for i in range(len(SnakeRects)):
            x1, y1, x2, y2 = SnakeRects[i]
            rect = (x1, y1, x2 - x1 + 1, y2 - y1 + 1)
            SnakeRects[i] = rect

        for rect in SnakeRects:
            self.pygame.draw.rect(self.screen, SNAKE_COLOR, rect)

        # Draw Apple
        ApplePos = state.apple.GetApplePos()
        self.screen.blit(self.applePic, ApplePos)

    # show game over animation using sprite technique
    def _GameOver(self):
        try:
            # load image and scale to fit screen size
            spritesheet = self.pygame.image.load(os.path.join('graph', 'gameover.png')).convert()
            spritesheet = self.pygame.transform.scale(spritesheet, (SCREEN_WITH * 24, SCREEN_HEIGHT))
        except:
            raise(UserWarning, "Unable to load sprite image file")

        t = 100
        for i in range(24):
            subImage = spritesheet.subsurface(SCREEN_WITH*i,0,SCREEN_WITH,SCREEN_HEIGHT)

            self.screen.blit(subImage, (0,0))
            self.pygame.time.delay(t)
            self.pygame.display.update()

snakeGame = Game(pygame)
snakeGame.Run()
