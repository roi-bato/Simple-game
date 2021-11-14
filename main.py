
import pygame, math, random, sys
pygame.init()


#générer la fenêtre du jeu
pygame.display.set_caption("Globbux vs Robotors")
width=1080
height=720
screen = pygame.display.set_mode((width,height))
Robolox = pygame.image.load("assets/Robotor.PNG")
Robolox = pygame.transform.scale(Robolox,(35,35))
background = pygame.image.load("assets/Capture.PNG")
player_char = pygame.image.load('assets/Robotor.PNG')
enemies = pygame.image.load("assets/Globbux.PNG")
enemies = pygame.transform.scale(enemies,(50,50))
running = True
color = (255,0,0)
player_x=30
player_y=30
player_width=35
player_height=35
player_speed=5
projectiles=[]
projectiles_speed=8
projectiles_height=10
projectiles_width=10
enemies_x=500
enemies_y=500
enemies_height=50
enemies_width=50
enemies_speed_x = 1
enemies_speed_y = 1
enemies_waypoint_x= random.randint(0,width)
enemies_waypoint_y=random.randint(0,height)
enemies_radians = math.atan2(enemies_waypoint_y-enemies_y, enemies_waypoint_x-enemies_x)
mydegrees = math.degrees(enemies_radians)
print(mydegrees)
print(enemies_waypoint_x)
print(enemies_waypoint_y)
velocity_enemys_x = math.cos(enemies_radians) * enemies_speed_x
velocity_enemys_y = math.sin(enemies_radians) * enemies_speed_y
enemys=[]
menu=1
color_dark=(100,100,100)
white_color=(255,255,255)
menu_state=1


white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
gamez=False
# Game Fonts
font = "assets/Font.ttf"
 
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 



def main_menu():


   
    selected="start"
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                    
                        

                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        
                        menu=False
                        gamez=True
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(red)
        title=text_format("JEU SIMPLE", font, 90, yellow)
        if selected=="start":
            text_start=text_format("START", font, 75, white)

        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        

def is_collide_between_rect(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    # are the sides of one rectangle touching the other?
    return r1x + r1w >= r2x and r1x <= r2x + r2w and r1y + r1h >= r2y and r1y <= r2y + r2h   




#en boucle tant que cette condition est vraie (on créer la boucle du jeu qui met à jour les persos etc)
def game():
    pygame.display.set_caption("Globbux vs Robotors")
    width=1080
    height=720
    screen = pygame.display.set_mode((width,height))
    Robolox = pygame.image.load("assets/Robotor.PNG")
    Robolox = pygame.transform.scale(Robolox,(35,35))
    background = pygame.image.load("assets/Capture.PNG")
    player_char = pygame.image.load('assets/Robotor.PNG')
    enemies = pygame.image.load("assets/Globbux.PNG")
    enemies = pygame.transform.scale(enemies,(50,50))
    running = True
    color = (255,0,0)
    player_x=30
    player_y=30
    player_width=35
    player_height=35
    player_speed=5
    projectiles=[]
    projectiles_speed=8
    projectiles_height=10
    projectiles_width=10
    enemies_x=500
    enemies_y=500
    enemies_height=50
    enemies_width=50
    enemies_speed_x = 1
    enemies_speed_y = 1
    enemies_waypoint_x= random.randint(0,width)
    enemies_waypoint_y=random.randint(0,height)
    enemies_radians = math.atan2(enemies_waypoint_y-enemies_y, enemies_waypoint_x-enemies_x)
    mydegrees = math.degrees(enemies_radians)
    print(mydegrees)
    print(enemies_waypoint_x)
    print(enemies_waypoint_y)
    velocity_enemys_x = math.cos(enemies_radians) * enemies_speed_x
    velocity_enemys_y = math.sin(enemies_radians) * enemies_speed_y
    enemys=[]
    menu=1
    color_dark=(100,100,100)
    white_color=(255,255,255)
    menu_state=1
    current_state=menu
    if current_state=="gamez":
        gamez=True
    while gamez:

        #appliquer l'arrière plan du jeu
        screen.blit(background, (0,0))
        #D'abord mettre l'axe x puis y puis la largeur de l'objet et puis hauteur   
        screen.blit(Robolox, (player_x,player_y))
        screen.blit(enemies, (enemies_x,enemies_y))
        

        #  projectile_x      projectile_y
        #    v                 v
        # [ [30,               30]          , [45, 22], [124, 454], ...]

        # On énumére (pour récupérer l'index / l'id et les valeurs) les projectiles
        for (index_projectile, projectile) in enumerate(projectiles):
            projectile[0] = projectile[0]+projectile[2]
            projectile[1] = projectile[1]+projectile[3]

            projectile_x = projectile[0]
            projectile_y = projectile[1]
            pygame.draw.rect(screen, color, pygame.Rect(projectile_x, projectile_y, projectiles_width, projectiles_height)) 

            collision=is_collide_between_rect(projectile_x,projectile_y, projectiles_width,projectiles_height,enemies_x,enemies_y,enemies_width,enemies_height)

            if collision:
                print("touchdown")

            if projectile_x>width:
                del projectiles[index_projectile] 





        #metre à jour l'écran
        pygame.display.flip()





        enemies_x=enemies_x+velocity_enemys_x
        enemies_y=enemies_y+velocity_enemys_y



        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x=player_x-player_speed
        if keys[pygame.K_RIGHT]:
            player_x=player_x+player_speed
        if keys[pygame.K_UP]:
            player_y=player_y-player_speed
        if keys[pygame.K_DOWN]:
            player_y=player_y+player_speed
        
        if player_x<0:
            player_x=0
        if player_x>width-player_width:
             player_x=width-player_width
        if player_y<0:
            player_y=0
        if player_y>height-player_height:
            player_y=height-player_height

        if is_collide_between_rect(player_x,player_y,player_width,player_height,enemies_x,enemies_y,enemies_width,enemies_height) :
            player_x=0
            player_y=0
            main_menu()
        




        if abs(enemies_x-enemies_waypoint_x)<50 and abs(enemies_y-enemies_waypoint_y)<50:
            enemies_waypoint_x= random.randint(0,width)
            enemies_waypoint_y=random.randint(0,height)
            enemies_radians = math.atan2(enemies_waypoint_y-enemies_y, enemies_waypoint_x-enemies_x)
            mydegrees = math.degrees(enemies_radians)
            print(mydegrees)
            velocity_enemys_x = math.cos(enemies_radians) * enemies_speed_x
            velocity_enemys_y = math.sin(enemies_radians) * enemies_speed_y
            print(enemies_waypoint_x)
            print(enemies_waypoint_y)









        #print(projectiles)
        
        if enemies_x<0:
            enemies_x=0
        if enemies_x>width-50:
            enemies_x=width-50
        if enemies_y<0:
            enemies_y=0
        if enemies_y>height-50:
            enemies_y=height-50




        #si le joueur ferme cette fenêtre
        for event in pygame.event.get() :

        
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                    
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                myradians = math.atan2(pos_y-player_y, pos_x-player_x)
                mydegrees = math.degrees(myradians)
                
                velocity_x = math.cos(myradians) * projectiles_speed
                velocity_y = math.sin(myradians) * projectiles_speed

                projectiles.append([player_x, player_y,velocity_x,velocity_y])
                    
            #pour vérifier que l'évènement est la fermeture de fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu")
if gamez==True:
    game()
else:
    main_menu()