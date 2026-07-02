import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pro Shooter 🚀")

clock = pygame.time.Clock()

# ---------- LOAD ASSETS ----------
player_img = pygame.image.load("assets/player.png")
enemy_img = pygame.image.load("assets/enemy.png")
bullet_img = pygame.image.load("assets/bullet.png")
bg_img = pygame.image.load("assets/background.jpg")

shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.play(-1)

# resize images
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

# ---------- PLAYER ----------
player = pygame.Rect(275, 600, 50, 50)
player_speed = 6
health = 3

# ---------- GAME DATA ----------
bullets = []
enemies = []
score = 0
game_state = "menu"

font_big = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 22)

# ---------- FUNCTIONS ----------
def reset_game():
    global bullets, enemies, score, health
    bullets = []
    enemies = []
    score = 0
    health = 3

def draw_text(text, font, x, y, color=(255,255,255)):
    screen.blit(font.render(text, True, color), (x, y))

def spawn_enemy():
    if random.randint(1, 25) == 1:
        enemies.append(pygame.Rect(random.randint(0, WIDTH-40), 0, 40, 40))

def move_enemies():
    global health
    for e in enemies[:]:
        e.y += random.randint(2,4)
        if e.y > HEIGHT:
            enemies.remove(e)
            health -= 1

def move_bullets():
    for b in bullets[:]:
        b.y -= 8
        if b.y < 0:
            bullets.remove(b)

def check_collision():
    global score
    for e in enemies[:]:
        for b in bullets[:]:
            if e.colliderect(b):
                enemies.remove(e)
                bullets.remove(b)
                score += 10
                break

def check_player_hit():
    global game_state
    for e in enemies:
        if player.colliderect(e):
            game_state = "gameover"

# ---------- MAIN LOOP ----------
running = True
while running:
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            if event.type == pygame.KEYDOWN:
                reset_game()
                game_state = "playing"

        elif game_state == "playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(player.x+20, player.y, 10, 20))
                    shoot_sound.play()

        elif game_state == "gameover":
            if event.type == pygame.KEYDOWN:
                game_state = "menu"

    # ---------- STATES ----------
    if game_state == "menu":
        draw_text("PRO SHOOTER", font_big, 170, 250)
        draw_text("Press any key to start", font_small, 180, 320)

    elif game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH-50:
            player.x += player_speed

        spawn_enemy()
        move_enemies()
        move_bullets()
        check_collision()
        check_player_hit()

        # draw player
        screen.blit(player_img, (player.x, player.y))

        # draw bullets
        for b in bullets:
            screen.blit(bullet_img, (b.x, b.y))

        # draw enemies
        for e in enemies:
            screen.blit(enemy_img, (e.x, e.y))

        # UI
        draw_text(f"Score: {score}", font_small, 10, 10)
        draw_text(f"Health: {health}", font_small, 450, 10)

        if health <= 0:
            game_state = "gameover"

    elif game_state == "gameover":
        draw_text("GAME OVER", font_big, 170, 250, (255,0,0))
        draw_text(f"Score: {score}", font_small, 250, 320)
        draw_text("Press any key to restart", font_small, 150, 370)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()