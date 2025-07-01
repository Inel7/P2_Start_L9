import pygame
import time
from snake import Snake
from food import Food
from startcode.snake import veld_grootte

# kleuren
kleur_achtergrond = (0,0,0)
kleur_tekst = (0,255,0)
# schermgrootte
breedte = 800
hoogte = 600
veld_grootte = 20
# Snelheid van het spel
spel_snelheid = 5

# Initialiseren van de pygame-module
pygame.init()

# Creëer een venster met opgegeven breedte en hoogte
venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('snake')

# Functie om de score op het scherm te tonen
def toon_score(score, venster):
    font = pygame.font.Font(None, 36)
    scoretekst = font.render(f"Score: {score}", True, kleur_tekst)
    venster.blit(scoretekst, (10, 10))

# Hoofdloop van het spel
def game_lus():
    snake = Snake(breedte//2, hoogte//2)
    food = Food(breedte, hoogte)
    score = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.x_verandering == 0:
                    snake.x_verandering = -veld_grootte
                    snake.y_verandering = 0
                elif event.key == pygame.K_RIGHT and snake.x_verandering == 0:
                    snake.x_verandering = veld_grootte
                    snake.y_verandering = 0
                elif event.key == pygame.K_UP and snake.y_verandering == 0:
                    snake.y_verandering = -veld_grootte
                    snake.x_verandering = 0
                elif event.key == pygame.K_DOWN and snake.y_verandering == 0:
                    snake.y_verandering = veld_grootte
                    snake.x_verandering = 0

        snake.beweeg()
        if snake.is_buiten_veld(breedte, hoogte) or snake.raakt_zichzelf():
            game_over = True
        #tekenen
        venster.fill(kleur_achtergrond)
        snake.teken(venster)
        food.teken(venster)
        toon_score(score, venster)

        if snake.x == food.x and snake.y == food.y:
            food.plaats_voedsel()
            snake.lengte_slang += 1
            score += 10

        pygame.display.update()

        time.sleep(1/ spel_snelheid)
    print("jouw score is: ", score)

game_lus()

# Start de hoofdloop van het spel