import pygame as pg
import random


class Control:
    def __init__(self):
        self.resolutions = [(300,200), (600,400),(800, 600), (928, 696),(1080,720)]
        self.render_size = self.resolutions[-1] #largest
        self.screen = pg.display.set_mode(self.resolutions[-1], pg.RESIZABLE)
        self.screen_rect = self.screen.get_rect()
        self.render_surf = pg.Surface(self.render_size).convert()
 
        #pg.event.clear(pg.VIDEORESIZE)
        self.clock = pg.time.Clock()
        self.done = False
        self.fps = 60
         
        self.ball = Ball(self.screen_rect)
         
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.VIDEORESIZE:
                self.on_resize(event.size)
                #pg.event.clear(pg.VIDEORESIZE)
                 
    def on_resize(self, size):
        if size == self.screen_rect.size:
            return
        res_index = self.resolutions.index(self.screen_rect.size)
        adjust = 1 if size > self.screen_rect.size else -1
        if 0 <= res_index+adjust < len(self.resolutions):
            new_size = self.resolutions[res_index+adjust]
        else:
            new_size = self.screen_rect.size
        self.screen = pg.display.set_mode(new_size, pg.RESIZABLE)
        self.screen_rect.size = new_size
        self.set_scale()
 
    def set_scale(self):
        w_ratio = self.render_size[0]/float(self.screen_rect.w)
        h_ratio = self.render_size[1]/float(self.screen_rect.h)
        self.scale = (w_ratio, h_ratio)
                 
    def update(self):
        self.ball.update(self.render_surf.get_rect()) #give obj updated screen size
         
    def render(self):
        if self.render_size != self.screen_rect.size:
            scale_args = (self.render_surf, self.screen_rect.size, self.screen)
            pg.transform.smoothscale(*scale_args)
        else:
            self.screen.blit(self.render_surf, (0, 0))
        self.render_surf.fill((255,255,255))
        self.ball.draw(self.render_surf)
 
         
    def game_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.render()
            pg.display.update()
            self.clock.tick(self.fps)

class button():
    def __init__(self, color, x,y,width,height, text='', callback):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.callback = callback
    
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback
 
    def on_click(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback(self)

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pg.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

    
 

class Utilities:
	def colorize(image, newColor):
	    """
	    Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
	    original).
	    :param image: Surface to create a colorized copy of
	    :param newColor: RGB color to use (original alpha values are preserved)
	    :return: New colorized Surface instance
	    """
	    image = image.copy()
	 
	    # zero out RGB values
	    image.fill((0, 0, 0, 255), None, pg.BLEND_RGBA_MULT)
	    # add in new RGB values
	    image.fill(newColor[0:3] + (0,), None, pg.BLEND_RGBA_ADD)
	 
	    return image

    def image(image_name):
        return pygame.image.load(image_name)




class Main_game:
    #Import resources
    Background = image('bg.jpg')
    
    #Window init
    win = pg.display.set_mode((800,600))
    win.fill((0,0,0))
    win.blit(Background,(0,0))

    def game_loop(self):
        while not self.done:
            self.event_loop()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.VIDEORESIZE:
                self.on_resize(event.size)
                #pg.event.clear(pg.VIDEORESIZE)
    



pg.init()
app = Main_game:
app.game_loop()
pg.quit()

