import pygame
import random
import os
pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green = (0,255,0)
blue = (0,0,255)
''' for defing the height of the window'''
screen_width=900
screen_height=600

# for creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("SNAKES")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text,color,x,y):    #it will print the text on the screen
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,(x,y))




def plot_snake(gameWindow,color,snake_list,snake_size):       ## this is for adding to the snake and cutting its head so it willinc itself like the game.
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color, [x,y,snake_size,snake_size])


def welcome():
    exit_game = False 
    while not exit_game:
        gameWindow.fill((150,200,0))
        text_screen("WELCOME TO SNAKES",black,260,240)
        text_screen("PRESS SPACE TO PLAY ",black,265,290)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

               


#game loop
def gameloop():
    # game variable 
    '''game specific variable--> this can be anything but it would have it while loop below'''

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x= 0
    velocity_y= 0
    snake_list=[]     # for inc the length of the snake everytime when it eats the food
    snake_length=1
    # check if file exit
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
              highscore = f.read()


     # for the food of the snake
    food_x = random.randint(20,screen_width/2) # randint:- it generates random no. from 0 to screen_width
    food_y = random.randint(20,screen_height/2)
    score = 0  # for score
    init_velocity = 5
    snake_size =20
    fps = 60 #frame per second

    

    while not exit_game:
        if game_over:
           with open("highscore.txt","w") as f:
              f.write(str(highscore))

           gameWindow.fill((150,200,200))
           text_screen("GAME OVER!! Press enter to continue",red,100,250)
            
           
           for event in pygame.event.get():   # this will handle motion
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:   # this will run when the game is not over .
            for event in pygame.event.get():   # this will handle motion
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x= init_velocity # movement toward x axis
                        velocity_y = 0 # so that snake would move in a particular dirction

                    if event.key == pygame.K_LEFT:
                        velocity_x= - init_velocity #movement toward -x axis
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity # movement toward y axis
                        velocity_x= 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity #movement toward -y axis
                        velocity_x = 0
                    
                    # cheat code - that will automaticalliy increase the 
                    if event.key == pygame.K_q: # for "q" key
                        score +=5


            #Position
            snake_x=snake_x+ velocity_x
            snake_y=snake_y+ velocity_y


            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:    #abs func. will give absolute value for score
                score +=10

                food_x = random.randint(20,screen_width / 2) # randint:- it generates random no. from 0 to screen_width
                food_y = random.randint(20,screen_height / 2)
                snake_length +=5
                if score > int(highscore):
                    highscore = score


            gameWindow.fill(white)
            text_screen("score : "+ str(score) + "  High Score : " + str(highscore),blue,5,5)

            # for the food(red)
            pygame.draw.rect(gameWindow,red, [food_x,food_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:   ## for cutting its head
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
            
            # for making snakes's head with black color using rectangle feature in python

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                

            #pygame.draw.rect(gameWindow,black, [snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
