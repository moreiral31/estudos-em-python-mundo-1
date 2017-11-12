import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
display = pygame.display.set_mode((800, 600))
pygame.display.update()
while pygame.mixer.music.get_busy():
 pygame.time.Clock().tick(10)