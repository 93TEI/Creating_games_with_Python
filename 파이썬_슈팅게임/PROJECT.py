﻿import pygame, sys, math, random
from pygame.locals import *

#게임 초기 설정

pygame.init()
pygame.mixer.init()


pygame.mixer.music.load('project_resources/q.ogg')
pygame.mixer.music.play(-1)
w=1022
h=511
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('도시에 쳐들어온 이정준 잡기')
playerpos = [50,300]
bosspos = 1000
bossfire = False
FPS_CLOCK = pygame.time.Clock()
keys = [False, False, False, False]
healthvalue = 194
missiles=[]
boss_rect = pygame.Rect(800,150,500,300)
fire_rect = pygame.Rect(300,90,600,300)

#이미지 LOAD
Background = pygame.image.load('project_resources/1.png')
Background2 = pygame.image.load('project_resources/09.png')
Boss = pygame.image.load('project_resources/Boss_1.png')
Boss_Fire = pygame.image.load('project_resources/114.png')
player = pygame.image.load('project_resources/playerr.png')
missile = pygame.image.load('project_resources/m.png')
lose = pygame.image.load('project_resources/lose.png')
win = pygame.image.load('project_resources/win.png')
healthbar = pygame.image.load("project_resources/healthbar.png")
health = pygame.image.load("project_resources/health.png")

#사운드 LOAD
hit = pygame.mixer.Sound("project_resources/explode.wav")

cnt1 = 0
cnt2 = 0

Run = 1
CLK = 2
while Run:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()

    if healthvalue == 0:
        RUN = 0
        CLK = 0
        
    while cnt1<=40: #인트로 
        screen.blit(Background,(0,0))
        pygame.display.flip()
        
        screen.blit(Boss,(bosspos,61))
        pygame.display.flip()
        
        if cnt1==40:
            FPS_CLOCK.tick(1)
            
        FPS_CLOCK.tick(30)
        bosspos-=5
        cnt1+=1
        
    bosspos+=5


    while cnt2<3: # 인트로 후 진짜 시작
        cnt2+=1
        screen.blit(Background,(0,0))
        screen.blit(Boss,(bosspos,61))
        
        pygame.display.flip()
        
        FPS_CLOCK.tick(10)
        screen.fill((255,255,255))
        
        pygame.display.flip()
        
        if cnt2==3:
            FPS_CLOCK.tick(1)
        else:
            FPS_CLOCK.tick(8)
            
    screen.blit(Background2,(0,0))
    
 

            
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    

    for m in missiles:
        index = 0
        velx = math.cos(m[0])*10
        vely = math.sin(m[0])*10
        m[1] += velx 
        m[2] += vely
        if m[1]<-64 or m[1]>1022 or m[2]<-64 or m[2]>511:
            missiles.pop(index)
        index += 1
        for projectile in missiles:
            missile1 = pygame.transform.rotate(missile, 360-projectile[0]*57.29)
            screen.blit(missile1, (projectile[1], projectile[2]))

    index1 = 0
    for m in missiles:
        bullrect = pygame.Rect(missile.get_rect())
        bullrect.right = m[1]
        bullrect.top = m[2]
        
        if boss_rect.colliderect(bullrect):
            hit.play()
            missiles.pop(index1)
            healthvalue -= random.randint(5,20)
            
        index1 += 1
    
    screen.blit(healthbar, (800, 5))
    
    for health1 in range(healthvalue):
        screen.blit(health, (health1 + 803, 8))
        
    if bossfire:
        screen.blit(Boss_Fire,(226,63))
        
    else:
        screen.blit(Boss,(800,61))
    screen.blit(playerrot, playerpos1)
    
    if event.type == KEYDOWN and event.key == K_q:
        bossfire=True
        
    if event.type == KEYUP and event.key ==K_q:
        bossfire=False

    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_s:
                keys[2] = True
            if event.key == K_a:
                keys[1] = True
            elif event.key == K_d:
                keys[3] = True
                
        if event.type == KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_s:
                keys[2] = False
            if event.key == K_a:
                keys[1] = False
            elif event.key == K_d:
                keys[3] = False
                
        if event.type == QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            missiles.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

 # player 움직이기
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
        
    pygame.display.flip() #화면 전체 업데이트 

    
     # WIN / LOSE 판별
        
    if pygame.time.get_ticks() >= 30000: # lose
        Run = 0
        CLK = 1
        
    if healthvalue <= 0: # win
        Run = 0
        CLK = 0

# WIN / LOSE 출력
if CLK == 1:
    screen.blit(lose,(0, 0))
    
elif CLK == 0:
    screen.blit(win, (0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
