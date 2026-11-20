import sys
import pygame
from scripts.settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #making a screen
        pygame.display.set_caption("Grieving Angels") #setting title for game
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = PLAYING #The game will start on MENU once the menu exists

    def handle_events(self): #the player's inputs will be recognised here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False #exits loop if player quits the game

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Esc key switches between playing and paused game states
                    if self.state == PLAYING:
                        self.state = PAUSED
                    elif self.state == PAUSED:
                        self.state = PLAYING

    def update(self):
        if self.state == PLAYING:
            pass #the level, player and angel will be updated here

    def draw(self): #The level and entities will all be drawn here
        self.screen.fill((0,0,0)) #the screen is initially black
        pygame.display.update() #the screen is updated to display the frame

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw() #the screen is drawn at the very end
            self.clock.tick(FPS) #makes the game run at 60FPS
        pygame.quit()
        sys.exit() #ends program without any errors

if __name__ == "__main__":
    Game().run() #running the run method from the Game class