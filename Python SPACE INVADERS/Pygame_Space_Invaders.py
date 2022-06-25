from pygame import *
import random
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_size,player_speed,player_health,move):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(player_size,player_size))

        self.player_speed = player_speed
        self.player_health = player_health
        self.move = move
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.player_speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.player_speed
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.player_speed
        if keys[K_DOWN] and self.rect.y <= 450:
            self.rect.y += self.player_speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 0:
            self.move = "right"
            self.rect.y += 25
        if self.rect.x >= 670:
            self.move = "left"
            self.rect.y += 25
        if self.move == "left":
            self.rect.x -= self.player_speed
        if self.move == "right":
            self.rect.x += self.player_speed

class Background():
    def __init__(self,background_image,background_x,background_y,background_width,background_height):
        self.image = transform.scale(image.load(background_image),(background_width,background_height))
        
        self.background_x = background_x
        self.background_y = background_y
    def create_background(self):
        window.blit(self.image,(self.background_x,self.background_y))

class Bullet():
    def __init__(self,bullet_image,bullet_x,bullet_y,bullet_size_x,bullet_size_y,bullet_speed,bullet_health,fire_delay):
        self.image = transform.scale(image.load(bullet_image),(bullet_size_x,bullet_size_y))
        
        self.fire_delay = fire_delay
        self.bullet_health = bullet_health
        self.bullet_speed = bullet_speed
        
        self.rect = self.image.get_rect()
        self.rect.y = bullet_y
        self.rect.x = bullet_x + 20
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def bullet_update(self):
        self.rect.y -= self.bullet_speed
    def enemy_bullet_update(self):
        self.rect.y += self.bullet_speed

class Phrase():
    def __init__(self,color1,color2,color3,font_type,text,x_pos,y_pos,font_size):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.font_type = font_type
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font_size = font_size
    def draw_text(self):
        self.font = font.SysFont(self.font_type,self.font_size)
        screen_text = self.font.render(self.text, True,(self.color1,self.color2,self.color3))
        window.blit(screen_text, [self.x_pos,self.y_pos])

def main_screen():
    background1.create_background()
    draw.rect(window,(255,255,255),(100,300,200,100))
    draw.rect(window,(255,255,255),(400,300,200,100))
    player_flip.reset()
    
    counter = 0
    for i in range(len(main_text_list)):
        main_text_list[i].draw_text()
    counter = 0
    for i in range(len(badguy_list)):
        badguy_list[i].reset()
    
    display.update()
    button_press = False
    while button_press == False:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and 100 <= e.pos[0] and 300 <= e.pos[1] and 300 >= e.pos[0] and 400 >= e.pos[1]:
                    button_press = True
                if e.button == 1 and 400 <= e.pos[0] and 300 <= e.pos[1] and 600 >= e.pos[0] and 400 >= e.pos[1]:
                    Instructions()
                    button_press = True

def Instructions():
    background1.create_background()
    draw.rect(window,(255,255,255),(10,10,200,100))

    for i in range(len(inst_text_list)):
        inst_text_list[i].draw_text()
    
    display.update()

    button_press = False
    while button_press == False:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and 10 <= e.pos[0] and 10 <= e.pos[1] and 210 >= e.pos[0] and 110 >= e.pos[1]:
                    main_screen()
                    button_press = True

def gameover():
    background1.create_background()
    draw.rect(window,(255,255,255),(100,300,200,100))
    draw.rect(window,(255,255,255),(400,300,200,100))

    for i in range(len(gameover_text_list)):
        gameover_text_list[i].draw_text()

    display.update()

    button_press = False
    while button_press == False:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and 100 <= e.pos[0] and 300 <= e.pos[1] and 300 >= e.pos[0] and 400 >= e.pos[1]:
                    button_press = True
                    return(True)
                if e.button == 1 and 400 <= e.pos[0] and 300 <= e.pos[1] and 600 >= e.pos[0] and 400 >= e.pos[1]:
                    button_press = True
                    return(False)

def victory():
    background1.create_background()
    draw.rect(window,(255,255,255),(100,300,200,100))
    draw.rect(window,(255,255,255),(400,300,200,100))
    victory_score_text = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Score: " + str(game_score),250,20,80)
    for i in range(len(victory_text_list)):
        victory_text_list[i].draw_text()
    victory_score_text.draw_text()

    display.update()

    button_press = False
    while button_press == False:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and 100 <= e.pos[0] and 300 <= e.pos[1] and 300 >= e.pos[0] and 400 >= e.pos[1]:
                    button_press = True
                    return(True)
                if e.button == 1 and 400 <= e.pos[0] and 300 <= e.pos[1] and 600 >= e.pos[0] and 400 >= e.pos[1]:
                    button_press = True
                    return(False)

