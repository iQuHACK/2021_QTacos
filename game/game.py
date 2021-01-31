import pygame as pg
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60
TIME_LIMIT = 6000

#Basic colors
BLACK   = (     0,  0,    0)
RED     = (   255,  0,    0)
BLUE    = (     0,  0,  255)

#Import resources
background = pg.image.load('resources/images/background.jpg')

plate = pg.image.load('resources/images/plate.png')

tortilla = pg.image.load('resources/images/tortilla.png')

deshebrada = pg.image.load('resources/images/deshebrada.png')
trompo = pg.image.load('resources/images/trompo.png')
pastor = pg.image.load('resources/images/pastor.png')
cilantro = pg.image.load('resources/images/cilantro.png')
cebolla = pg.image.load('resources/images/cebolla.png')
chicken = pg.image.load('resources/images/chicken.png')

tortilla_glow = pg.image.load('resources/images/tortilla_glow.png')
deshebrada_glow = pg.image.load('resources/images/deshebrada_glow.png')
trompo_glow = pg.image.load('resources/images/trompo_glow.png')
cilantro_glow = pg.image.load('resources/images/cilantro_glow.png')
cebolla_glow = pg.image.load('resources/images/cebolla_glow.png')
chicken_glow = pg.image.load('resources/images/chicken_glow.png')

paper = pg.image.load('resources/images/paper.png')
no_glow = pg.image.load('resources/images/no_glow.png')


#Text render method
def message_to_screen(screen,msg,color,position,size):
    font = pg.font.SysFont(None, size)
    text = font.render(msg,True,color)
    screen.blit(text,position)


class button():
    def __init__(self, image, effects, position, size, callback):
        self.image = image
        self.effects = effects
        self.position = position
        self.size = size
        self.callback = callback

        #Hitbox definition
        self.x = position[0] + (size[0] / 6)
        self.y = position[1] + (size[1] / 6)
        self.width = size[0]
        self.height = size[1]

        #Effects flag
        self.do_effects = False

    def draw(self,screen):
        #Call this method to draw the button on the screen
        screen.blit(self.image,self.position)
        if self.do_effects:
            screen.blit(self.effects, self.position)


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < (self.x + self.width):
            if pos[1] > self.y and pos[1] < (self.y + self.height):
                return True
        
        self.do_effects = False
        return False

    def hover_effects(self):
        self.do_effects = True
    
    """
    /////////////////////////////////////////////////////////////////////
    AQUÍ VAN LAS ACCIONES QUE REALIZA CADA BOTÓN

    FALTA IMPLEMENTAR LA 'SUMA' DE INGREDIENTES SOBRE LA TORTILLA
    """
    def do_action(self):
        print(self.callback)

    """
    /////////////////////////////////////////////////////////////////////

    """

class Game(object):
    def __init__(self):
        self.score = 0

        #List with every game element (buttons)
        self.button_list = []

        #Button init
        self.button_list.append(button(tortilla, tortilla_glow, (510,100),(180,180),'Tortilla1'))
        self.button_list.append(button(tortilla, tortilla_glow, (390,285),(180,180),'Tortilla2'))
        self.button_list.append(button(tortilla, tortilla_glow, (620,290),(180,180),'Tortilla3'))
        self.button_list.append(button(trompo, trompo_glow, (0,310),(200,280),'Trompo'))
        self.button_list.append(button(deshebrada, deshebrada_glow, (230,410),(150,150),'Deshebrada'))
        self.button_list.append(button(chicken, chicken_glow, (180,260),(140,140),'Chicken'))
        self.button_list.append(button(cilantro, cilantro_glow, (0,200),(155,80),'Cilantro'))
        self.button_list.append(button(cebolla, cebolla_glow, (180,130),(120,100),'Cebolla'))
        self.button_list.append(button(paper, deshebrada_glow, (10,-10),(250,120),'Paper'))


    def process_events(self):
        pos = pg.mouse.get_pos()

        for event in pg.event.get():
            #Quit game
            if event.type == pg.QUIT:
                return True
            
            #Click on screen
            #(Button implementation)
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in self.button_list:
                    if button.isOver(pos):
                        button.do_action()
            
            #Hover effects trigger
            if event.type == pg.MOUSEMOTION:
                for button in self.button_list:
                    if button.isOver(pos):
                        button.hover_effects()
                


        return False

        """
    /////////////////////////////////////////////////////////////////////
    AQUÍ VAN TODAS LAS FUNCIONES LOGICAS DEL JUEGO

    AQUÍ DEBE EJECUTARSE LA 'SUMA' DE INGREDIENTES
    """
    def run_logic(self):
        pass

    """
    /////////////////////////////////////////////////////////////////////

    """
    

    def display_frame(self, screen, time_bar_width):
        #Background elements
        screen.fill(BLACK)
        screen.blit(background,(0,0))
        screen.blit(plate,(370,90))

        #Display game elements
        for button in self.button_list:
            button.draw(screen)

        #Display Score
        score_msg = "Score: " + str(self.score)
        message_to_screen(screen,score_msg,BLUE,(710,40),60)

        #Display order
        order_msg = "|001>"
        message_to_screen(screen,order_msg,BLACK,(40,40),60)

        #Display timer bar
        pg.draw.rect(screen, RED,(0,0,time_bar_width,20))

        pg.display.flip()



def main():
    pg.init()

    screen = pg.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

    done = False
    clock = pg.time.Clock()
    timer = TIME_LIMIT
    time_bar_width = SCREEN_WIDTH
    time_bar_speed = SCREEN_WIDTH / TIME_LIMIT
    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic
        game.display_frame(screen, time_bar_width)
        clock.tick(FPS)
        timer -= 1
        time_bar_width -= time_bar_speed
        if timer <= 0:
            done = True
    pg.quit()


if __name__ == "__main__":
	main()