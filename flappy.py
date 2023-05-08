import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 600
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Images vi skal bruke i spillet
bird_image = pg.image.load("images/bird.png")
bakgrunn = pg.image.load("images/background.jpg")
pipe_image = pg.image.load("images/pipe.png")

class Pipe:
    def __init__(self, x, y, bredde, høyde, farge):
        self.x = x
        self.y = y
        self.bredde = bredde
        self.høyde = høyde
        self.farge = farge

    def tegn(self):
        pg.draw.rect(vindu, self.farge (self.x, self.y, self.bredde, self.høyde))

class Ball:
    def __init__(self, farge, radius, høyde, key_up, key_down):
        self.radius = radius
        self.farge = farge
        self.key_up = key_up
        self.key_down = key_down
        self.x = VINDU_BREDDE / 3
        self.y = VINDU_BREDDE / 2
        self.høyde = høyde
        self.score = 0
        self.score_font = pg.font.SysFont(None, 100)

    def tegn_sirkel(self):
        pg.draw.circle(vindu, (self.farge), (self.x, self.y), self.radius)

    def flytt(self, taster):
    #flytte spilleren (hinder)
        if taster[self.key_up] and self.y > 2:  # Legger til en verdi for å hindre spilleren i å gå over øvre kant av vinduet
            self.y -= 1
        elif taster[self.key_down] and self.y + self.høyde < VINDU_HOYDE - 2:  # Legger til en verdi for å hindre spilleren i å gå under nedre kant av vinduet
            self.y += 1

ball1 = Ball((255, 255, 255), 10, 10, K_UP, K_DOWN)
hinder = Pipe(100, 200, 50, 100, (0, 255, 0))

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Farger bakgrunnen svart
    vindu.fill((0, 0, 0))

    #Tegner bakgrunn
    vindu.blit(bakgrunn,(0, 0))

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
    # Tegner og flytter spiller og hinder
    ball1.tegn_sirkel()
    ball1.flytt(trykkede_taster)
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()