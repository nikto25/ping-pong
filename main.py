from pygame import *
from random import randint
def generate_color():
    return Color(randint(0,255),randint(0,255),randint(0,255))
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180,0,0))
score_font = font.Font(None, 70)
size = [600, 500]
FPS=60
color_selection = False
background = generate_color()
window = display.set_mode(size)
display.set_caption("ping-pong")
clock = time.Clock()
window.fill(background)
class GameSprite():
    def __init__(self, p_image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
racket2 = Player('racket.png', 30, 200, 50, 150, 4)
racket1 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png',200,200,50,50,4)
speed_x = 3 
speed_y = 3
score1=0
score2=0
score=0
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            color_selection = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:
            color_selection = False
    if color_selection:
        background = generate_color()

    if not finish:
        window.fill(background)
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        ball.reset()

        score_text = f'{score1}:{score2}'
        score_img = score_font.render(score_text, True, (255,255,255))
        score_rect = score_img.get_rect(center =(300,50))
        window.blit(score_img,score_rect)

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if color_selection:
            background = generate_color()
        if ball.rect.x < 0:
            score1+=1
            ball.rect.x=200
            ball.rect.y=200

        if ball.rect.x > 600:
            score2+=1
            ball.rect.x = 200
            ball.rect.y = 200

        if score1 == 3:
            
            window.blit(lose2, (200, 250))
            display.update()
            finish = True
        
        if score2 == 3:
            
            window.blit(lose1, (200, 250))
            display.update()
            finish = True
        window.blit(score_img,score_rect)
        display.update()
        clock.tick(FPS)
    
    