import pygame, sys
from pygame.locals import *
import random

rectangles=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
shapesarrangement=[]

Rectangle1=Rect(0,0,100,100)
Rectangle2=Rect(100,0,100,100)
Rectangle3=Rect(200,0,100,100)
Rectangle4=Rect(300,0,100,100)
Rectangle5=Rect(0,100,100,100)
Rectangle6=Rect(100,100,100,100)
Rectangle7=Rect(200,100,100,100)
Rectangle8=Rect(300,100,100,100)
Rectangle9=Rect(0,200,100,100)
Rectangle10=Rect(100,200,100,100)
Rectangle11=Rect(200,200,100,100)
Rectangle12=Rect(300,200,100,100)
Rectangle13=Rect(0,300,100,100)
Rectangle14=Rect(100,300,100,100)
Rectangle15=Rect(200,300,100,100)
Rectangle16=Rect(300,300,100,100)

RectangleObjects=(Rectangle1,Rectangle2,Rectangle3,Rectangle4,Rectangle5,Rectangle6,Rectangle7,Rectangle8,Rectangle9,Rectangle10,Rectangle11,Rectangle12,Rectangle13,Rectangle14,Rectangle15,Rectangle16)


def drawBackground():
    Window.fill((255,255,255))
    for Rectangle in RectangleObjects:
        pygame.draw.rect(Window,(255,0,0),Rectangle,10)

def drawCircleshape(x,color):
    if x==1:
        pygame.draw.circle(Window,color,(50,50),30)
    elif x==2:
        pygame.draw.circle(Window,color,(150,50),30)
    elif x==3:
        pygame.draw.circle(Window,color,(250,50),30)
    elif x==4:
        pygame.draw.circle(Window,color,(350,50),30)
    elif x==5:
        pygame.draw.circle(Window,color,(50,150),30)
    elif x==6:
        pygame.draw.circle(Window,color,(150,150),30)
    elif x==7:
        pygame.draw.circle(Window,color,(250,150),30)
    elif x==8:
        pygame.draw.circle(Window,color,(350,150),30)
    elif x==9:
        pygame.draw.circle(Window,color,(50,250),30)
    elif x==10:
        pygame.draw.circle(Window,color,(150,250),30)
    elif x==11:
        pygame.draw.circle(Window,color,(250,250),30)
    elif x==12:
        pygame.draw.circle(Window,color,(350,250),30)
    elif x==13:
        pygame.draw.circle(Window,color,(50,350),30)
    elif x==14:
        pygame.draw.circle(Window,color,(150,350),30)
    elif x==15:
        pygame.draw.circle(Window,color,(250,350),30)
    elif x==16:
        pygame.draw.circle(Window,color,(350,350),30)
        
def drawRectangleshape(x,color):
    if x==1:
        pygame.draw.rect(Window,color,(20,20,60,60))
    elif x==2:
        pygame.draw.rect(Window,color,(120,20,60,60))
    elif x==3:
        pygame.draw.rect(Window,color,(220,20,60,60))
    elif x==4:
        pygame.draw.rect(Window,color,(320,20,60,60))
    elif x==5:
        pygame.draw.rect(Window,color,(20,120,60,60))
    elif x==6:
        pygame.draw.rect(Window,color,(120,120,60,60))
    elif x==7:
        pygame.draw.rect(Window,color,(220,120,60,60))
    elif x==8:
        pygame.draw.rect(Window,color,(320,120,60,60))
    elif x==9:
        pygame.draw.rect(Window,color,(20,220,60,60))
    elif x==10:
        pygame.draw.rect(Window,color,(120,220,60,60))
    elif x==11:
        pygame.draw.rect(Window,color,(220,220,60,60))
    elif x==12:
        pygame.draw.rect(Window,color,(320,220,60,60))
    elif x==13:
        pygame.draw.rect(Window,color,(20,320,60,60))
    elif x==14:
        pygame.draw.rect(Window,color,(120,320,60,60))
    elif x==15:
        pygame.draw.rect(Window,color,(220,320,60,60))
    elif x==16:
        pygame.draw.rect(Window,color,(320,320,60,60))
        
