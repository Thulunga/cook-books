
import pygame
import random
import sys


def get_new_position(pos,vel):
     return(pos[0] + vel[0], pos[1] + vel[1])


pygame.init()
WHITE = (255,255,255)
RED =  (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (900, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BLACK)
ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
ball_radius = 20
ball = pygame.draw.circle(screen, RED, ball_centre, ball_radius)

PADDLE_LENGTH = 100
PADDLE_WIDTH = 15

paddle_1_top = (4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle_1_bottom = (4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
paddle1 = pygame.draw.line(screen, GREEN, paddle_1_top, paddle_1_bottom, PADDLE_WIDTH)


paddle_2_top = (896, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle_2_bottom = (896, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))
paddle2 = pygame.draw.line(screen, GREEN, paddle_2_top, paddle_2_bottom, PADDLE_WIDTH)


boundary_1_top = (9,0)
boundary_1_bottom =(9,600)
boundary1 = pygame.draw.line(screen, WHITE,boundary_1_top, boundary_1_bottom )


boundary_2_top = (891,0)
boundary_2_bottom =(891,600)
boundary2 = pygame.draw.line(screen, WHITE,boundary_2_top, boundary_2_bottom )

ball_velocity = (1,random.choice(range(-10,10)))
print ball_velocity
paddle1_velocity = (0,0)
paddle2_velocity = (0,0)

while True:
   screen.fill(BLACK)
   pygame.time.Clock().tick(100)
   ball_centre = get_new_position(ball_centre, ball_velocity)
 
   paddle1 = pygame.draw.line(screen, GREEN, paddle_1_top, paddle_1_bottom, PADDLE_WIDTH)

 
   paddle2 = pygame.draw.line(screen, GREEN, paddle_2_top, paddle_2_bottom, PADDLE_WIDTH)
   ball = pygame.draw.circle(screen, RED, ball_centre, ball_radius)

   boundary1 = pygame.draw.line(screen, WHITE,boundary_1_top, boundary_1_bottom )

   boundary2 = pygame.draw.line(screen, WHITE,boundary_2_top, boundary_2_bottom )

   if  (ball_centre[1] + ball_radius > SCREEN_HEIGHT or ball_centre[1]-ball_radius < 0):
       ball_velocity= (ball_velocity[0], -ball_velocity[1])

   if  (ball_centre[0] + ball_radius > SCREEN_WIDTH or ball_centre[0]-ball_radius < 0):
       ball_velocity= (-ball_velocity[0], ball_velocity[1])


   for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

     elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
		  paddle2_velocity = (0,-3)   
        elif event.key == pygame.K_DOWN:
		  paddle2_velocity = (0,3)
        elif event.key == pygame.K_w:
		  paddle1_velocity = (0,-3)   
        elif event.key == pygame.K_s:
		  paddle1_velocity = (0,3)


     elif event.type == pygame.KEYUP:
	    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
		   paddle2_velocity = (0,0)

	    elif event.key == pygame.K_w or event.key == pygame.K_s:
	 	   paddle1_velocity = (0,0)
     
       
   p2_new_top = get_new_position(paddle_2_top, paddle2_velocity)
   p2_new_bottom = get_new_position(paddle_2_bottom, paddle2_velocity)

   p1_new_top = get_new_position(paddle_1_top, paddle1_velocity)
   p1_new_bottom = get_new_position(paddle_1_bottom, paddle1_velocity)

   if (p2_new_top[1] > 0 and p2_new_bottom[1] < SCREEN_HEIGHT):
		 
		paddle_2_top = p2_new_top
		paddle_2_bottom = p2_new_bottom

   if (p1_new_top[1] > 0 and p1_new_bottom[1] < SCREEN_HEIGHT):
		paddle_1_top = p1_new_top
		paddle_1_bottom = p1_new_bottom

   if ball_centre[0] + ball_radius > boundary_2_top[0]:
	if (paddle_2_top[1] < ball_centre[1]
		and paddle_2_bottom[1] > ball_centre[1]):
		ball_velocity = (-ball_velocity[0], ball_velocity[1])
	else:
		ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
		ball_velocity = (-1, random.choice(range(-10, 10)))


  
   if ball_centre[0] - ball_radius < boundary_1_top[0]:
	if (paddle_1_top[1] < ball_centre[1]
		and paddle_1_bottom[1] > ball_centre[1]):
		ball_velocity = (-ball_velocity[0], ball_velocity[1])
	else:
		ball_centre = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
		ball_velocity = (1, random.choice(range(-10, 10)))


   

  
        
        
   
   pygame.display.update()
