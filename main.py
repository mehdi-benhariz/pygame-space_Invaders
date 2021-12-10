import pygame,random 

pygame.init()
#create the screen 
screen = pygame.display.set_mode((800,600))
#Design 
pygame.display.set_caption('game')
background=pygame.image.load('background.png')

#player diplay
playerIm = pygame.image.load("space-invaders.png")
X = 370
Y = 500
val=10
score = 0

def player(X,Y):
   screen.blit(playerIm,(X,Y))
#jumping function 
def jump():
       global Y
       jumpVal=-10 
       neg = 1 if (jumpVal > 0) else -1 
       if jumpVal>=-10 :
              Y-=(jumpVal**2)*0.5*neg
              jumpVal-=1
       else:
              jumpVal =10

  while(Y<=actualY):
              print("jump")
              print("Y:" + str(Y))

              Y+=jumpVal
              if(Y==actualY -300):
                     jumpVal= -5 

#player mouvement 
def Movement(k):
    global X,Y
    if event.key == pygame.K_RIGHT and X<736 :
                X+=val
    elif event.key == pygame.K_LEFT and X>0 :
                X-=val
    elif event.key == pygame.K_UP and Y>0  :
           jump()
    elif event.key == pygame.K_DOWN and Y <536 :
                Y+=val

#attack 
bulletIm = pygame.image.load("torpedo.png")
bull_X = X
bull_Y = Y
is_fire=False

def fire():
   global bull_X,bull_Y,is_fire,score
   bull_Y =Y
   bull_X =X
   is_fire=True
   for i in range(7):
        if abs(Xen[i]-bull_X)<15 or abs(Yen[i] -bull_Y)<15 : 
          destroyed[i] = True
          score+=1
   print(score)

#enemy diplay
enemyIm=[]
Xen=[]
Yen=[]
dx=[]
destroyed=[]

for i in range(7):
   enemyIm.append(pygame.image.load("enemy.png"))
   Xen.append(random.randint(0,800))
   Yen.append(random.randint(10,500))
   dx.append(5)
   destroyed.append(False)

def enemy(i):
   global destroyed,enemyIm,Xen,Yen
   if destroyed[i] == False:
        screen.blit(enemyIm[i],(Xen[i],Yen[i]))
 
def enemyMove(i):
   global Xen,dx,Yen
   Xen[i] +=dx[i]
   if Xen[i]<=0 :
      dx[i]=5
      Yen[i] +=10  
   elif Xen[i] >=736:
      dx[i]=-5  
      Yen[i] +=10

#score affiche 
font = pygame.font.Font('freesansbold.ttf',32)
def show_score(X,Y):
     screen.blit(font.render("score:"+ str(score), True,(0,255,0)) ,(X,Y))

# game over affiche
game = pygame.font.Font('freesansbold.ttf',64)
def show_game_over(X,Y):
      screen.blit(game.render("GAME OVER", True,(255,0,0)) ,(X,Y))


#looping the function
running=True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         if event.type == pygame.KEYDOWN:
           Movement(event.key)
           if event.key == pygame.K_SPACE:
               fire()   
            
    screen.fill((200,200,200))
    player(X,Y)
    for i in range(7):
       if Yen[i]>440:
          for j in range(7):
             Yen[j]=2000
          show_game_over(200,250)
          break
       if destroyed[i] == False:
           #enemy(i)
           enemyMove(i)
     
    if is_fire:
          screen.blit(bulletIm,(bull_X,bull_Y))
          bull_Y-=10
    show_score(10 ,10 )   
    pygame.display.update()