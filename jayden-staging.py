#Tic Tac Toe  with circles
import pygame
import time

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

running = True
i=0
cursor_x = 0
cursor_y = 0
X_or_Y=0
TicTacToe=[[0 for j in range(3)] for k in range(3)  ]
print(TicTacToe)

def draw_lines():
    corner_x=cursor_x*166
    corner_y=cursor_y*166
    screen.fill((0,0,0))

    for i in range(0, 3):
        for j in range(0, 3):
            if TicTacToe[i][j]==-1: 
                cordinate_y=i*166
                cordinate_x=j*166
                                                             #problem              #problem
                pygame.draw.circle(screen, (255, 255, 255), (cordinate_x+((500/3)/2), cordinate_y+((500/3)/2)), (56), 8)
            elif TicTacToe[i][j]==1: 
                cordinate=i*166
                cordinate_b=j*166                                            #problem              #problem
                pygame.draw.circle(screen, (255, 255, 255), (cordinate_b+((500/3)/2), cordinate+((500/3)/2)), (56))
    pygame.draw.line(screen, (255, 249, 0), (166, 0), (166, 500), 5)
    pygame.draw.line(screen, (255, 249, 0), (332, 0), (332, 500), 5)
    pygame.draw.line(screen, (255, 249, 0), (0, 166), (500, 166), 5)
    pygame.draw.line(screen, (255, 249, 0), (0, 332), (500, 332), 5)
    pygame.draw.line(screen, (0, 255, 0), (corner_x+96, corner_y+30), (corner_x+96, corner_y+106), 5)
    
         
    pygame.display.flip()
    
draw_lines()

while running:
    
    for event in pygame.event.get():
        draw_lines()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
  
            if event.key == pygame.K_LEFT:
                if cursor_x > 0:
                    cursor_x -= 1
                  
            if event.key == pygame.K_RIGHT:
                if cursor_x < 2:
                    cursor_x += 1
            if event.key == pygame.K_DOWN:
                if cursor_y < 2:
                    cursor_y += 1
            if event.key == pygame.K_UP:
                if cursor_y > 0:
                    cursor_y -= 1
            draw_lines()

            if event.key==pygame.K_SPACE and (X_or_Y==0 or X_or_Y==1):
                corner_x=cursor_x*166
                corner_y=cursor_y*166
                X_or_Y=-1
                TicTacToe[cursor_y][cursor_x]=X_or_Y
            elif event.key==pygame.K_SPACE and X_or_Y==-1:
                corner_x=cursor_x*166
                corner_y=cursor_y*166
                #pygame.draw.line(screen, (255, 255, 255), (corner_x, corner_y), (corner_x+166, corner_y+166), 10)
                X_or_Y+=2
                TicTacToe[cursor_y][cursor_x]=X_or_Y
            

        time.sleep(0.01)
        
print(TicTacToe)
pygame.quit()
class Point:
    x = 0
""""""

#Number guesser addion hints for kids
"""""
"""""
import random
custom=input("how long?")
custom=int(custom)
random_number=int(random.random()*custom)

username= input("your guess")
i=0
username=int(username)
while username!=random_number:
    hint= input("hint?")
    a=100
    if hint == str("yes") and username!=random_number:
        i=int(random.random()*custom/2)
        j=int(random.random()*custom/2-1)
        username=int(username)
        if i+j<random_number:
            print(i, j)
            print("bigger than", i, end=" " )
            print("+",j)
        else:
            
            print(i, j)
            print("smaller than", i, end=" " )
            print("+", j)

    username=int(username)
    if i!=0:
        username= input("your guess")
        username=int(username)
    if username>random_number:
        print("too big")
    elif username<random_number: 
        print("too small")
    
    i+=1

print("bingo")
print(username)

"""""

# awesome shooty game
"""""
how_many_points = 0
import pygame
import time
pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
rects_point=0 
circle_point=0  
running = True
screen.fill((23, 134, 231))
i=0
j=0 
bullets=[]
rect_bullets=[]
cir_points=0
def shooting(ji, points)->(int):
    i=0         
    while (i!=len(bullets)-1 and len(bullets)!=0): 
        j=i
        if len(bullets)>0:
            if i%2== 1 and i+1 < len(bullets):
                i=i+1
            if j%2==0 and (i+2 < len(bullets) and i+2!=len(bullets))  and i!=0:
                i=i+2
                j=i
            pygame.draw.line(screen, (193, 120, 12), (bullets[i], bullets[i+1]), (bullets[i]-10, bullets[i+1]), 5)
            pygame.display.flip()
            bullets[i]=bullets[i]-20
            print(bullets)
        now=i
        if bullets[i]<-10:
            del bullets[i]
            del bullets[i]
            print(bullets)
        if len(bullets)>=2:
            if now%2!=0:
                now=now+1
            if (bullets[now]==50) and(bullets[now+1]== 205+ji or bullets[now+1]== 200+ji or bullets[now+1]== 190+ji ):
                    
            
                    
                    points+=1
                    if points == 1:
                        text_surface = my_font.render('1', False, (255, 0, 0))
                        screen.blit(text_surface, (450, 20))
                        
                    return points
        i=i+1
        j=i
        if i%2==0 == len(bullets):
            return points
    return points
