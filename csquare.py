import pygame
pygame.init()

wn=pygame.display.set_mode((700,700))
font = pygame.font.Font("freesansbold.ttf", 32)
white=(255,255,255)
red=(255,0,0)
orange=(255,140,0)

#######################################################################################################################################################################

sqlist=[]
class Square:
    def __init__(self, sq_id, image):
        self.n=sq_id
        self.img=pygame.image.load(image)
        sqlist.append(self)
        self.piece=0
        if True:
            xa=self.n//8
            self.x=(xa*86)+6

            ya=self.n%8
            self.y=(ya*86)+6

            wn.blit(self.img, (self.x,self.y))

        self.xbound=[self.x, self.x+86]
        self.ybound=[self.y, self.y+86]

    def isinbounds(self, x, y):
        if x>=self.xbound[0] and x<=self.xbound[1] and y>=self.ybound[0] and y<=self.ybound[1]:
            yea=True
        else:
            yea=False
        return yea
    
    
    def refresh(self):
        wn.blit(self.img, (self.x,self.y))
        if self.piece:
            if True:
                if self.piece==1:
                    ovr=pygame.image.load("hope/w_p.png")
                elif self.piece==2:
                    ovr=pygame.image.load("hope/w_b.png")
                elif self.piece==3:
                    ovr=pygame.image.load("hope/w_n.png")
                elif self.piece==4:
                    ovr=pygame.image.load("hope/w_r.png")
                elif self.piece==5:
                    ovr=pygame.image.load("hope/w_q.png")
                elif self.piece==6:
                    ovr=pygame.image.load("hope/w_k.png")
                elif self.piece==7:
                    ovr=pygame.image.load("hope/b_p.png")
                elif self.piece==8:
                    ovr=pygame.image.load("hope/b_b.png")
                elif self.piece==9:
                    ovr=pygame.image.load("hope/b_n.png")
                elif self.piece==10:
                    ovr=pygame.image.load("hope/b_r.png")
                elif self.piece==11:
                    ovr=pygame.image.load("hope/b_q.png")
                elif self.piece==12:
                    ovr=pygame.image.load("hope/b_k.png")

                wn.blit(ovr, (self.x,self.y))

def locatesq(x):
    bang=False
    for i in sqlist:
        if i.n==x:
            bang=i
    return bang

def locatepi(x):
    bang=False
    for i in plist:
        if i.onSquare==x:
            bang=i
    return bang

plist=[]

#######################################################################################################################################################################

class pawn():
    def __init__(self, team, onSquare):
        self.team=team
        self.onSquare=onSquare
        self.type=(team*6)-5
        plist.append(self)
        locatesq(self.onSquare).piece=self.type
        self.calc=((-1)**team)
        self.hasMoved=0

    def rank(self):
        rank=9-(self.onSquare%8 + 1)
        return rank
    
    def generate_move(self):
        movelist=[]
        posmove=self.onSquare+self.calc
        if self.hasMoved==0 and self.team==2:
            if locatesq(posmove).piece==0:
                posmove+=1
                if locatesq(posmove).piece==0:
                    movelist.append(posmove)
        posmove=self.onSquare+self.calc
        if self.hasMoved==0 and self.team==1:
            if locatesq(posmove).piece==0:
                posmove-=1
                if locatesq(posmove).piece==0:
                    movelist.append(posmove)

        posmove=self.onSquare+self.calc
        if locatesq(posmove):
            if locatesq(posmove).piece==0:
                movelist.append(posmove)
        posmove+=8
        if posmove<64:
            if locatesq(posmove).piece:
                if locatepi(posmove).team!=self.team:
                    movelist.append(posmove)
        posmove-=16
        if posmove>=0:
            if locatesq(posmove).piece:
                if locatepi(posmove).team!=self.team:
                    movelist.append(posmove)
        if (self.team==1 and self.rank()==5) or (self.team==2 and self.rank()==4):
            j=[8,-8]
            for cxd in j:
                if locatesq(self.onSquare+cxd):
                    if locatesq(self.onSquare+cxd).piece:
                        if (locatepi(self.onSquare+cxd).type==(self.type+6)) or (locatepi(self.onSquare+cxd).type==(self.type-6)):
                            if locatepi(self.onSquare+cxd).hasMoved==1:
                                babudi=self.onSquare+cxd+self.calc
                                movelist.append(babudi)
                                
        return movelist

    def move(self, squar):
        if locatesq(squar).piece:
            locatepi(squar).onSquare=64
        else:
            if locatesq(squar-self.calc).piece:
                if locatepi(squar-self.calc).team != self.team:
                    locatepi(squar-self.calc).onSquare=64
                    locatesq(squar-self.calc).piece=0
        old=self.onSquare
        self.onSquare=squar
        locatesq(squar).piece=self.type
        locatesq(old).piece=0
        if self.hasMoved==0:
            self.hasMoved=3
        if self.rank()==1 or self.rank()==8:
            hagg=queen(self.team, self.onSquare)
            self.onSquare=64


