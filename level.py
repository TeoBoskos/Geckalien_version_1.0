import csv
import pygame

def load_layer(file_path, tile_size):
  """
  This function is designed to use the CSV data from the
  file, in order to create the map of the game. `-1` is
  equivalent to empty space, whereas `0` is equivalent to
  a grass block. So the functions loops through each tile
  of each row and check if it is equal to 0. If true, a
  grass block will be placed there.

  Parameters: `file_path`: The path to the CSV file,
    `tile_size`: The size of the tile in pixels.

  Return: It returns a list of rectangles ( the grass blocks
    basically ).
  """

  rects =[]

  with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for y, row in enumerate(reader):
      for x, tile in enumerate(row):
        if tile == '0':  # 0 means that there is a block of grass right there.
          rects.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))

  return rects