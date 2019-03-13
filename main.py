import pygame
from particle import *

pygame.init()

screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()

particles_x = [Particle(x, 1, screen) for x in range(10, 1, -1)]
particles_y = [Particle(1, y, screen) for y in range(10, 1, -1)]

done = False

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                done = True

    #screen.fill((51,51,51))

    for particle in particles_x:
        particle.update(pygame.time.get_ticks())
        particle.show()

    for particle in particles_y:
        particle.update(pygame.time.get_ticks())
        particle.show()

    for particle_x in particles_x:
        for particle_y in particles_y:
            pygame.draw.circle(screen, (255, 255, 255), (particle_x.x, particle_y.y), 1)

    pygame.display.flip()
    clock.tick(120)