#######################################################################################################################################################################

class knight:
    def __init__(self, team, onSquare):
        self.team=team
        self.onSquare=onSquare
        self.type=(team*6)-3
        plist.append(self)
        locatesq(self.onSquare).piece=self.type
        self.hasMoved=0

    def generate_move(self):
        movelist=[]
        a=[7,6]
        b=[0,1]
        c=[7]
        d=[0]
        posmoves=[[self.onSquare+6, a], [self.onSquare+15, c], [self.onSquare+17, d], [self.onSquare+10, b], [self.onSquare-6, b], [self.onSquare-15, d], [self.onSquare-17, c], [self.onSquare-10, a]]
        for posmove in posmoves:
            if locatesq(posmove[0]):
                tru_dat=True
                for cond in posmove[1]:
                    if posmove[0]%8==cond:
                        tru_dat=False
                if tru_dat:
                    if locatesq(posmove[0]).piece==0:
                        movelist.append(posmove[0])
                    elif locatepi(posmove[0]).team != self.team:
                        movelist.append(posmove[0])
        return movelist

    def move(self, squar):
        if locatesq(squar).piece:
            locatepi(squar).onSquare=64
        old=self.onSquare
        self.onSquare=squar
        locatesq(squar).piece=self.type
        locatesq(old).piece=0
        
#######################################################################################################################################################################

class king:
    def __init__(self, team, onSquare):
        self.onSquare=onSquare
        self.team=team
        self.type=(team*6)
        plist.append(self)
        locatesq(self.onSquare).piece=self.type
        self.hasMoved=0

    def is_in_check(self):
        moves=[]
        for pie in plist:
            if pie.team != self.team:
                if pie.onSquare < 64:
                    for nom in pie.generate_move():
                        moves.append(nom)
        moves = list(set(moves))
        chk=False
        for i in moves:
            if i==self.onSquare:
                chk=True
        return chk

    def is_attacked(self):
        moves=[]
        for pie in plist:
            if pie.team != self.team and pie.type != 6 and pie.type != 12:
                if pie.onSquare < 64:
                    for nom in pie.generate_move():
                        moves.append(nom)
        moves = list(set(moves))
        chk=False
        for i in moves:
            if i==self.onSquare:
                chk=True
        return chk

    def generate_move(self):
        movelist=[]
        posmoves=[[self.onSquare+1, 0], [self.onSquare+9, 0], [self.onSquare+8 , 8], [self.onSquare+7, 7], [self.onSquare-1, 7], [self.onSquare-8, 8], [self.onSquare-7, 0], [self.onSquare-9, 7]]
        for posmove in posmoves:
            if locatesq(posmove[0]):
                if posmove[0]%8 != posmove[1]: 
                    if locatesq(posmove[0]).piece==0:
                        movelist.append(posmove[0])
                    elif locatepi(posmove[0]).team != self.team:
                        movelist.append(posmove[0])

        if self.hasMoved==0 and not(self.is_attacked()):
            if locatesq(self.onSquare+24).piece==(self.type-2) and locatesq(self.onSquare+16).piece==0 and locatesq(self.onSquare+8).piece==0:
                if locatepi(self.onSquare+24).hasMoved==0:
                    self.onSquare+=8
                    if not(self.is_attacked()):
                        movelist.append(self.onSquare+8)
                    self.onSquare-=8
            if locatesq(self.onSquare-32).piece==(self.type-2) and locatesq(self.onSquare-16).piece==0 and locatesq(self.onSquare-8).piece==0 and locatesq(self.onSquare-24).piece==0:
                if locatepi(self.onSquare-32).hasMoved==0:
                    self.onSquare-=8
                    if not(self.is_attacked()):
                        movelist.append(self.onSquare-8)
                    self.onSquare+=8
        return movelist
        
    def move(self, squar):
        if self.onSquare-squar==16:
            old=self.onSquare
            self.onSquare=squar
            locatesq(squar).piece=self.type
            locatesq(old).piece=0                    
            if self.hasMoved==0:
                self.hasMoved=3
            locatesq(self.onSquare-16).piece=0
            locatepi(self.onSquare-16).onSquare=self.onSquare+8
            locatesq(self.onSquare+8).piece=locatepi(self.onSquare+8).type
            locatepi(self.onSquare+8).hasMoved=3
        elif self.onSquare-squar==-16:
            old=self.onSquare
            self.onSquare=squar
            locatesq(squar).piece=self.type
            locatesq(old).piece=0                    
            if self.hasMoved==0:
                self.hasMoved=3
            locatesq(self.onSquare+8).piece=0
            locatepi(self.onSquare+8).onSquare=self.onSquare-8
            locatesq(self.onSquare-8).piece=locatepi(self.onSquare-8).type
            locatepi(self.onSquare-8).hasMoved=3

        else:            
            if locatesq(squar).piece:
                locatepi(squar).onSquare=64
            old=self.onSquare
            self.onSquare=squar
            locatesq(squar).piece=self.type
            locatesq(old).piece=0                    
            if self.hasMoved==0:
                self.hasMoved=3
        