def drawTriangleshape(x,color):
    if x==1:
        pygame.draw.polygon(Window,color,((20,20),(80,20),(50,80)))
    elif x==2:
        pygame.draw.polygon(Window,color,((120,20),(180,20),(150,80)))
    elif x==3:
        pygame.draw.polygon(Window,color,((220,20),(280,20),(250,80)))
    elif x==4:
        pygame.draw.polygon(Window,color,((320,20),(380,20),(350,80)))
    elif x==5:
        pygame.draw.polygon(Window,color,((20,120),(80,120),(50,180)))
    elif x==6:
        pygame.draw.polygon(Window,color,((120,120),(180,120),(150,180)))
    elif x==7:
        pygame.draw.polygon(Window,color,((220,120),(280,120),(250,180)))
    elif x==8:
        pygame.draw.polygon(Window,color,((320,120),(380,120),(350,180)))
    elif x==9:
        pygame.draw.polygon(Window,color,((20,220),(80,220),(50,280)))
    elif x==10:
        pygame.draw.polygon(Window,color,((120,220),(180,220),(150,280)))
    elif x==11:
        pygame.draw.polygon(Window,color,((220,220),(280,220),(250,280)))
    elif x==12:
        pygame.draw.polygon(Window,color,((320,220),(380,220),(350,280)))
    elif x==13:
        pygame.draw.polygon(Window,color,((20,320),(80,320),(50,380)))
    elif x==14:
        pygame.draw.polygon(Window,color,((120,320),(180,320),(150,380)))
    elif x==15:
        pygame.draw.polygon(Window,color,((220,320),(280,320),(250,380)))
    elif x==16:
        pygame.draw.polygon(Window,color,((320,320),(380,320),(350,380)))
        
def drawDiamondshape(x,color):
    if x==1:
        pygame.draw.polygon(Window,color,((50,20),(80,50),(50,80),(20,50)))
    elif x==2:
        pygame.draw.polygon(Window,color,((150,20),(180,50),(150,80),(120,50)))
    elif x==3:
        pygame.draw.polygon(Window,color,((250,20),(280,50),(250,80),(220,50)))
    elif x==4:
        pygame.draw.polygon(Window,color,((350,20),(380,50),(350,80),(320,50)))
    elif x==5:
        pygame.draw.polygon(Window,color,((50,120),(80,150),(50,180),(20,150)))
    elif x==6:
        pygame.draw.polygon(Window,color,((150,120),(180,150),(150,180),(120,150)))
    elif x==7:
        pygame.draw.polygon(Window,color,((250,120),(280,150),(250,180),(220,150)))
    elif x==8:
        pygame.draw.polygon(Window,color,((350,120),(380,150),(350,180),(320,150)))
    elif x==9:
        pygame.draw.polygon(Window,color,((50,220),(80,250),(50,280),(20,250)))
    elif x==10:
        pygame.draw.polygon(Window,color,((150,220),(180,250),(150,280),(120,250)))
    elif x==11:
        pygame.draw.polygon(Window,color,((250,220),(280,250),(250,280),(220,250)))
    elif x==12:
        pygame.draw.polygon(Window,color,((350,220),(380,250),(350,280),(320,250)))
    elif x==13:
        pygame.draw.polygon(Window,color,((50,320),(80,350),(50,380),(20,350)))
    elif x==14:
        pygame.draw.polygon(Window,color,((150,320),(180,350),(150,380),(120,350)))
    elif x==15:
        pygame.draw.polygon(Window,color,((250,320),(280,350),(250,380),(220,350)))
    elif x==16:
        pygame.draw.polygon(Window,color,((350,320),(380,350),(350,380),(320,350)))


def startGame():
    for i in range(4):
        if i==0 or i==1:
            color=(0,0,255)
        else:
            color=(0,255,0)
        x=random.choice(rectangles)
        shapesarrangement.append(x)
        drawRectangleshape(x,color)
        rectangles.remove(x)
    
    for i in range(4):
        if i==0 or i==1:
            color=(255,255,0)
        else:
            color=(0,255,255)
        x=random.choice(rectangles)
        shapesarrangement.append(x)
        drawCircleshape(x,color)
        rectangles.remove(x)
    
    for i in range(4):
        if i==0 or i==1:
            color=(255,0,255)
        else:
            color=(128,0,0)
        x=random.choice(rectangles)
        shapesarrangement.append(x)
        drawTriangleshape(x,color)
        rectangles.remove(x)
        
    for i in range(4):
        if i==0 or i==1:
            color=(128,128,0)
        else:
            color=(128,0,128)
        x=random.choice(rectangles)
        shapesarrangement.append(x)
        drawDiamondshape(x,color)
        rectangles.remove(x)
 
