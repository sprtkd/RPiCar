import Rpi_RC_car_control as car
import pygame
import time

#status of keys
upkey_flag=0
downkey_flag=0
leftkey_flag=0
rightkey_flag=0
pygame.init()
white=[255,255,255]
red=[255,0,0]
clock=pygame.time.Clock()
fps=30
background=pygame.display.set_mode([800,600])
pygame.display.set_caption("Car_Control")
background.fill(white)
    
    
def controller_start():
    game_exit=True
    while game_exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    car.turn_left_start()
                    leftkey_flag=1
                    if event.key==pygame.K_RIGHT:
                        car.dir_stop()
                        rightkey_flag=1
                    elif event.key==pygame.K_UP:
                        car.move_fwd_start()
                        upkey_flag=1
                    elif event.key==pygame.K_DOWN:
                        car.move_bckwd_start()
                        downkey_flag=1
                if event.key==pygame.K_RIGHT:
                    car.turn_right_start()
                    rightkey_flag=1
                    if event.key==pygame.K_LEFT:
                        car.dir_stop()
                        leftkey_flag=1
                    elif event.key==pygame.K_UP:
                        car.move_fwd_start()
                        upkey_flag=1
                    elif event.key==pygame.K_DOWN:
                        car.move_bckwd_start()
                        downkey_flag=1
                if event.key==pygame.K_UP:
                    car.move_fwd_start()
                    upkey_flag=1
                    if event.key==pygame.K_DOWN:
                        car.throttle_stop()
                        downkey_flag=1
                    elif event.key==pygame.K_LEFT:
                        car.turn_left_start()
                        leftkey_flag=1
                    elif event.key==pygame.K_RIGHT:
                        car.turn_right_start()
                        rightkey_flag=1
                if event.key==pygame.K_DOWN: 
                    car.move_bckwd_start()
                    downkey_flag=1
                    if event.key==pygame.K_UP:
                        car.throttle_stop()
                        upkey_flag=1
                    elif event.key==pygame.K_LEFT:
                        car.turn_left_start()
                        leftkey_flag=1
                    elif event.key==pygame.K_RIGHT:
                        car.turn_right_start()
                        rightkey_flag=1
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT and event.key==pygame.K_RIGHT:
                    car.dir_stop()
                    leftkey_flag=0
                    rightkey_flag=0
                if event.key==pygame.K_UP and event.key==pygame.K_DOWN:
                    car.throttle_stop()
                    upkey_flag=0
                    downkey_flag=0
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    car.car_exit()


def getkeystatus():
    return upkey_flag,downkey_flag,leftkey_flag,rightkey_flag




                    
