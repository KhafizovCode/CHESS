import pygame
from cheeeees import CHESS
def doskaa():
        n=0 
        dis.fill(brown)
        while n!=8:
            if n<3:
                for i in range(0,8):
                    if (n+i)%2==0 :
                        pygame.draw.rect(dis, white,[100*i, 100*n, 100, 100])
                        pygame.draw.circle(dis, black,[50*(2*i+1), 50*(2*n+1)],25)
            elif n<5:
                for i in range(0, 8):
                    if (n+i)%2==0:
                        pygame.draw.rect(dis, white,[100*i, 100*n, 100, 100])
            else:
                for i in range(0,8):
                    if (n+i)%2==0 :
                        pygame.draw.rect(dis, white,[100*i, 100*n, 100, 100])
                        pygame.draw.circle(dis, black,[50*(2*i+1), 50*(2*n+1)],25)

            n = n + 1
chess1=CHESS()
chess1.doska()
white = (255, 255, 255)
black = (0, 0, 0)
brown=(0, 25, 75,)
dis=pygame.display.set_mode((800,800))
pygame.display.set_caption("Chess")
z=int
while z!=0:
    pygame.display.update()
    doskaa()
pygame.quit()