def rect_shooting(ji, points)->(int):   
    i=0                                                                              
    while i!=len(rect_bullets)-1 and len(rect_bullets)!=0: 
        j=i
        if rect_bullets[i]<500:
            if i%2== 1 and i+1 < len(rect_bullets):
                i=i+1
            if j%2==0 and i+2 < len(rect_bullets) and i !=0:
                i=i+2
                j=i
            if i%2==0 and i!=len(rect_bullets)-1:
                pygame.draw.circle(screen, (11, 1 , 211), (rect_bullets[i],rect_bullets[i+1]+30), 8)
                pygame.display.flip()
                rect_bullets[i]=rect_bullets[i]+20
                print(rect_bullets) 
        now=i
        if rect_bullets[i]>=500:
            del rect_bullets[i]
            del rect_bullets[i]
            print(rect_bullets)
     # Dying
        if len(rect_bullets)>=2:
            if now%2!=0:
                now=now+1
            if (rect_bullets[now]==420) and( rect_bullets[now+1]== 220+ji ):
                    points+=1
                    if rects_point != 5 or 10:
                        
                        pygame.display.flip()
                    return points
        i=i+1
        j=i
        if i == len(rect_bullets):
            return points
    return points
while running:
    screen.fill((114, 255, 32))   
    pygame.draw.circle(screen, (121, 12, 14), (400, 250+j), 30)                      
    pygame.draw.rect(screen,(23 , 123, 132),(0,180+i,100,50))
    pygame.display.flip()
    if cir_points == 0:
        text_surface = my_font.render('0', False, (255,0, 0))
        screen.blit(text_surface, (450, 20))
    if cir_points == 1:
        text_surface = my_font.render('1', False, (255,0, 0))
        screen.blit(text_surface, (450, 20))
    if cir_points == 2:
        text_surface = my_font.render('2', False, (255,0, 0))
        screen.blit(text_surface, (450, 20))
    if cir_points == 3:
        text_surface = my_font.render('3', False, (255,0, 0))
        screen.blit(text_surface, (450, 20))
    if cir_points == 4:
        text_surface = my_font.render('4', False, (255,0, 0))
        screen.blit(text_surface, (450, 20))
    if cir_points == 5:
        text_surface = my_font.render('5', False, (255,0, 0))
        screen.blit(text_surface, (450, 20))
    if how_many_points == 0:
        text_surface = my_font.render('0', False, (255,0, 0))
        screen.blit(text_surface, (10, 20))
    if how_many_points == 1:
        text_surface = my_font.render('1', False, (255,0, 0))
        screen.blit(text_surface, ( 10, 20))
    if how_many_points == 2:
        text_surface = my_font.render('2', False, (255,0, 0))
        screen.blit(text_surface, (10, 20))
    if how_many_points == 3:
        text_surface = my_font.render('3', False, (255,0, 0))
        screen.blit(text_surface, (10, 20))
    if how_many_points == 4:
        text_surface = my_font.render('4', False, (255,0, 0))
        screen.blit(text_surface, (10, 20))
    if how_many_points == 5:
        text_surface = my_font.render('5', False, (255,0, 0))
        screen.blit(text_surface, (10, 20))
        time.sleep(1)
    how_many_points=rect_shooting(j, how_many_points)
    pygame.display.flip() 
    cir_points=shooting(i, cir_points)
    pygame.display.flip() 
    if cir_points==5:
        t=1   
        screen.fill((23, 134, 231))         
        my_font = pygame.font.SysFont('Comic Sans MS', 50)                          
        text_surface = my_font.render('Circle Wins', False, (255,0, 0))
        screen.blit(text_surface, (100, 250))
        pygame.display.flip()  
        while event.type != pygame.QUIT:
            if event.type == pygame.QUIT:
                running = False  
            time.sleep(0.1)
        quit()
    if how_many_points==5:
            t=1   
            screen.fill((23, 134, 231))         
            my_font = pygame.font.SysFont('Comic Sans MS', 50)                          
            text_surface = my_font.render('Rectangle Wins', False, (255,0, 0))
            screen.blit(text_surface, (100, 250))
            pygame.display.flip()  
            while event.type != pygame.QUIT:
                if event.type == pygame.QUIT:
                    running = False  
                time.sleep(0.1)   
            quit()
    
    for event in pygame.event.get(): 
        
        
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_BACKSLASH:
                bullets.append(370)     
                bullets.append(250+j)
            if event.key==pygame.K_1:
                rect_bullets.append(100)     
                rect_bullets.append(180+i)
                

            if event.key ==pygame.K_DOWN:
                j=j+10
                if j>250:
                    j=j-10
            if event.key == pygame.K_UP:               
                j=j-10
                if j==-190:
                    j=j+10
            if event.key ==pygame.K_s:
                i=i+10
                if i > 300:
                    i=i-10
            if event.key == pygame.K_w:               
                i=i-10
                if i==-140:
                    i=i+10
    time.sleep(0.05)