def rightchoice(firstchoice,secondchoice):
    x=shapeIndex(firstchoice)
    y=shapeIndex(secondchoice)
    if(x==0 and y==1 or x==1 and y==0)\
        or (x==2 and y==3 or x==3 and y==2)\
        or (x==4 and y==5 or x==5 and y==4)\
        or (x==6 and y==7 or x==7 and y==6)\
        or (x==8 and y==9 or x==9 and y==8)\
        or (x==10 and y==11 or x==11 and y==10)\
        or (x==12 and y==13 or x==13 and y==12)\
        or (x==14 and y==15 or x==15 and y==14):
            return True

def shapeIndex(mouse_position):
    for i in range(16):
        if RectangleObjects[i].collidepoint(mouse_position):
            return shapesarrangement.index(i+1)
        
def recNumber(mouse_position):
    for i in range(16):
        if RectangleObjects[i].collidepoint(mouse_position):
            return i+1

def hide(mouse_position):
    rectanglenumber=recNumber(mouse_position)
    for i in range(16):
        if rectanglenumber==i+1:
            pygame.draw.rect(Window,(255,255,255),RectangleObjects[i].inflate(-10,-10))

def show(mouse_position):
    rectanglenumber=recNumber(mouse_position)
    shapeindex=shapeIndex(mouse_position)
    if shapeindex==0 or shapeindex==1:
        color=(0,0,255)
        drawRectangleshape(rectanglenumber,color)
    elif shapeindex==2 or shapeindex==3:
        color=(0,255,0)
        drawRectangleshape(rectanglenumber,color)
    elif shapeindex==4 or shapeindex==5:
        color=(255,255,0)
        drawCircleshape(rectanglenumber,color)
    elif shapeindex==6 or shapeindex==7:
        color=(0,255,255)
        drawCircleshape(rectanglenumber,color)
    elif shapeindex==8 or shapeindex==9:
        color=(255,0,255)
        drawTriangleshape(rectanglenumber,color)
    elif shapeindex==10 or shapeindex==11:
        color=(128,0,0)
        drawTriangleshape(rectanglenumber,color)
    elif shapeindex==12 or shapeindex==13:
        color=(128,128,0)
        drawDiamondshape(rectanglenumber,color)
    elif shapeindex==14 or shapeindex==15:
        color=(128,0,128)
        drawDiamondshape(rectanglenumber,color)
        
                 

def main():
    pygame.init()
    global Window
    Window = pygame.display.set_mode((410,410))
    Window.fill((255,255,255))
    pygame.display.set_caption("Test Game")

    drawBackground()
    startGame()
    # pygame.draw.circle(Window,(255,255,0),(50,50),30)
    # pygame.draw.polygon(Window,(0,255,0),((120,20),(180,20),(150,80)))
    # pygame.draw.polygon(Window,(0,0,255),((250,20),(280,50),(250,80),(220,50)))
    # pygame.draw.rect(Window,(128,0,0),(320,20,60,60))
    # for i in range(1,17):
    #     drawDiamondshape(i,(255,255,0))
    pygame.display.update()
    pygame.time.wait(3000)
    Window.fill((255,255,255))
    drawBackground()
    pygame.display.update()
    flag=0
    truechoices=[]
    
    
    
    

    while True:
        for event in pygame.event.get():
            # if event.type==MOUSEBUTTONUP:
            #     print("Mouse button is Clicked.")

            # if event.type==KEYUP:
            #     print("Keyboard button is Pressed.")

            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_position=pygame.mouse.get_pos()
                show(mouse_position)
                pygame.display.update()
                if flag==0:
                    firstchoice=mouse_position
                    if recNumber(firstchoice) in truechoices: flag=0
                    else: flag=1
                else:
                    secondchoice=mouse_position
                    if recNumber(secondchoice) in truechoices: flag=1
                    else: flag=0
                    if not (recNumber(firstchoice) in truechoices) and not (recNumber(secondchoice) in truechoices):
                        if rightchoice(firstchoice,secondchoice):
                            truechoices.append(recNumber(firstchoice))
                            truechoices.append(recNumber(secondchoice))
                        else:
                            pygame.time.wait(1000)
                            hide(firstchoice)
                            hide(secondchoice)
                            pygame.display.update()
        
        if len(truechoices) == 16:
            myfont = pygame.font.SysFont('Comic Sans MS',60,True)
            textsurface = myfont.render('You did it!', False, (0, 0, 0))
            Window.blit(textsurface,(20,150))
            image = pygame.image.load('won.png')
            Window.blit(image, (10, 10))
            pygame.display.update()

                    

                


if __name__=="__main__":
    main()
