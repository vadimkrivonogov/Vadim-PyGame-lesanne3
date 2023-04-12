from lib2to3 import pygram
import pygame
import random
import sys

def Maja(x,y,laius,korgus,pind,varv):
    punktid=[(x,y- ((3/4.0) * korgus)), (x,y), (x+laius,y), (x+laius, y-(3/4.0) * korgus), (x,y- ((3/4.0) * korgus)), (x+laius/2.0, y- korgus), (x+laius,y-(3/4.0)*korgus)]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
fon=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
majavarv=[r,g,b]
pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 3")
pind.fill(fon)

for i in range(10):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    varv=[r,g,b]

    laius=random.randint(1,80)
    korgus=random.randint(1,80)

    x=random.randint(0,640-laius)
    y=random.randint(0,480-korgus)
    pygame.draw.rect(pind,varv,[x,y,laius,korgus])

    pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        sys.exit()
pygame.quit()

