
import pygame, math, random
pygame.init()


#générer la fenêtre du jeu
pygame.display.set_caption("Globbux vs Robotors")
screen = pygame.display.set_mode((1080,720))
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
player_width=10
player_height=10
player_speed=5
projectiles=[]
projectiles_speed=8
projectiles_height=10
projectiles_width=10
enemies_x=500
enemies_y=500
enemies_height=50
enemies_width=50
enemies_speed_x = 5
enemies_speed_y = 5
enemies_waypoint_x= random.randint(0,1080)
enemies_waypoint_y=random.randint(0,720)
enemies_radians = math.atan2(enemies_waypoint_y-enemies_y, enemies_waypoint_x-enemies_x)
mydegrees = math.degrees(enemies_radians)
print(mydegrees)
print(enemies_waypoint_x)
print(enemies_waypoint_y)
velocity_enemys_x = math.cos(enemies_radians) * enemies_speed_x
velocity_enemys_y = math.sin(enemies_radians) * enemies_speed_y
enemys=[]




def crash(): 
  
  global enemies_y
  
  
  if player_y < (enemies_y + 50): 
  
      if ((player_x > enemies_x
           and player_x < (enemies_x+ 50)) 
          or ((player_x + 50) > enemies_x
           and (player_x + 50) < (enemies_x + 50))): 
  
          enemies_y= 1080 + 1000
#en boucle tant que cette condition est vraie (on créer la boucle du jeu qui met à jour les persos etc)
while running:

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
        if projectile_x>1080:
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
    if player_x>1080-player_width:
       player_x=1080-player_width
    if player_y<0:
        player_y=0
    if player_y>720-player_height:
        player_y=720-player_height


    
    if abs(enemies_x-enemies_waypoint_x)<50 and abs(enemies_y-enemies_waypoint_y)<50:
        enemies_waypoint_x= random.randint(0,1080)
        enemies_waypoint_y=random.randint(0,720)
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
    if enemies_x>1080-50:
        enemies_x=1080-50
    if enemies_y<0:
        enemies_y=0
    if enemies_y>720-50:
        enemies_y=720-50




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

