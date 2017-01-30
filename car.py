import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
car_width = 53

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Cross The Street')
clock = pygame.time.Clock()
Carimg = pygame.image.load('Car.png')
def score_count(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE: "+str(count),True, red)
    gameDisplay.blit(text,(0,0))
def Car(x,y):
    gameDisplay.blit(Carimg,(x,y))

def blocks(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh])



def crash():
    message_display('Crash')
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

    def things(thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh])
    

    
def game_loop():
    x = display_width*0.45
    y = display_height*0.8
    x_change = 0
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    score = 0
    crashed = False    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -100
                elif event.key == pygame.K_RIGHT:
                    x_change = 100
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
            x+=x_change
        gameDisplay.fill(white)
        blocks(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        Car(x,y)
        score_count(score)
        
        if x>(display_width-car_width) or x<0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0-thing_height
            thing_startx = random.randrange(0, display_width)
            score+=1
            thing_speed += 1
            thing_width += (score+1.2)
        if y < thing_starty+thing_height:
            #log message
            print('past y')
            if x > thing_startx and x < thing_startx + thing_width or x+car_width> thing_startx and x+car_width<thing_startx+thing_width:
                #log message
                print('past x')
                crash()

        
        
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
