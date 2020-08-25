import pygame

pygame.init()

window = pygame.display.set_mode([800, 580])

quadX = 100
quadY = 100
speedX = 0
speedY = 0

clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        speedX = 1
      if event.key == pygame.K_LEFT:
        speedX = -1
      if event.key == pygame.K_DOWN:
        speedY = 1
      if event.key == pygame.K_UP:
        speedY = -1
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        speedX = 0
      if event.key == pygame.K_LEFT:
        speedX = 0
      if event.key == pygame.K_DOWN:
        speedY = 0
      if event.key == pygame.K_UP:
        speedY = 0
          

  window.fill((255, 255, 255))

  pygame.draw.rect(window, (0, 0, 255), 
    [quadX, quadY, 100, 100])

  quadX = quadX + speedX  
  quadY = quadY + speedY

  pygame.display.update()
  clock.tick(60)