def power():
    global extra_health
    global regeneration
    global number_bullets
    global bullet_health
    background1.create_background()
    powerup_text.draw_text()
    draw.rect(window,(255,255,255),(100,300,200,100))
    draw.rect(window,(255,255,255),(400,300,200,100))
    if power_option == 2:
        powerup_heart.reset()
        powerup_spike.reset()
        powerup_text4.draw_text()
        powerup_text5.draw_text()
    else:
        powerup_eye.reset()
        powerup_blast.reset()
        powerup_text1.draw_text()
        powerup_text2.draw_text()
        powerup_text3.draw_text()
    display.update()

    button_press = False
    while button_press == False:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and 100 <= e.pos[0] and 300 <= e.pos[1] and 300 >= e.pos[0] and 400 >= e.pos[1]:
                    button_press = True
                    if power_option == 2:
                        extra_health += 500
                    else:
                        bullet_health += 1

                if e.button == 1 and 400 <= e.pos[0] and 300 <= e.pos[1] and 600 >= e.pos[0] and 400 >= e.pos[1]:
                    button_press = True
                    if power_option == 2:
                        regeneration += 5
                    else:
                        number_bullets += 1
#spike,heart
#extra health,regeration

#tech,blast
#double shot,picering

window_width = 700
window_height = 500
display.set_caption("Space Invaders")
window = display.set_mode((window_width,window_height))

powerup_heart = GameSprite("Python SPACE INVADERS/power_up_icons_heart.png",450,200,100,0,0,"")
powerup_blast = GameSprite("Python SPACE INVADERS/power_up_icons_blast.png",450,200,100,0,0,"")
powerup_tech = GameSprite("Python SPACE INVADERS/power_up_icons_tech.png",450,200,100,0,0,"")
powerup_battery = GameSprite("Python SPACE INVADERS/power_up_icons_battery.png",150,200,100,0,0,"")
powerup_reload = GameSprite("Python SPACE INVADERS/power_up_icons_reload.png",150,200,100,0,0,"")
powerup_speedup = GameSprite("Python SPACE INVADERS/power_up_icons_speedup.png",150,200,100,0,0,"")
powerup_spike = GameSprite("Python SPACE INVADERS/power_up_icons_spike.png",150,200,100,0,0,"")
powerup_wings = GameSprite("Python SPACE INVADERS/power_up_icons_wings.png",150,200,100,0,0,"")
powerup_weight = GameSprite("Python SPACE INVADERS/power_up_icons_weight.png",350,200,100,0,0,"")
powerup_eye = GameSprite("Python SPACE INVADERS/power_up_icons_eye.png",150,200,100,0,0,"")

powerup_text = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Power Up Options",140,50,75)
powerup_text1 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Piercing",120,310,50)
powerup_text2 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Bullets",145,360,50)
powerup_text3 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Extra Bullet",410,335,45)
powerup_text4 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Regeration",410,335,45)
powerup_text5 = Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Extra Health",110,335,45)


main_text_list = []
main_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Space Invaders Odyssey",40,50,75))
main_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Created By: Inferno Studios",450,5,25))
main_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Single",150,310,50))
main_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Player",145,360,50))
main_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Instructions",410,335,45))