#######################################################################################################################################################################

class rook:
    def __init__(self, team, onSquare):
        self.team=team
        self.onSquare=onSquare
        self.type=(team*6)-2
        plist.append(self)
        locatesq(self.onSquare).piece=self.type
        self.hasMoved=0

    def generate_move(self):
        movelist=[]
        posmoves=[[1, 0], [-1, 7], [8, 8], [-8, 8]]
        for posmove in posmoves:
            cal=posmove[0]
            cond=posmove[1]
            itble=self.onSquare+cal
            while True:
                if locatesq(itble):
                    if itble%8!=cond:
                        if locatesq(itble).piece==0:
                            movelist.append(itble)
                            itble+=cal
                        elif locatepi(itble).team != self.team:
                            movelist.append(itble)
                            break
                        else:
                            break
                    else:
                        break
                else:
                    break
        return movelist
                            
    def move(self, squar):
        if locatesq(squar).piece:
            locatepi(squar).onSquare=64
        old=self.onSquare
        self.onSquare=squar
        locatesq(squar).piece=self.type
        locatesq(old).piece=0
        if self.hasMoved==0:
            self.hasMoved=3
                        
#######################################################################################################################################################################

class bishop:
    def __init__(self, team, onSquare):
        self.team=team
        self.onSquare=onSquare
        self.type=(team*6)-4
        plist.append(self)
        locatesq(self.onSquare).piece=self.type
        self.hasMoved=0

    def generate_move(self):
        movelist=[]
        posmoves=[[7, 7], [-7, 0], [9, 0], [-9, 7]]
        for posmove in posmoves:
            cal=posmove[0]
            cond=posmove[1]
            itble=self.onSquare+cal
            while True:
                if locatesq(itble):
                    if itble%8!=cond:
                        if locatesq(itble).piece==0:
                            movelist.append(itble)
                            itble+=cal
                        elif locatepi(itble).team != self.team:
                            movelist.append(itble)
                            break
                        else:
                            break
                    else:
                        break
                else:
                    break
        return movelist
                            
    def move(self, squar):
        if locatesq(squar).piece:
            locatepi(squar).onSquare=64
        old=self.onSquare
        self.onSquare=squar
        locatesq(squar).piece=self.type
        locatesq(old).piece=0

#######################################################################################################################################################################

class queen:
    def __init__(self, team, onSquare):
        self.team=team
        self.onSquare=onSquare
        self.type=(team*6)-1
        plist.append(self)
        locatesq(self.onSquare).piece=self.type
        self.hasMoved=0

    def generate_move(self):
        movelist=[]
        posmoves=[[7, 7], [-7, 0], [9, 0], [-9, 7],[1, 0], [-1, 7], [8, 8], [-8, 8]]
        for posmove in posmoves:
            cal=posmove[0]
            cond=posmove[1]
            itble=self.onSquare+cal
            while True:
                if locatesq(itble):
                    if itble%8!=cond:
                        if locatesq(itble).piece==0:
                            movelist.append(itble)
                            itble+=cal
                        elif locatepi(itble).team != self.team:
                            movelist.append(itble)
                            break
                        else:
                            break
                    else:
                        break
                else:
                    break
        return movelist
                            
    def move(self, squar):
        if locatesq(squar).piece:
            locatepi(squar).onSquare=64
        old=self.onSquare
        self.onSquare=squar
        locatesq(squar).piece=self.type
        locatesq(old).piece=0
    
#######################################################################################################################################################################

