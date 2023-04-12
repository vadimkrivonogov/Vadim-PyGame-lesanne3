from lib2to3 import pygram
import pygame
import random
import sys

r=random.randit(0,255)
g=random.randit(0,255)
b=random.randit(0,255)

fon=[r,g,b]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 3")
pind.fill(fon)

for i in range(10):
    r=random.randit(0,255)
    g=random.randit(0,255)
    b=random.randit(0,255)
    varv=[r,g,b]

    laius=random.ranint(1,80)

    x=random.randint(0,610)
    y=random.randint(0,450)
    pygame.draw.rect(pind,varv,[x,y,30,30])

    pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        sys.exit()
pygame.quit()

