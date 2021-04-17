import pygame, sys

from varname import nameof

import random

from listfile import *

from persoimage import *
from listesinsults import *

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

joueur=''

nom= ''
Width = 800
Height = 600
RED =(255,0,0)
YELLOW = (255,255,0)
# Green= (52, 255, 51)
Green =(0,128,0)
BACKGROUND_COLOR=(0,0,0)
white = (255,255,255)
#player_pos=[400,300]
testx=400
testy=150
player_size= 100
player_health =100
enemy_health=100
score = 0
click = False
leftRect=50
leftRectVerbs=50
topRect=100
topRectVerbs=100
widthRect=200
heightRect=50
heightRectVerbs=30
widthRectVerbs=70
rectButton=pygame.Rect(leftRect,topRect,widthRect,heightRect)
rectButtonVerbs=pygame.Rect(leftRectVerbs,topRectVerbs,widthRectVerbs,heightRectVerbs)

from characterList import Characters

Player1 = Characters("Lucas")
Player2 = Characters("Peter")
Player3 = Characters("Itachi")
Player4 = Characters("Max")
Player5 = Characters("Sarah")
PlayerArray= [Player1.name,Player2.name,Player3.name,Player4.name,Player5.name]
Playercopy=PlayerArray.copy()
myFont= pygame.font.SysFont("monospace",35)
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 20)
fontVerbs = pygame.font.SysFont("monospace",20,True)
def enemy_choice(playerTab,playerone):
    for player in playerTab:
        if player == playerone:  
            playerTab.remove(player)
    return playerTab

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def text_objectsVerbs(text, font):
    textSurface = fontVerbs.render(text, True, white)
    return textSurface, textSurface.get_rect()
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
playerluck1= Player1.luck 
playerluck2= Player2.luck 
playerluck3= Player3.luck 
playerluck4= Player4.luck 
playerluck5= Player5.luck 
playerStrength1= Player1.strength 
playerStrength2= Player2.strength 
playerStrength3= Player3.strength 
playerStrength4= Player4.strength 
playerStrength5= Player5.strength
# exclaListe = Exclamationsfinales
# compListe = Complément
# liaisonListe= Liaisons
# sujetListe= sujet
listTest=['abaisser,aim:er,lower', 'abandonner,aim:er,abandon', 'abasourdir,fin:ir,stun','abâtardir,fin:ir,bastardize', 'abattre,bat:tre,tear down', 'abcéder,c:éder,abscess']
nameWrap = nameof(listVerbs)

def recupOneindiceVerbs(liste):
    newList=[]
    for i in range(0,5):
        listeI=liste[random.randint(0,len(liste))]
        #print(listeI)
        indicevirgule= listeI.index(',')
        newList.append(listeI[0:indicevirgule])
    #print(newList)
    return newList
#recupOneindiceVerbs(listVerbs)
def recupOneindice(liste):
    newList=[]
    for words in range(0,5):
        liste2=liste[random.randint(0,len(liste)-1)]
        #print(liste2)
        newList.append(liste2)
    #print(newList)
    return newList
