import sys
import pygame
from elements import *

# initDisplay
display = WindowSize(640, 640)
display.initDisplay()
screen = window.returnScreen()

camera = Camera(320, 320, screen, blue)