inst_text_list = []
inst_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Back To",50,20,45))
inst_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Main Screen",20,70,45))
inst_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Instructions",250,20,100))
inst_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","In Space Invaders Odysssy you must",20,150,45))
inst_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","eliminate all of the invading aliens to",20,200,45))
inst_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","save mother earth. Use the arrow keys to",20,250,45))
inst_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","avoid incoming lazers and fire back using",20,300,45))
inst_text_list.append(Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","the space bar. Best of luck!",20,350,45))

victory_text_list = []
victory_text_list.append(Phrase(0,255,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Victory",150,150,160))
victory_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Next Level",110,330,50))
victory_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Quit Game",410,330,50))

gameover_text_list = []
gameover_text_list.append(Phrase(255,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","GAMEOVER",150,150,110))
gameover_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Play Again",110,330,50))
gameover_text_list.append(Phrase(0,0,0,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Quit Game",410,330,50))

text1 = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Inferno Studios",50,50,100)
text2 = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Presents",50,250,100)
text3 = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Space Invaders",50,50,100)
text4 = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Odyssey",50,250,100)
text6 = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Press Space To Play",50,350,90)


big_player = Player("Python SPACE INVADERS/spaceinvadersship.png",450,250,200,10,50," ")
player_flip = Player("Python SPACE INVADERS/spaceinvadersship_flip1.png",50,160,100,10,100," ")

background1 = Background("Python SPACE INVADERS/space_background.png",0,0,700,500)

badguy_list = []
for i in range(10):
    badguy_list.append(Enemy("Python SPACE INVADERS/pink_dude-png.png",i*40 + 300,160,25,4,100,"left"))
    badguy_list.append(Enemy("Python SPACE INVADERS/orange_dude-png.png",i*40 + 300,185,25,4,100,"right"))
    badguy_list.append(Enemy("Python SPACE INVADERS/red_dude-png.png",i*40 + 300,210,25,4,100,"left"))
    badguy_list.append(Enemy("Python SPACE INVADERS/green_dude-png.png",i*40 + 300,235,25,4,100,"right"))

big_badguy = Enemy("Python SPACE INVADERS/orange_dude-png.png",450,250,200,4,100,"right")

power_option = 1
game_score = 0
level = 1
extra_health = 0
regeneration = 0


background1.create_background()
text1.draw_text()
text2.draw_text()
big_player.reset()
display.update()
time.delay(1000)

background1.create_background()
text3.draw_text()
text4.draw_text()
big_badguy.reset()
display.update()
time.delay(1000)


in_game = False

gameloop = True
while gameloop == True:

    player = Player("Python SPACE INVADERS/spaceinvadersship.png",325,420,50,10,1000 + extra_health," ")

    bullet_list = []

    enemy_bullet_list = []

    enemy_list = []
    for i in range(17):
        if level >= 1:
            enemy_list.append(Enemy("Python SPACE INVADERS/pink_dude-png.png",i*40,10,25,8,100,"left"))
        if level >= 2:
            enemy_list.append(Enemy("Python SPACE INVADERS/orange_dude-png.png",i*40 + 25,35,25,8,100,"right"))
        if level >= 3:
            enemy_list.append(Enemy("Python SPACE INVADERS/red_dude-png.png",i*40,60,25,8,100,"left"))
        if level >= 4:
            enemy_list.append(Enemy("Python SPACE INVADERS/green_dude-png.png",i*40 + 25,85,25,8,100,"right"))
        if level >= 5:
            enemy_list.append(Enemy("Python SPACE INVADERS/purple_dude-png.png",i*40,110,25,8,100,"left"))
        if level >= 6:
            enemy_list.append(Enemy("Python SPACE INVADERS/light_blue_dude-png.png",i*40 + 25,135,25,8,100,"right"))
        if level >= 7:
            enemy_list.append(Enemy("Python SPACE INVADERS/yellow_dude-png.png",i*40,160,25,8,100,"left"))
        if level >= 8:
            enemy_list.append(Enemy("Python SPACE INVADERS/orange_dude-png.png",i*40,10,25,8,100,"left"))
        if level >= 9:
            enemy_list.append(Enemy("Python SPACE INVADERS/red_dude-png.png",i*40 + 25,35,25,8,100,"right"))
        if level >= 10:
            enemy_list.append(Enemy("Python SPACE INVADERS/green_dude-png.png",i*40,60,25,8,100,"left"))
        if level >= 11:
            enemy_list.append(Enemy("Python SPACE INVADERS/purple_dude-png.png",i*40 + 25,85,25,8,100,"right"))
        if level >= 12:
            enemy_list.append(Enemy("Python SPACE INVADERS/light_blue_dude-png.png",i*40,110,25,8,100,"left"))
        if level >= 13:
            enemy_list.append(Enemy("Python SPACE INVADERS/yellow_dude-png.png",i*40 + 25,135,25,8,100,"right"))
        if level >= 14:
            enemy_list.append(Enemy("Python SPACE INVADERS/pink_dude-png.png",i*40,160,25,8,100,"left"))

    time1 = 0
    time2 = 0
    time3 = 0

    if in_game == False:
        level = 1
        game_score = 0
        main_screen()
        regeneration = 0
        extra_health = 0
        number_bullets = 1
        bullet_health = 1
        power_option = 2

    background1.create_background()
    text5 = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Level " + str(level),100,150,200)
    text5.draw_text()
    text6.draw_text()
    display.update()
    space_bar = False
    while space_bar == False:
        for e in event.get():
            keys = key.get_pressed()
            if keys[K_SPACE]:
                space_bar = True


    run = True
    while run == True:
        
        time.delay(50)

        background1.create_background()

        text_score = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Score: " + str(game_score),520,450,50)
        text_health = Phrase(255,255,255,"C:/Users/joshu/AppData/Local/Microsoft/Windows/INetCache/IE/9EP3SYSI/Authentic_Script_Rough[1].ttf","Health: " + str(player.player_health),20,450,50)
        text_score.draw_text()
        text_health.draw_text()

        if time.get_ticks() >= time3 and 995 + extra_health >= player.player_health:
            player.player_health += regeneration
            time3= time.get_ticks() + 1000

        for e in event.get():
            keys = key.get_pressed()
            if keys[K_SPACE] and time.get_ticks() >= time1:
                for i in range(number_bullets):
                    bullet_list.append(Bullet("Python SPACE INVADERS/green_lazer-png.png",player.rect.x - number_bullets * 5 + 10 * i + 7,player.rect.y + 10,5,10,20,bullet_health,500))
                time1 = time.get_ticks() + bullet_list[0].fire_delay
        

        if time.get_ticks() >= time2:
            random_number = random.randrange(0,(len(enemy_list)))
            enemy_bullet_list.append(Bullet("Python SPACE INVADERS/red_lazar-png.png",enemy_list[random_number].rect.x,enemy_list[random_number].rect.y,10,20,20,5,500))
            time2 = time.get_ticks() + 2000 - len(enemy_list) * 10

        counter = 0
        for i in bullet_list:
            if bullet_list[counter].rect.y >= 0:
                bullet_list[counter].bullet_update()
            else:
                del bullet_list[counter]
                counter -= 1
            counter += 1

        counter = 0
        for i in enemy_bullet_list:
            if enemy_bullet_list[counter].rect.y <= 500:
                enemy_bullet_list[counter].enemy_bullet_update()
            else:
                del enemy_bullet_list[counter]
                counter -= 1
            counter += 1

        counter = 0
        for i in enemy_list:
            enemy_list[counter].update()
            counter += 1

        counter = 0
        for i in bullet_list:
            bullet_list[counter].reset()
            counter += 1
        
        counter = 0
        for i in enemy_bullet_list:
            enemy_bullet_list[counter].reset()
            counter += 1

        counter = 0
        for i in enemy_list:
            enemy_list[counter].reset()
            counter += 1

        player.update()
        player.reset()

        hit = False
        b_counter = 0
        for i in bullet_list:
            e_counter = 0
            for i in enemy_list:
                if sprite.collide_rect(bullet_list[b_counter],enemy_list[e_counter]):
                    del_bullet = b_counter
                    del_enemy = e_counter
                    hit = True
                e_counter += 1
            b_counter += 1

        if hit == True:
            bullet_list[del_bullet].bullet_health -= 1
            del enemy_list[del_enemy]
            game_score += 1

        hit = False
        b_counter = 0
        for i in bullet_list:
            e_counter = 0
            for i in enemy_bullet_list:
                if sprite.collide_rect(bullet_list[b_counter],enemy_bullet_list[e_counter]):
                    del_bullet = b_counter
                    del_enemy_bullet = e_counter
                    hit = True
                e_counter += 1
            b_counter += 1

        if hit == True:
            bullet_list[del_bullet].bullet_health -= 1
            del enemy_bullet_list[del_enemy_bullet]

        hit = False
        for i in range(len(enemy_list)):
            if sprite.collide_rect(enemy_list[i],player):
                player.player_health -= 500
                hit = True
                del_bullet = i

        
        if hit == True:
            del enemy_list[del_bullet]

        hit = False
        for i in range(len(enemy_bullet_list)):
            if sprite.collide_rect(enemy_bullet_list[i],player):
                player.player_health -= 100
                hit = True
                del_bullet = i
        
        if hit == True:
            del enemy_bullet_list[del_bullet]

        counter = 0
        for i in bullet_list:
            if bullet_list[counter].bullet_health <= 0:
                del bullet_list[counter]
                counter -= 1
            counter += 1
        
        if player.player_health <= 0:
            run = False
            gameloop = gameover()
            in_game = False
        
        if 0 == len(enemy_list):
            run = False
            gameloop = victory()
            if gameloop == True:
                if power_option == 1:
                    power_option = 2
                else:
                    power_option = 1
                power()
            level += 1
            in_game = True


        display.update()
