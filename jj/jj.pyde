r= 30
a=870
p=270
f= 515
t= 600
img1=0
bg = 0
img=0
x=350
def setup():
    global img, img1,p,f,a,p
    size(1000,700)
    img1 = loadImage("map.jpg")
    img = loadImage("map.jpg")
    






def draw():
    global img,x,r,img1,p,t,f,a,p
    
    
    # image(img1, 0, 0,1000,700)
 

    image(img, 0, 0,1000,700)
    
    
    
    fill(0,255,255)
    rect(x,130,  30,30)#гренландия
    fill(255,0,255)
    rect(r,230,  30,30)#карта
    fill(255,255,0)
    rect(t,230,  30,30)#казахстан yellow
    fill(201,229,211)
    rect(f,535,  30,30)#порт-елизабет
    fill(100,47,129)
    rect(a,560, 30,30)#australia
    fill(255,118,171)
    rect(p,600, 30,30)#патагония
    print(mouseX, mouseY)
    fill(255,255,255)
    textSize(90)
    text(u'карта', 410,70)
    textSize(30)
    text(u'выход', 16,221)


def mouseClicked():
    global bg, img,x,r,img1,p,t,f,a,p
    if mouseX > 350 and mouseX < 380 and mouseY > 130 and mouseY < 160 and mouseY:
        img = loadImage("nuuk-vestgronland-greenland.jpg")
        x=-89
        t=-87
        r=30
        f=-39
        a=-134
        p=-66
    if mouseX > 30 and mouseX < 60 and mouseY > 230 and mouseY < 260 and mouseY:
        img = loadImage("map.jpg")
        x=350
        r=0
        t=600
        f=515
        a=870
        p=270
    if mouseX > 600 and mouseX < 630 and mouseY > 230 and mouseY < 260 and mouseY:
        img = loadImage("scale_1200.jpg")
        x=-89
        r=30
        t=-87
        f=-39
        a=-134
        p=-66
    if mouseX > 30 and mouseX < 60 and mouseY > 230 and mouseY < 260 and mouseY:
        img = loadImage("map.jpg")
        x=350
        r=0
        t=600
        f=515
        a=870
        p=270
    if mouseX > 515 and mouseX < 545 and mouseY > 535 and mouseY < 565 and mouseY:
        img = loadImage("africa.jpg")
        x=-89
        r=30
        t=-87
        f=-39
        a=-134
        p=-66
    if mouseX > 30 and mouseX < 60 and mouseY > 230 and mouseY < 260 and mouseY:
        img = loadImage("map.jpg")
        x=350
        r=0
        t=600
        f=515
        a=870
        p=270
    if mouseX > 870 and mouseX < 900 and mouseY > 560 and mouseY < 590 and mouseY:
        img = loadImage("australia (2).jpg")
        x=-89
        r=30
        t=-87
        f=-39
        a=-76
        p=-66
    if mouseX > 30 and mouseX < 60 and mouseY > 230 and mouseY < 260 and mouseY:
        img = loadImage("map.jpg")
        x=350
        r=0
        t=600
        f=515
        a=870
        p=270
    if mouseX > 270 and mouseX < 300 and mouseY > 600 and mouseY < 630 and mouseY:
            img = loadImage("patagonia.jpg")
            x=-89
            r=30
            t=-87
            f=-39
            a=-76 
            p=-66
