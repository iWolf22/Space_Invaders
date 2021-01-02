from pygame import *

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

class Background():
    def __init__(self,background_image,background_x,background_y,background_width,background_height):
        self.image = transform.scale(image.load(background_image),(background_width,background_height))
        
        self.background_x = background_x
        self.background_y = background_y
    def create_background(self):
        window.blit(self.image,(self.background_x,self.background_y))

class Button():
    def __init__(self,left_x,top_y):
        self.top_y = top_y
        self.left_x = left_x
    def buttom_press(self):
        if e.pos[0] >= self.left_x and e.pos[0] + 250 <= self.left_x and e.pos[1] >= self.top_y and e.pos[1] <= self.top_y + 250:
            print(e.pos)

window_width = 1400
window_height = 700
display.set_caption("X and O")
window = display.set_mode((window_width,window_height))

gameloop = True
while gameloop == True:
    draw.rect(window,(255,255,255),(950,100,10,500))
    draw.rect(window,(255,255,255),(1150,100,10,500))
    draw.rect(window,(255,255,255),(800,250,500,10))
    draw.rect(window,(255,255,255),(800,450,500,10))
    
    button_list = []
    button1A = Button(800,100)
    button_list.append(button1A)
    button1B = Button(950,100)
    button_list.append(button1B)
    button1C = Button(1200,100)
    button_list.append(button1C)
    button2A = Button(800,350)
    button_list.append(button2A)
    button2B = Button(950,350)
    button_list.append(button2B)
    button2C = Button(1200,350)
    button_list.append(button2C)
    button3A = Button(800,600)
    button_list.append(button3A)
    button3B = Button(950,600)
    button_list.append(button3B)
    button3C = Button(1200,600)
    button_list.append(button3C)


    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                for i in range(len(button_list)):
                    button_list[i].buttom_press()
    
    display.update()