exclaListe=recupOneindice(Exclamationsfinales)
compListe=recupOneindice(Complément)
liaisonListe=recupOneindice(Liaisons)
sujetListe=recupOneindice(sujet)
verbListe=recupOneindiceVerbs(listVerbs)
# print(verbListe)
# print(exclaListe)
# print(compListe)
# print(liaisonListe)
# print(sujetListe)
#print(fooname)
playerPv1= Player1.hp
playerPv2= Player2.hp
playerPv3= Player3.hp
playerPv4= Player4.hp
playerPv5= Player5.hp
def combatWords(joueur1,joueur2):
    global enemy_health
    global player_health
    # joueur1= joueur1
    # joueur2= joueur2
    playerpv=100
    enemypv=100
    joueur1flag= True
    joueur2flag= False
    TotalDegat= 0
    TotalDegatEnemy= 0
    gameover=False 
    print(gameover)
    def luck (joueur,degat):
        if joueur == Player1.name:
            degat+= (degat/2)
        if joueur == Player2.name:
            degat*= playerluck2
        if joueur == Player3.name:
            degat*= playerluck3
        if joueur == Player4.name:
            degat*= playerluck4
        if joueur == Player5.name:
            degat+= (degat/2)
        return degat
        print(degat)  
    def strength(joueur):
        x= 1
        degat =1
        if joueur == Player1.name:
            degat= playerStrength1
            x=2
        if joueur == Player2.name:
            degat= playerStrength2
            x=4
        if joueur == Player3.name:
            degat= playerStrength3
            x=3
        if joueur == Player4.name:
            degat= playerStrength4
            x=5
        if joueur == Player5.name:
            degat= playerStrength5
            x=2
        res= [x,degat]
        return res
    def chooseWords(liste,liste2,liste3,liste4,liste5,flagjoueur):
        joueur1flag= flagjoueur
        #print(liste)
        if joueur1flag:
            print('Tour de '+ joueur1 + ':')
        else:
            print('Tour de' + joueur2+':')
        
        questions= 'Choisis le sujet:'
        questions2= 'Choisis le verbe:'
        questions3= 'Choisis le complement:'
        questions4= 'Choisis la liaison:'
        questions5= 'Choisis l\'exclamation finale:'
        listeRep=[]
        #print(questions)
        #print('Reponse:')
        
        reponse= False
        reponse2= False
        reponse3= False
        reponse4= False
        reponse5= False
        while not reponse:
            print(questions)
            print(liste)
            print('Reponse:')
            answersUser = input()
            for words in liste:
                if words== answersUser:
                    listeRep.append(words)
                    print('oui')
                    reponse= True
                else:
                    continue
        print(listeRep)
        while not reponse2:
            print(liste2)
            print(questions2)
            print('Reponse:')
            answersUser = input()
            for words in liste2:
                if words== answersUser:
                    listeRep.append(words)
                    print('oui')
                    reponse2= True
                else:
                    continue
        print(listeRep)
        while not reponse3:
            print(liste3)
            print(questions3)
            print('Reponse:')
            answersUser = input()
            for words in liste3:
                if words== answersUser:
                    listeRep.append(words)
                    print('oui')
                    reponse3= True
                else:
                    continue
        print(listeRep)
        while not reponse4:
            print(liste4)
            print(questions4)
            print('Reponse:')
            answersUser = input()
            for words in liste4:
                if words== answersUser:
                    listeRep.append(words)
                    print('oui')
                    reponse4= True
                else:
                    continue
        print(listeRep)
        while not reponse5:
            print(liste5)
            print(questions5)
            print('Reponse:')
            answersUser = input()
            for words in liste5:
                if words== answersUser:
                    listeRep.append(words)
                    print('oui')
                    reponse5= True
                else:
                    continue
        print(listeRep)
        return listeRep
    strengthJoueur1= strength(joueur1)
    strengthJoueur2= strength(joueur2)
    while not gameover:
        while joueur1flag:
            sujetListe =recupOneindice(sujet)
            exclaListe=recupOneindice(Exclamationsfinales)
            compListe=recupOneindice(Complément)
            liaisonListe=recupOneindice(Liaisons)
            verbListe=recupOneindiceVerbs(listVerbs)
            JoueurChoix=chooseWords( sujetListe,verbListe,compListe,liaisonListe,exclaListe,joueur1flag)
            strengthJoueur1= strength(joueur1)
            TotalDegat= 0
            for choix in JoueurChoix:
                pointsbyWords= random.randint(strengthJoueur1[0],strengthJoueur1[1])
                TotalDegat+= pointsbyWords
            print(TotalDegat)
            TotalDegat= luck(joueur1,TotalDegat)
            print(TotalDegat)
            joueur1flag= False
            enemy_health-= TotalDegat
            print(enemy_health)
            joueur2flag=True
            if enemy_health<=0:
                print('le perdant est ' + joueur2)
                gameover=True
                joueur2flag= False
        while joueur2flag:
            sujetListe =recupOneindice(sujet)
            exclaListe=recupOneindice(Exclamationsfinales)
            compListe=recupOneindice(Complément)
            liaisonListe=recupOneindice(Liaisons)
            verbListe=recupOneindiceVerbs(listVerbs)
            TotalDegatEnemy=0
            Joueur2Choix=chooseWords( sujetListe,verbListe,compListe,liaisonListe,exclaListe,joueur1flag)
            for choix in Joueur2Choix:
                pointsbyWords= random.randint(strengthJoueur2[0],strengthJoueur2[1])
                TotalDegatEnemy+= pointsbyWords
            print(TotalDegatEnemy)
            TotalDegatEnemy= luck(joueur2,TotalDegatEnemy)
            print(TotalDegatEnemy)
            player_health-=TotalDegatEnemy
            print(player_health)
            joueur2flag=False
            joueur1flag= True
            if player_health <= 0:
                print('le perdant est ' + joueur1)
                gameover=True
        
#combatWords(Player1.name,Player2.name)
click = False
mx, my = pygame.mouse.get_pos()
def main_menu():
    click = False
    while True:
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
def displayChoiceChar(listchar,x,y):
    for i in listchar:
        Char = myFont.render(i,True,YELLOW)
        screen.blit(Char,(x,y))
        y-= 50
