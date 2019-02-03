import Rpi_RC_car_control as control
import pygame
import time

#status of keys
upkey_flag=0
downkey_flag=0
leftkey_flag=0
rightkey_flag=0
filename1='up.jpg'
filename2='down.png'
filename3='left.png'
filename4='right.jpg'
pygame.init()
white=[255,255,255]
red=[255,0,0]
clock=pygame.time.Clock()
fps=30
background=pygame.display.set_mode([800,600])
pygame.display.set_caption("Car_Control")
def controller_start():
    game_exit=True
    while game_exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    turn_left_start()
                    img1=pygame.image.load(filename3)
                    background.blit(img1,[200,200])
                    background.display.update()
                    leftkey_flag=1
                    if event.key==pygame.K_RIGHT:
                        dir_stop()
                        img2=pygame.image.load(filename4)
                        background.blit(img2,[400,400])
                        background.display.update()
                        rightkey_flag=1
                    elif event.key==pygame.K_UP:
                        move_fwd_start()
                        img3=pygame.image.load(filename1)
                        background.blit(img3,[400,400])
                        background.display.update()
                        upkey_flag=1
                    elif event.key==pygame.K_DOWN:
                        move_bckwd_start()
                        img4=pygame.image.load(filename2)
                        background.blit(img4,[400,400])
                        background.display.update()
                        downkey_flag=1
                if event.key==pygame.K_RIGHT:
                    turn_right_start()
                    img2=pygame.image.load(filename4)
                    background.blit(img2,[200,200])
                    background.display.update()
                    rightkey_flag=1
                    if event.key==pygame.K_LEFT:
                        dir_stop()
                        img1=pygame.image.load(filename3)
                        background.blit(img1,[400,400])
                        background.display.update()
                        leftkey_flag=1
                    elif event.key==pygame.K_UP:
                        control.move_fwd_start()
                        img3=pygame.image.load(filename1)
                        background.blit(img3,[400,400])
                        background.display.update()
                        upkey_flag=1
                    elif event.key==pygame.K_DOWN:
                        move_bckwd_start()
                        img4=pygame.image.load(filename2)
                        background.blit(img4,[400,400])
                        background.display.update()
                        downkey_flag=1
                if event.key==pygame.K_UP:
                    move_fwd_start()
                    img3=pygame.image.load(filename1)
                    background.blit(img3,[200,200])
                    background.display.update()
                    upkey_flag=1
                    if event.key==pygame.K_DOWN:
                        throttle_stop()
                        img4=pygame.image.load(filename2)
                        background.blit(img4,[400,400])
                        background.display.update()
                        downkey_flag=1
                    elif event.key==pygame.K_LEFT:
                        turn_left_start()
                        img1=pygame.image.load(filename3)
                        background.blit(img1,[400,400])
                        background.display.update()
                        leftkey_flag=1
                    elif event.key==pygame.K_RIGHT:
                        turn_right_start()
                        img2=pygame.image.load(filename4)
                        background.blit(img2,[400,400])
                        background.display.update()
                        rightkey_flag=1
                if event.key==pygame.K_DOWN: 
                    move_bckwd_start()
                    img4=pygame.image.load(filename2)
                    background.blit(img4,[200,200])
                    background.display.update()
                    downkey_flag=1
                    if event.key==pygame.K_UP:
                        throttle_stop()
                        img3=pygame.image.load(filename1)
                        background.blit(img3,[400,400])
                        background.display.update()
                        upkey_flag=1
                    elif event.key==pygame.K_LEFT:
                        turn_left_start()
                        img1=pygame.image.load(filename3)
                        background.blit(img1,[400,400])
                        background.display.update()
                        leftkey_flag=1
                    elif event.key==pygame.K_RIGHT:
                        turn_right_start()
                        img2=pygame.image.load(filename4)
                        background.blit(img2,[400,400])
                        background.display.update()
                        rightkey_flag=1
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT and event.key==pygame.K_RIGHT:
                    dir_stop()
                    img1=pygame.image.load(filename3)
                    background.blit(img1,[200,300])
                    background.display.update()
                    time.sleep(2)
                    leftkey_flag=0
                    img2=pygame.image.load(filename4)
                    background.blit(img2,[200,300])
                    background.display.update()
                    time.sleep(2)
                    rightkey_flag=0
                if event.key==pygame.K_UP and event.key==pygame.K_DOWN:
                    control.throttle_stop()
                    img3=pygame.image.load(filename1)
                    background.blit(img3,[200,300])
                    background.display.update()
                    time.sleep(2)
                    upkey_flag=0
                    img4=pygame.image.load(filename2)
                    background.blit(img4,[200,300])
                    background.display.update()
                    downkey_flag=0
        background.fill(white)            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()







                    
