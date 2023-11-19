import pygame
import time
import random
#Chuẩn bị khung hình và dữ liệu cần thiết
pygame.init()
pygame.font.init()
green = (0,100,0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
height = 1300
width = 700
screen = pygame.display.set_mode((height,width))


def main_screen():
    logo = pygame.image.load("assets/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake vs Hunter ---By Tama")
def message(msg,text_color,size,x,y):
    font = pygame.font.Font("assets/font.ttf", size)
    text = font.render(msg,True,text_color)
    screen.blit(text ,(x , y))
def main():
    #khởi tạo module và màn hình 
    pygame.display.init()
    main_screen()
    #Khởi tạo hình ảnh
    background = pygame.image.load("assets/background.png")
    head_snake = pygame.image.load("assets/head.png")
    head_snake_stun = pygame.image.load("assets/dead_stun.png")
    apple = pygame.image.load("assets/apple.png")
    banana = pygame.image.load("assets/banana.png")
    snake_body = pygame.image.load("assets/snake_body.png")
    apple = pygame.transform.scale(apple, (50,50))
    banana = pygame.transform.scale(banana, (50,50))
    snake_body = pygame.transform.rotate(snake_body,90)
    head_snake_stun = pygame.transform.scale(head_snake_stun, (50,70))
    head_snake_stun = pygame.transform.rotate(head_snake_stun,90)
    head_snake = pygame.transform.scale(head_snake, (50,70))
    head_snake = pygame.transform.rotate(head_snake,90)
    #----------------------------------------------------------------------------------
    snake_list = []
    snake_length = 1
    # Vị trí của con rắn
    snake_xpos = 50
    snake_ypos = 50
    # Vị trí của trái táo
    apple_x = 200
    apple_y = 100
    time_drop_apple = 0
    # Vị trí của trái chuối
    banana_x = 200
    banana_y = 100
    time_drop_banana = 0
    # Số pixel con rắn đi được(tốc độ di chuyển)
    snake_step_x = 5
    snake_step_y = 0
    rotate = 'RIGHT'
    running = True
    game_over = False
    have_apple = True
    have_banana = False
    skill_snake = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                #Khởi tạo di chuyển-------------------------------------------------
                if event.key == pygame.K_LEFT:
                    if rotate == "RIGHT" or rotate == "LEFT":
                        continue
                    snake_step_x = -5 - snake_length
                    snake_step_y = 0
                    #Xoay-------------------------------------
                    if rotate == "DOWN":
                        head_snake = pygame.transform.rotate(head_snake,-90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,-90)
                        snake_body = pygame.transform.rotate(snake_body,-90)
                    elif rotate == "UP":
                        head_snake = pygame.transform.rotate(head_snake,90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,90)
                        snake_body = pygame.transform.rotate(snake_body,90)
                    rotate = "LEFT"
                    #-----------------------------------------
                elif event.key == pygame.K_RIGHT:
                    if rotate == "RIGHT" or rotate == "LEFT":
                        continue
                    snake_step_x = 5 + snake_length
                    snake_step_y = 0 
                    #Xoay-------------------------------------
                    if rotate == "DOWN":
                        head_snake = pygame.transform.rotate(head_snake,90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,90)
                        snake_body = pygame.transform.rotate(snake_body,90)
                    elif rotate == "UP":
                        head_snake = pygame.transform.rotate(head_snake,-90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,-90)
                        snake_body = pygame.transform.rotate(snake_body,-90)
                    rotate = "RIGHT"     
                    #-----------------------------------------        
                elif event.key == pygame.K_UP:
                    if rotate == "UP" or rotate == "DOWN":
                        continue
                    snake_step_x = 0
                    snake_step_y = -5 - snake_length
                    #Xoay-------------------------------------
                    if rotate == "LEFT":
                        head_snake = pygame.transform.rotate(head_snake,-90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,-90)
                        snake_body = pygame.transform.rotate(snake_body,-90)
                    elif rotate == "RIGHT":
                        head_snake = pygame.transform.rotate(head_snake,90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,90)
                        snake_body = pygame.transform.rotate(snake_body,90)
                    rotate = "UP"
                    #-----------------------------------------
                elif event.key == pygame.K_DOWN:
                    if rotate == "UP" or rotate == "DOWN":
                        continue
                    snake_step_x = 0
                    snake_step_y = 5 + snake_length
                    #Xoay-------------------------------------
                    if rotate == "LEFT":
                        head_snake = pygame.transform.rotate(head_snake,90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,90)
                        snake_body = pygame.transform.rotate(snake_body,90)
                    elif rotate == "RIGHT":
                        head_snake = pygame.transform.rotate(head_snake,-90)
                        head_snake_stun = pygame.transform.rotate(head_snake_stun,-90)
                        snake_body = pygame.transform.rotate(snake_body,-90)
                    rotate = "DOWN"
                    #-----------------------------------------
        snake_xpos += snake_step_x
        snake_ypos += snake_step_y
        #------------------------------------------------------------------------
        pygame.time.wait(30)
        screen.blit(background,(0,0))
        #----------------------------------------------
        #Xoay cơ thể-----------------------------------
        pos = [snake_xpos,snake_ypos]
        snake_list.insert(0,(list(pos)))
        for body_part in range(len(snake_list)):
            snake_body_x = snake_list[body_part][0]
            snake_body_y = snake_list[body_part][1]
            if rotate == "RIGHT":
                screen.blit(snake_body,(snake_body_x - 40,snake_body_y))
            elif rotate == "DOWN":
                screen.blit(snake_body,(snake_body_x,snake_body_y - 40))
            elif rotate == "UP":
                screen.blit(snake_body,(snake_body_x,snake_body_y + 60))
            elif rotate == "LEFT":
                screen.blit(snake_body,(snake_body_x + 60,snake_body_y))
        #----------------------------------------------
        #Game_over nếu rắn chết(vì đụng tường)-----------------------
        if (snake_xpos > 1200) or (snake_ypos > 600) or (snake_xpos < 30) or (snake_ypos < 30) :
            game_over = True
        while game_over == True:    
            message("Hunter Win",red,50,400,width/2)
            message("Press Q-Quit or C-Play Again",black,25,300,width/2-200)
            for body_part in range(len(snake_list)):
                snake_body_x = snake_list[body_part][0]
                snake_body_y = snake_list[body_part][1]
                if rotate == "RIGHT":
                    screen.blit(snake_body,(snake_body_x - 40,snake_body_y))
                elif rotate == "DOWN":
                    screen.blit(snake_body,(snake_body_x,snake_body_y - 40))
                elif rotate == "UP":
                    screen.blit(snake_body,(snake_body_x,snake_body_y + 60))
                elif rotate == "LEFT":
                    screen.blit(snake_body,(snake_body_x + 60,snake_body_y))
            screen.blit(head_snake_stun, (snake_xpos,snake_ypos))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        pygame.quit()
                    if event.key == pygame.K_c:
                        main()
        #----------------------------------------------
        #Game over nếu rắn chết(vì đụng trúng bản thân)---------
        for i in range(len(snake_list)):    
            body_x = snake_list[i][0]
            body_y = snake_list[i][1]
            if (snake_xpos == body_x) and (snake_ypos == body_y) and (i != 0):
                game_over == True
            while game_over == True:    
                message("Hunter Win",red,50,400,width/2)
                message("Press Q-Quit or C-Play Again",black,25,300,width/2-200)
                for body_part in range(len(snake_list)):
                    snake_body_x = snake_list[body_part][0]
                    snake_body_y = snake_list[body_part][1]
                    if rotate == "RIGHT":
                        screen.blit(snake_body,(snake_body_x - 40,snake_body_y))
                    elif rotate == "DOWN":
                        screen.blit(snake_body,(snake_body_x,snake_body_y - 40))
                    elif rotate == "UP":
                        screen.blit(snake_body,(snake_body_x,snake_body_y + 60))
                    elif rotate == "LEFT":
                        screen.blit(snake_body,(snake_body_x + 60,snake_body_y))
                screen.blit(head_snake_stun, (snake_xpos,snake_ypos))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            running = False
                            pygame.quit()
                        if event.key == pygame.K_c:
                            main()
        #Ăn táo--------------------------------------------
        if (apple_x - 30 <= snake_xpos <= apple_x + 30) and (apple_y - 30 <= snake_ypos <= apple_y + 30) and (have_apple == True):
            have_apple = False
            snake_length += 1
            apple_x = 0
            apple_y = 0
        else:
            snake_list.pop()
        #--------------------------------------------------
        #Thả táo-------------------------------------------
        if time_drop_apple > 50 and have_banana == False:
            time_drop_apple = 0
            apple_x = random.randint(30, 1200)
            apple_y = random.randint(30, 600)
            have_apple = True
        if have_apple == True:
            screen.blit(apple, (apple_x,apple_y))
        else:
            time_drop_apple += 1
        #-----------------------------------------------------
        #Ăn chuối--------------------------------------------
        if (banana_x - 30 <= snake_xpos <= banana_x + 30) and (banana_y - 30 <= snake_ypos <= banana_y + 30) and (have_banana == True):
            have_banana = False
            skill_snake += 1
            banana_x = 0
            banana_y = 0
        #Thả chuối-------------------------------------------
        if time_drop_banana > 500 and have_apple == False:
            time_drop_banana = 0
            banana_x = random.randint(30, 1200)
            banana_y = random.randint(30, 600)
            have_banana = True
        if have_banana == True:
            screen.blit(banana, (banana_x,banana_y))
        else:
            time_drop_banana += 1
        #-----------------------------------------------------
        print(time_drop_apple,time_drop_banana)
        print(have_apple,have_banana)
        screen.blit(head_snake, (snake_xpos,snake_ypos))
        pygame.display.update()
            
if __name__ == "__main__":
    main() 