def is_move_legal(piece, square):
    oldpie=0
    pee=[]
    if locatesq(square).piece:
        oldpie=locatesq(square).piece
        pee.append(locatepi(square))        
        locatepi(square).onSquare=100
    oldsq=locatepi(piece).onSquare
    

    locatesq(oldsq).piece=0
    locatepi(piece).onSquare=square
    locatesq(square).piece=locatepi(square).type
    manqin=[]
    if locatepi(square).type==1 or locatepi(square).type==7:
        gg=square-locatepi(square).calc
        if locatepi(gg):
            if locatepi(gg).type==locatepi(square).type+6 or locatepi(gg).type==locatepi(square).type-6:
                if locatepi(gg).hasMoved==1:
                    manqin.append(locatepi(gg))
                    locatepi(gg).onSquare=64
                    locatesq(gg).piece=0


    for mans in plist:
        if mans.type==(locatepi(square).team * 6):
            a = mans
    legal=not(a.is_in_check())

    for i in manqin:
        i.onSquare=gg
        locatesq(gg).piece=i.type
        
    
    locatepi(square).onSquare=oldsq
    locatesq(oldsq).piece=locatepi(oldsq).type
    locatesq(square).piece=oldpie
    for i in pee:
        i.onSquare=square

    return legal

#######################################################################################################################################################################


def check_hit(tup):
    if go_ahead:
        x = tup[0]
        y = tup[1]
        b="no"
        for i in sqlist:
            if i.isinbounds(x,y):
                b = i.n
        return b
    else:
        return "no"

def check_mate(x):
    for ki in plist:
        if ki.type == x*6:
            ck=ki
    leg=False
    for pice in plist:
        if pice.team==ck.team:
            if pice.onSquare < 64:
                for nod in pice.generate_move():
                    if is_move_legal(pice.onSquare, nod):
                        leg=True
    command=False
    if leg==False:
        if ck.is_attacked():
            command="checkmate"
        else:
            command="stalemate"
        
    return command
            

def sqgen():
    for i in range(64):
        if (i//8)%2==0:
            if i%2==0:
                fa=Square(i, "hope/w.bmp")
            else:
                fa=Square(i, "hope/g.bmp")
        else:
            if i%2==0:
                fa=Square(i, "hope/g.bmp")
            else:
                fa=Square(i, "hope/w.bmp")

def pwngen():
    for i in range(1, 58, 8):
        pwn = pawn(2, i)
    for i in range(6, 63, 8):
        pwn = pawn(1, i)

def knghtgen():
    knig=knight(2, 8)
    knig=knight(1, 15)
    knig=knight(2, 48)
    knig=knight(1, 55)

def knggen():
    kin=king(1, 39)
    kin=king(2, 32)

def rkgen():
    ruk=rook(1, 7)
    ruk=rook(2, 0)
    ruk=rook(1, 63)
    ruk=rook(2, 56)

def bshpgen():
    bish=bishop(1,23)
    bish=bishop(2,16)
    bish=bishop(1,47)
    bish=bishop(2,40)

def qngen():
    qun=queen(2, 24)
    qun=queen(1, 31)

sqgen()
pwngen()
knghtgen()
knggen()
rkgen()
bshpgen()
qngen()
pygame.display.update()

#######################################################################################################################################################################
global go_ahead
global selected
global turn
go_ahead=True
turn=1
selected=1000
def main(sqno):
    global selected
    global turn
    global go_ahead
    if selected == 1000:
        if locatesq(sqno).piece:
            if locatepi(sqno).team == turn:
                selected = sqno
    else:
        mlist = locatepi(selected).generate_move()
        sq="no"
        for i in mlist:
            if int(i) == int(sqno):
                sq = sqno
        if sq == "no":
            if locatesq(sqno).piece:
                if locatepi(sqno).team == turn:
                    selected = sqno
                else:
                    selected=1000
            else:
                selected=1000
        else:
            if is_move_legal(selected, sqno):
                locatepi(selected).move(sqno)
                for c in plist:
                    if c.hasMoved==1:
                        c.hasMoved=2
                    elif c.hasMoved==3:
                        c.hasMoved=1
                selected=1000
                if turn==1:
                    turn=2
                else:
                    turn=1

                if check_mate(turn):
                    go_ahead=False
            else:
                selected=1000
            
    for g in sqlist:
        g.refresh()
    for wd in plist:
        if wd.type==turn*6:
            cheep=wd
    if cheep.is_attacked():
        text = font.render("check", True, white, orange)
        textRect=text.get_rect()
        textRect.center=(350,350)
        wn.blit(text, textRect)        
        
    if go_ahead==False:
        text = font.render(check_mate(turn), True, white, red)
        textRect=text.get_rect()
        textRect.center=(350,350)
        wn.blit(text, textRect)
    pygame.display.update()
        

#######################################################################################################################################################################


for g in sqlist:
    g.refresh()
pygame.display.update()


loop=True
while loop:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            loop=False
        if event.type== pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            avagadro = check_hit(pos)
            if avagadro != "no":
                main(avagadro)
                


pygame.quit()
