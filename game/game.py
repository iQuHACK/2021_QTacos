import pygame as pg
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BLACK = (0,0,0)
fps = 60

#Import resources
background = pg.image.load('background.jpg')

class button():
    """
    def __init__(self, color, x,y,width,height, text='', callback):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.callback = callback
    """
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback
 
    def on_click(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback(self)

class Game(object):
    def __init__(self):
        self.score = 0

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True
        return False

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(BLACK)
        screen.blit(background,(0,0))
        pg.display.flip()

def main():
    pg.init()

    screen = pg.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

    done = False
    clock = pg.time.Clock()
    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic
        game.display_frame(screen)
        clock.tick(fps)
    pg.quit()


if __name__ == "__main__":
	main()