def health_bars(player_health,enemy_health,screenchoice):
    if player_health > 75:
        player_health_color=Green
    elif player_health>50:
        player_health_color= YELLOW
    else:
        player_health_color = RED

    if enemy_health > 75:
        enemy_health_color=Green
    elif enemy_health>50:
        enemy_health_color= YELLOW
    else:
        enemy_health_color = RED
    playerdouble= player_health*2
    enemydouble= enemy_health*2
    pygame.draw.rect(screenchoice,player_health_color,(20,50,playerdouble,25))
    pygame.draw.rect(screenchoice,enemy_health_color,(580,50,enemydouble,25))
def button(screen,text,x,y):
    color = RED
    textSurf, textRect = text_objects(text, myFont)
    textRect.center = ( (leftRect+(widthRect/2)), (topRect+(heightRect/2)) )
    rectButton.left= x
    rectButton.top= y
    pygame.draw.rect(screen, color, rectButton)
    screen.blit(textSurf, (x,y))
def ButtonVerbs(screen,text,x,y):
    color = Green
    textSurf, textRect = text_objectsVerbs(text, myFont)
    textRect.center = ( (leftRectVerbs+(widthRectVerbs/2)), (topRectVerbs+(heightRectVerbs/2)) )
    rectButtonVerbs.left= x
    rectButtonVerbs.top= y
    pygame.draw.rect(screen, color, rectButtonVerbs)
    screen.blit(textSurf, (x,y))
    return rectButtonVerbs
def displayimage(image,x,y,screen):
    screen.blit(image, (x,y))
