
import pygame, math, random, sys
pygame.init()
#générer la fenêtre du jeu
pygame.display.set_caption("Globbux vs Robotors")
width=1080
height=720
screen = pygame.display.set_mode((width,height))

# Game Fonts

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def main_menu():
    font = "assets/Font.ttf"
    gamez=False
    white=(255, 255, 255)
    black=(0, 0, 0)
    gray=(50, 50, 50)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    yellow=(255, 255, 0)
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
    red=(255, 0, 0)
    enemies = pygame.image.load("assets/Globbux.PNG")
    enemies = pygame.transform.scale(enemies,(50,50))
    boss = pygame.image.load("assets/Ship6.PNG")
    boss = pygame.transform.scale(boss,(500,300))
    boss_x=600
    boss_y=360
    boss_movement_speed_y=3
    boss_movement_speed_x=3
    boss_waypoint_x = 600
    boss_waypoint_y = random.randint(0, 1080)
    boss_width = 500
    boss_height = 200
    boss = pygame.transform.rotate(boss, 180)
    score=0
    hp_boss = 100
    player_x=30
    player_y=30
    player_width=35
    player_height=35
    player_speed=5
    projectiles=[]
    projectiles_speed=8
    projectiles_height=10
    projectiles_width=10
    enemys_height=50    
    enemys_width=50
    enemys_speed_x = 3
    enemys_speed_y = 4
    lazer=pygame.image.load("assets/Laser.PNG")
    lazer = pygame.transform.scale(lazer,(1080-boss_width,2000))
    lazer = pygame.transform.rotate(lazer, 270)
    lazer_x=0
    lazer_y=720-boss_y
    lazer_width=1080-boss_width
    lazer_height=boss_height
    lazer_distant=0
    black=(0, 0, 0)
    boss_status=True
    player_hp=100
    player_alive=True
    invincible_time=pygame.time.get_ticks()
    
   
   
    
    enemys=[[600,600,100,100]]
   
    clo_obj=pygame.time.Clock()
    


    
    gamez=True
    timev1=pygame.time.get_ticks()
    while gamez:
        
        #appliquer l'arrière plan du jeu
        screen.blit(background, (0,0))
        #D'abord mettre l'axe x puis y puis la largeur de l'objet et puis hauteur   
        if player_alive:
            screen.blit(Robolox, (player_x,player_y))
        if boss_status:
            screen.blit(boss, (boss_x,boss_y))
        screen.blit(lazer, (lazer_x,lazer_y))
        


        if(pygame.time.get_ticks() > timev1 + 100):
            timev1 = pygame.time.get_ticks()
            if(random.randint(0, 100) >= 0):

                enemys.append([random.randint(0,width),random.randint(0,height),random.randint(0,width),random.randint(0,height)])


        

        #  projectile_x      projectile_y
        #    v                 v0
        # [ [30,               30]          , [45, 22], [124, 454], ...]

        # On énumére (pour récupérer l'index / l'id et les valeurs) les projectiles
        for (index_projectile, projectile) in enumerate(projectiles):
            projectile[0] = projectile[0]+projectile[2]
            projectile[1] = projectile[1]+projectile[3]

            projectile_x = projectile[0]
            projectile_y = projectile[1]
            pygame.draw.rect(screen, red, pygame.Rect(projectile_x, projectile_y, projectiles_width, projectiles_height)) 
            for (index_enemy, enemy) in enumerate(enemys):
                (enemy_x, enemy_y, enemy_waypoint_x, enemy_waypoint_y) = enemy
                collision=is_collide_between_rect(projectile_x,projectile_y, projectiles_width,projectiles_height,enemy_x,enemy_y,enemys_width,enemys_height)
                if collision:
                    #enemys[index_enemy][0] = 9999999
                    #enemys[index_enemy][1] = 19999999
                    del enemys[index_enemy]
                    score=score+50
            if boss_status:
                collision_boss=is_collide_between_rect(projectile_x,projectile_y, projectiles_width,projectiles_height,boss_x,boss_y,boss_width,boss_height)
                if collision_boss:
                    hp_boss=hp_boss-1
                    print(hp_boss)
                if hp_boss<0:
                    del boss
                    boss_status=False
            if projectile_x>width:
                del projectiles[index_projectile] 



        if abs(boss_x-boss_waypoint_x)<50 and abs(boss_y-boss_waypoint_y)<50:
               
                boss_waypoint_y=random.randint(0-enemys_height,1080+enemys_height)
                 
        

        
        

        boss_radians = math.atan2(boss_waypoint_y-boss_y, boss_waypoint_x-boss_x)
        
        velocity_boss_x = math.cos(boss_radians) * boss_movement_speed_x
        velocity_boss_y = math.sin(boss_radians) * boss_movement_speed_y
        boss_x = boss_x+velocity_boss_x
        boss_y = boss_y+velocity_boss_y
        







        for (index_enemys, enemy) in enumerate(enemys):
            (enemy_x, enemy_y, enemy_waypoint_x, enemy_waypoint_y) = enemy

            enemy_radians = math.atan2(enemy_waypoint_y-enemy_y, enemy_waypoint_x-enemy_x)
            mydegrees = math.degrees(enemy_radians)
            velocity_enemy_x = math.cos(enemy_radians) * enemys_speed_x
            velocity_enemy_y = math.sin(enemy_radians) * enemys_speed_y
            enemy[0] = enemy[0]+velocity_enemy_x
            enemy[1] = enemy[1]+velocity_enemy_y
            screen.blit(enemies, (enemy_x,enemy_y))

       
     

            if abs(enemy_x-enemy_waypoint_x)<50 and abs(enemy_y-enemy_waypoint_y)<50:
                enemy_waypoint_x= random.randint(0,width)
                enemy_waypoint_y=random.randint(0,height)
                enemys[index_enemys] =  [enemy_x, enemy_y, enemy_waypoint_x, enemy_waypoint_y]

 
            '''collision=is_collide_between_rect(projectile_x,projectile_y, projectiles_width,projectiles_height,enemys_x,enemys_y,enemys_width,enemys_height)
            
            if abs(enemys_x-enemys_waypoint_x)<50 and abs(enemys_y-enemys_waypoint_y)<50:
                enemys_waypoint_x= random.randint(0,width)
                enemys_waypoint_y=random.randint(0,height)
                enemys_radians = math.atan2(enemys_waypoint_y-enemys_y, enemys_waypoint_x-enemys_x)
                mydegrees = math.degrees(enemys_radians)
                print(mydegrees)
                velocity_enemys_x = math.cos(enemys_radians) * enemys_speed_x
                velocity_enemys_y = math.sin(enemys_radians) * enemys_speed_y
                print(enemys_waypoint_x)
                print(enemys_waypoint_y)

            if collision:
                print("touchdown")
            if timev1>timev2+timev1:
                screen.blit(enemys, (enemys_x,enemys_y))'''
            for (index_enemys,enemy)  in enumerate(enemys): #Faire une indentation pour un nnouveau mode de jeu encore plus fun
                if is_collide_between_rect(player_x,player_y,player_width,player_height,enemy_x,enemy_y,enemys_width,enemys_height) and (pygame.time.get_ticks() > invincible_time + 100) :
                    player_hp=player_hp-1
                    print(player_hp)
                    invincible_time=pygame.time.get_ticks()
            if player_hp<0:
                gamez = False
                
        #metre à jour l'écran
        pygame.display.flip()


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
                projectiles.append([player_x, player_y,velocity_x+5,velocity_y+5])
                projectiles.append([player_x, player_y,velocity_x+5,velocity_y-5])


                
                    
            #pour vérifier que l'évènement est la fermeture de fenêtre
            if event.type == pygame.QUIT:
                
                pygame.quit()
                print("fermeture du jeu")



#         if abs(enemys_x-enemys_waypoint_x)<50 and abs(enemys_y-enemys_waypoint_y)<50:
#            enemys_waypoint_x= random.randint(0,width)
#            enemys_waypoint_y=random.randint(0,height)
#            enemys_radians = math.atan2(enemys_waypoint_y-enemys_y, enemys_waypoint_x-enemys_x)
#            mydegrees = math.degrees(enemys_radians)
#            velocity_enemys_x = math.cos(enemys_radians) * enemys_speed_x
#            velocity_enemys_y = math.sin(enemys_radians) * enemys_speed_y




while(True):
    main_menu()
    game()  