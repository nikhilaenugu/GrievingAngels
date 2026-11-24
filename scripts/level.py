import json
import pygame
from scripts.settings import *


class Level:
    def __init__(self, path):
        self.tile_img = pygame.image.load(FLOOR_IMG_PATH).convert_alpha() #Loaded at start-up

        with open(path) as file:
            data = json.load(file) #Reading map.json into a dictionary

        self.map_width = data["mapWidth"] #How many tiles wide the map is
        self.map_height = data["mapHeight"] #How many tiles tall the map is

        self.walkable_tiles = [] #A 2D list where walkable tiles are True
        for row in range(self.map_height):
            new_row = [] #A new separate list for every row of the grid
            for col in range(self.map_width):
                new_row.append(False) #Every tile begins as False
            self.walkable_tiles.append(new_row)

        #Marker positions, lists containing the on-grid positions
        self.player_starts = []
        self.angel_starts = []
        self.exit_tiles = []
        self.key_spots = []
        self.spawn_points = []
        self.junctions = []

        self.load_layers(data)


    def load_layers(self, data): #Fills the walkability grid and marker lists
        for layer in data["layers"]: #Iterates through each layer separately
            if layer["name"] == "Floor":
                for tile in layer["tiles"]:
                    col = tile["x"]
                    row = tile ["y"]
                    self.walkable_tiles[row][col] = True #Tile True in the walkability grid

            if layer["name"] == "Markers":
                for tile in layer["tiles"]:
                    self.add_markers(tile["id"], (tile["x"], tile["y"]))


    def add_markers(self, id, pos): #All ids are stored as strings in map.json
        if id == PLAYER_START_ID:
            self.player_starts.append(pos)
        elif id == ANGEL_START_ID:
            self.angel_starts.append(pos)
        elif id == EXIT_LEFT_ID or id == EXIT_RIGHT_ID:
            self.exit_tiles.append(pos)
        elif id == KEY_SPOT_ID:
            self.key_spots.append(pos)
        elif id == SPAWN_POINT_ID:
            self.spawn_points.append(pos)
        elif id == JUNCTION_ID:
            self.junctions.append(pos)


    def render(self, surf):
        for row in range(self.map_height):
            for col in range(self.map_width):
                if self.walkable_tiles[row][col]: #Checks if the tile is walkable
                    x = col * TILE_SIZE
                    y = row * TILE_SIZE
                    surf.blit(self.tile_img, (x,y)) #Draws the tile onto the surface passed in