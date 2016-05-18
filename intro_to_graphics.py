import pygame

BLACK = (   0,   0,   0)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
WHITE = (0xFF, 0xFF, 0xFF)

PI = 3.141592653

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Kellen's Cool Game")

#Loop until the user clicks the close button
done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main program loop
while not done:
	# Main event loop
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicks close
				done = True # Flag that we are done so we exit the loop

		#--- Game logic should go here
		
		
		# Screen clearing code:
		# First clear the screen to white. Don't put other drawing commmands
		# above this or they will be erased with this command.
		screen.fill(WHITE)

		#--- Drawing code will go here 
		
		# Draw on the screen a green line from (0, 0) to (100, 100)
		# that is 5 pixels wide.
		pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

		# Draw more lines
		pygame.draw.line(screen, RED, [10, 50], [1000, 600], 40)
		pygame.draw.line(screen, BLACK, [500, 60], [320, 340], 10)
		pygame.draw.line(screen, GREEN, [45, 100], [450, 1], 15)
		pygame.draw.rect(screen, BLACK, [55, 50, 20, 25])
		pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

		# Draw on the screen several lines from (0,10) to (100,110)
		# 5 pixels wide using a for loop
		for y_offset in range(100, 200, 20): 
			pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset], 5)

		# Draw x's to the screen
		for x_offset in range(100, 400, 50):
			pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90], 2)
			pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100], 2)

		# Draw a rectangle to the screen
		pygame.draw.rect(screen, GREEN, [100, 100, 50, 25], 10)

		# Draw an ellipse to the screen
		pygame.draw.ellipse(screen, BLACK, [250, 250, 100, 100], 2)

		# Draw multiple arcs in different quadrants of an ellipse
		pygame.draw.arc(screen, GREEN, [100, 100, 250, 200], PI / 2, PI, 2)
		pygame.draw.arc(screen, RED, [100, 100, 250, 200], 0, PI / 2, 2)
		pygame.draw.arc(screen, BLACK, [100, 100, 250, 200], 3*PI / 2, 2* PI, 2)
		pygame.draw.arc(screen, RED, [100, 100, 250, 200], PI, 3*PI / 2, 2)

		# Draw a polygon
		pygame.draw.polygon(screen, BLACK, [[200, 200], [300, 100], [15, 5]], 6)

		# Drawing text to the screen
		# Select the font to use, size, bold, italic
		font = pygame.font.SysFont('Arial', 60, False, False)

		# Render the text. "True" means anti-aliased text.
		# Black is the color. The variable "BLACK" was defined earlier
		# at the top of the program.
		# Note: This line creates an image of the letters,
		# but does not put the image of letters on screen yet
		text = font.render("My text", True, BLACK) 

		# Put the image of the text on the screen at 250 x 250
		screen.blit(text, [250, 250])
		
		# Update the screen with what I have drawn
		pygame.display.flip()

		# Limit to 60 frames per second
		clock.tick(60) 


pygame.quit()