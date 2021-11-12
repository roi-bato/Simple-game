
import pygame, math
pygame.init()

#générer la fenêtre du jeu
pygame.display.set_caption("Globbux vs Robotors")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/Capture.PNG")

running = True
color = (255,0,0)
player_x=30
player_y=30
player_width=50
player_height=50
player_speed=5
projectiles=[]
projectiles_speed=8
projectiles_height=10
projectiles_width=10


#en boucle tant que cette condition est vraie (on créer la boucle du jeu qui met à jour les persos etc)
while running:

    #appliquer l'arrière plan du jeu
    screen.blit(background, (0,0))
    #D'abord mettre l'axe x puis y puis la largeur de l'objet et puis hauteur   
    pygame.draw.rect(screen, color, pygame.Rect(player_x, player_y, player_width, player_height)) 
    

    #  projectile_x      projectile_y
    #    v                 v
    # [ [30,               30]          , [45, 22], [124, 454], ...]

    # On énumére (pour récupérer l'index / l'id et les valeurs) les projectiles
    for (index, projectile) in enumerate(projectiles):
        projectile[0] = projectile[0]+projectile[2]
        projectile[1] = projectile[1]+projectile[3]

        projectile_x = projectile[0]
        projectile_y = projectile[1]
        pygame.draw.rect(screen, color, pygame.Rect(projectile_x, projectile_y, projectiles_width, projectiles_height)) 
        if projectile_x>1080:
            del projectiles[index] 

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
    if player_x>1080-player_width:
       player_x=1080-player_width
    if player_y<0:
        player_y=0
    if player_y>720-player_height:
        player_y=720-player_height



    #print(projectiles)
    


    #si le joueur ferme cette fenêtre
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
            myradians = math.atan2(pos_y-player_y, pos_x-player_x)
            mydegrees = math.degrees(myradians)
            print(mydegrees)
            velocity_x = math.cos(myradians) * projectiles_speed
            velocity_y = math.sin(myradians) * projectiles_speed

            projectiles.append([player_x, player_y,velocity_x,velocity_y])

        #pour vérifier que l'évènement est la fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

