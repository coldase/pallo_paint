import pygame

#Sizes
screen_width = 800	#x
screen_height = 600	#y

#Colors
powderblue = (176, 224, 230)

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def main():
	pygame.init()

	main_screen = pygame.display.set_mode((screen_width, screen_height))

	pygame.display.set_caption("Pallopaint lol")

	main_screen.fill(powderblue)
	pygame.draw.circle(main_screen, red, (20,20), 20)
	pygame.draw.circle(main_screen, black, (80,20), 20)
	pygame.draw.circle(main_screen, green, (140,20), 20)
	pygame.draw.circle(main_screen, blue, (200,20), 20)
	pygame.display.update()

	current_color = red
	
	
	def draw(position, color):
		pygame.draw.circle(main_screen, (color), position, 20)

	def clear_screen():
		main_screen.fill((powderblue))

	
	run = True
	while run:
		
		pygame.time.delay(100)
		
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_SPACE:
						print("Space pressed")
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					pos = event.pos
					draw(pos, current_color)
					pygame.display.update()

				if event.button == 2:
					main_screen.fill(powderblue)
					pygame.draw.circle(main_screen, red, (20,20), 20)
					pygame.draw.circle(main_screen, black, (80,20), 20)
					pygame.draw.circle(main_screen, green, (140,20), 20)
					pygame.draw.circle(main_screen, blue, (200,20), 20)
					pygame.display.update()
				if event.button == 3:
					pos = event.pos
					print(f'x={pos[0]}, y={pos[1]}')
					if (pos[0] >= 180 and pos[0] <= 218) and (pos[1] >= 2 and pos[1] <= 39):
						current_color = blue
					if (pos[0] >= 120 and pos[0] <= 158) and (pos[1] >= 2 and pos[1] <= 39):
						current_color = green
					if (pos[0] >= 60 and pos[0] <= 98) and (pos[1] >= 2 and pos[1] <= 39):
						current_color = black
					if (pos[0] >= 0 and pos[0] <= 40) and (pos[1] >= 2 and pos[1] <= 39):
						current_color = red

	pygame.quit()

if __name__ == "__main__":
	main()