import sys
import pygame
from scripts.settings import *
from scripts.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Making a screen
        self.level = Level(MAP_PATH) #Loads the map, walkability grid and markers
        pygame.display.set_caption("Grieving Angels") #Setting title for game
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = PLAYING #The game will start on MENU once the menu exists

        #Temporary debug camera
        self.offset_x = 0
        self.offset_y = 0

        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)) #Display 1/2 size of screen

    def handle_events(self): #The player's inputs will be recognised here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False #Exits loop if player quits the game

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Esc key switches between playing and paused game states
                    if self.state == PLAYING:
                        self.state = PAUSED
                    elif self.state == PAUSED:
                        self.state = PLAYING

                #Changing pixel offset for debug camera using user input
                if event.key == pygame.K_UP:
                    self.offset_y -= 40
                if event.key == pygame.K_DOWN:
                    self.offset_y += 40
                if event.key == pygame.K_RIGHT:
                    self.offset_x += 40
                if event.key == pygame.K_LEFT:
                    self.offset_x -= 40

    def update(self):
        if self.state == PLAYING:
            pass #The level, player and angel will be updated here

    def draw(self): #The level and entities will all be drawn here
        self.display.fill((0,0,0)) #Clears the display to black every frame
        self.level.render(self.display, self.offset_x, self.offset_y) #Draws the floor tiles onto the display
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0)) #Scales up and draws the display onto the screen
        pygame.display.update() #The screen is updated to display the frame

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw() #The screen is drawn at the very end
            self.clock.tick(FPS) #Makes the game run at 60FPS
        pygame.quit()
        sys.exit() #Ends program without any errors

if __name__ == "__main__":
    Game().run() #Running the run method from the Game class
