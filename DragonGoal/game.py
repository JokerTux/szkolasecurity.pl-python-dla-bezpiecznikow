import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('graphics/player/walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('graphics/player/walk_2.png').convert_alpha()
		player_walk_3 = pygame.image.load('graphics/player/walk_3.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2,player_walk_3]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/player/jump.png')
		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (100,400))
		self.gravity = 0

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 400:
			self.gravity = -24

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 400:
			self.rect.bottom = 400

	def animation(self):
		if self.rect.bottom < 400:
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			#print(self.player_index)
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]
				

	def update(self):
		self.player_input()
		self.apply_gravity()		
		self.animation()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		zombie_walk_1 = pygame.image.load('graphics/monsters/zombie_walk1.png').convert_alpha()
		zombie_walk_2 = pygame.image.load('graphics/monsters/zombie_walk2.png').convert_alpha()
		zombie_walk_3 = pygame.image.load('graphics/monsters/zombie_walk3.png').convert_alpha()
		zombie_walk_4 = pygame.image.load('graphics/monsters/zombie_walk4.png').convert_alpha()
		self.walk = [zombie_walk_1,zombie_walk_2,zombie_walk_3,zombie_walk_4]
		y_pos = 400

		self.animation_index = 0

		self.image = self.walk[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(1300,1550),y_pos))

	def animation(self):
		self.animation_index += 0.09
		if self.animation_index >= len(self.walk):self.animation_index = 0
		self.image = self.walk[int(self.animation_index)]

	def kill_monsters(self):
		if self.rect.x <= -100:
			self.kill()

	def update(self):
		self.animation()	
		self.rect.x -= 5.5
		self.kill_monsters()

def display_score():
	current_time = int(pygame.time.get_ticks()/1000) - start_time 
	score_surf = font.render(f'{current_time}',True,(64,64,64))
	score_rect = score_surf.get_rect(center=(500,50))
	screen.blit(score_surf,score_rect)
	return current_time
	
def collision():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else:
		return True	

pygame.init()

font = pygame.font.Font(None,80)
score = 0 
start_time = 0

#Extra event with a new Timer for the respawn of "UI"
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,randint(1500,2500))


screen = pygame.display.set_mode((1000 , 500))
pygame.display.set_caption('DragonGoal')
clock = pygame.time.Clock()
game_active = False

background = pygame.image.load('graphics/background.png').convert()

#Groups and sprites

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()
obstacle_group.add(Obstacle())

#Game loop

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	
		if event.type == obstacle_timer and game_active:
			obstacle_group.add(Obstacle())

			# print('test')
			

	if game_active:
			
		screen.blit(background,(0,0))

		#Drawning sprites		
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		game_active = collision()
		score = display_score()
	else:
		screen.fill('Blue')
		welcome = "Press space to start the game"
		welcome_msg = font.render(welcome,True,(64,64,64))
		welcome_rect = welcome_msg.get_rect(center=(500,50))

		score_msg = font.render(f'Your score:{score}',True,(255,100,100))
		score_msg_rec =score_msg.get_rect(center=(450,50)) 
		
		if score == 0:
			screen.blit(welcome_msg,welcome_rect)	
		else:
			screen.blit(score_msg,score_msg_rec)


		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			game_active = True
			start_time = int(pygame.time.get_ticks()/1000) - start_time

	
	

	pygame.display.update()
		
	clock.tick(60)

	