def game():
    screenGame = pygame.display.set_mode((Width,Height))
    click=False
    player_pos=[400,300]
    running = True
    choiceplayer=''
    choiceenemy=''
    global joueur
    def chooseEnemy():
        global joueur
        clickenemy=False
        runningEnemy = True
        screenGame = pygame.display.set_mode((Width,Height))
        GameplayerChoice=enemy_choice(Playercopy,choiceplayer)
        #print(GameplayerChoice)
        def Combat():
            screenGame = pygame.display.set_mode((Width,Height))
            
            runningCombat = True
            SarahImg = pygame.image.load('sarah.png')
            SarahImg=pygame.transform.scale(SarahImg,(270,270))
            xSarah =  [0,550]
            ySarah = 80
            xItachi=[0,550]
            yItachi=80
            itachiImg= pygame.image.load('itachi.png')
            itachiImg=pygame.transform.scale(itachiImg,(270,270))
            xLucas=[0,550]
            yLucas=80
            lucasImg= pygame.image.load('lucas.png')
            lucasImg=pygame.transform.scale(lucasImg,(200,270))
            xMax=[20,550]
            yMax=80
            maxImg= pygame.image.load('max.png')
            maxImg=pygame.transform.scale(maxImg,(180,260))
            xPeter=[0,550]
            yPeter=100
            peterImg= pygame.image.load('peter.png')
            peterImg=pygame.transform.scale(peterImg,(220,250))
            Joueur1array=[]
            click = False
            while runningCombat:
                screen.fill(BACKGROUND_COLOR)      
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            runningCombat = False
                        if event.key == K_RETURN:
                            combatWords(choiceplayer,choiceenemy)
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            
                health_bars(player_health,enemy_health,screenGame)
                draw_text('Combat', font, (255, 255, 255), screen, 20, 20)
                #combatWords(choiceplayer,choiceenemy)           
                if choiceplayer== "Itachi":
                    displayimage(itachiImg,xItachi[0],yItachi,screenGame)
                if choiceplayer== "Peter":
                    displayimage(peterImg,xPeter[0],yPeter,screenGame)
                if choiceplayer== "Lucas":
                    displayimage(lucasImg,xLucas[0],yLucas,screenGame)
                if choiceplayer== "Max":
                    displayimage(maxImg,xMax[0],yMax,screenGame)
                if choiceplayer== "Sarah":
                    displayimage(SarahImg,xSarah[0],ySarah,screenGame)
                if choiceenemy== "Itachi":
                    displayimage(itachienemyImg,xItachi[1],yItachi,screenGame)
                if choiceenemy== "Peter":
                    displayimage(peterenemyImg,xPeter[1],yPeter,screenGame)
                if choiceenemy== "Lucas":
                    displayimage(lucasenemyImg,xLucas[1],yLucas,screenGame)
                if choiceenemy== "Max":
                    displayimage(maxenemyImg,xMax[1],yMax,screenGame)
                if choiceenemy== "Sarah":
                    displayimage(SarahenemyImg,xSarah[1],ySarah,screenGame)
                draw_text('Joueur 1: Press Enter', font, (255, 255, 255), screen, 20, 400)
                
                pygame.display.update()
                
                mainClock.tick(60)
        while runningEnemy:
            mx, my = pygame.mouse.get_pos()
            ButtonEnemy1= button(screenGame,GameplayerChoice[0],testx,testy)
            ButtonEnemy2=button(screenGame,GameplayerChoice[1],testx,testy+ 70)
            ButtonEnemy3=button(screenGame,GameplayerChoice[2],testx,testy+ 140)
            ButtonEnemy4=button(screenGame,GameplayerChoice[3],testx,testy+ 210)
            ButtonChar1Enemy = pygame.Rect(testx, testy, 200, 50)
            ButtonChar2Enemy = pygame.Rect(testx, testy+70, 200, 50)
            ButtonChar3Enemy = pygame.Rect(testx, testy+140, 200, 50)
            ButtonChar4Enemy = pygame.Rect(testx, testy+210, 200, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        runningEnemy = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clickenemy = True
            if ButtonChar1Enemy.collidepoint((mx, my)):
                if clickenemy:
                    choiceenemy= GameplayerChoice[0]
                    #print(joueur)
                    Combat()
            if ButtonChar2Enemy.collidepoint((mx, my)):
                if clickenemy:
                    choiceenemy= GameplayerChoice[1]
                    #print(joueur)
                    Combat()
            if ButtonChar3Enemy.collidepoint((mx, my)):
                if clickenemy:
                    choiceenemy= GameplayerChoice[2]
                    #print(joueur)
                    Combat()
            if ButtonChar4Enemy.collidepoint((mx, my)):
                if clickenemy:
                    choiceenemy= GameplayerChoice[3]
                    Combat()
            
            draw_text('Choose player two', font, (255, 255, 255), screen, 20, 20)
            pygame.display.update()
        
    while running:
        PlayerArray2=PlayerArray
        mx, my = pygame.mouse.get_pos()
        flagButton= False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

                
        screenGame.fill(BACKGROUND_COLOR)
        text = "Score: "+ str(score)
        label = myFont.render(text,1,YELLOW)
        screenGame.blit(label,(Width-200,Height-40))
        ButtonChar1= button(screenGame,PlayerArray[0],testx,testy)
        ButtonChar2=button(screenGame,PlayerArray[1],testx,testy+ 70)
        ButtonChar3=button(screenGame,PlayerArray[2],testx,testy+ 140)
        ButtonChar4=button(screenGame,PlayerArray[3],testx,testy+ 210)
        ButtonChar5=button(screenGame,PlayerArray[4],testx,testy+ 280)
        buttonArray= [ButtonChar1,ButtonChar2,ButtonChar3,ButtonChar4,ButtonChar5]
        ButtonChar1bis = pygame.Rect(testx, testy, 200, 50)
        ButtonChar2bis = pygame.Rect(testx, testy+70, 200, 50)
        ButtonChar3bis = pygame.Rect(testx, testy+140, 200, 50)
        ButtonChar4bis = pygame.Rect(testx, testy+210, 200, 50)
        ButtonChar5bis = pygame.Rect(testx, testy+280, 200, 50)
        if ButtonChar1bis.collidepoint((mx, my)):
            #print('oui')
            if click:
                #joueur+= PlayerArray[0]
                #print(joueur)
                choiceplayer=PlayerArray[0]
                chooseEnemy()
        if ButtonChar2bis.collidepoint((mx, my)):
            #print('oui')
            if click:
                #joueur+= PlayerArray[1]
                choiceplayer=PlayerArray[1]
                #print(joueur)
                chooseEnemy()
        if ButtonChar3bis.collidepoint((mx, my)):
            #print('oui')
            #print('oui')
            if click:
                #joueur+= PlayerArray[2]
                #print(joueur)
                choiceplayer=PlayerArray[2]
                chooseEnemy()
        
        if ButtonChar4bis.collidepoint((mx, my)):
            #print('oui')
            if click:
                #joueur+= PlayerArray[3]
                #print(joueur)
                choiceplayer=PlayerArray[3]
                chooseEnemy()
        if ButtonChar5bis.collidepoint((mx, my)):
            if click:
                #joueur+= PlayerArray[4]
                choiceplayer=PlayerArray[4]
                print(choiceplayer)
                chooseEnemy()
        

        #displayWords(testx,testy)
        #displayChoiceChar(PlayerArray,testx,testy)
        #pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
        draw_text('game', font, (255, 255, 255), screen, 20, 20)    
        pygame.display.update()
        mainClock.tick(60)
        
    
   
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
main_menu()

