import sys, pygame, random

size = width, height = 500, 500
black = 0, 0, 0
fireworks = []
colors = [(0, 255, 0),(0, 0, 255),(255,0,0),(255, 255, 0),(0, 255, 255),(255, 0, 255)]
auto = True
#how much the fireworks appear (1-100)
frequency = 5

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill(black)

class firework:
    def __init__(self, surface, color, pos,size,stage):
        self.surfacew, self.surfaceh = pygame.display.get_surface().get_size()
        self.surface = surface
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.r = size
        self.pos = pos
        self.speed = (0, -1)
        self.speedx = self.speed[0]
        self.speedy = self.speed[1]
        self.stage = 1
        self.stagemax = stage
        self.bombheight = self.y - (self.surfaceh/2)
        self.end = False
        self.particles = []
        self.all_particles = 0
        pygame.draw.circle(self.surface, self.color, self.pos,self.r)

    def move(self):
        if self.y < self.bombheight:
            if self.stage >= self.stagemax:
                self.end = True
            pygame.draw.circle(self.surface, self.color, self.pos, int(self.r*self.stage/2),1)
            self.stage = self.stage + 1
        else:
            self.x = self.x + self.speedx
            self.y = self.y + self.speedy
            self.pos = (self.x,self.y)
            pygame.draw.circle(self.surface, self.color, self.pos, self.r)

while 1:
    screen.fill(black)
    if auto:
        if random.randrange(1,100) < frequency:
            color = random.choice(colors)
            size = random.randrange(2, 10)
            stage = random.randrange(2, 8)*size
            pos = (random.randrange(10,width-10),random.randrange(height*4/5,height))
            fireworks.append(firework(screen, color, pos, size, stage))

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = random.choice(colors)
            size = random.randrange(2,10)
            stage = random.randrange(2, 8) * size
            fireworks.append(firework(screen, color, (event.pos[0],event.pos[1]),size,stage))

    for thefirework in fireworks:
        thefirework.move()
        if thefirework.end :
            fireworks.remove(thefirework)
    pygame.display.flip()
    clock.tick(120)
