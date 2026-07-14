import pygame
pygame.init()
font = pygame.font.SysFont('Colibri', 80)
version_font = pygame.font.SysFont('Times New Roman', 30)

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 102, 102)
colors = [red, green, blue, white, black, pink]

cell_size = 60
screen_size = (800, 600)
selected_color = font.render('>', True, white)
version = version_font.render('paint v.0.3', True, white)
current_color = (255,255,255)
screen = pygame.display.set_mode(screen_size)
grid = [[(0,0,0) for _ in range(8)] for _ in range(8)]

clock = pygame.time.Clock()
running  = True

while running:

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #events updates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        row = mouse_x // cell_size
        col = mouse_y // cell_size

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка
                if 0 <= col <= 7 and 0 <= row <= 7:
                    grid[row][col] = current_color
                elif 12 <= row <= 13 and 0 <= col  <= 5:
                    current_color = colors[col]
                pass
    # рисовать


    #screen and others

    #back
    screen.fill((0,35,100))
    #hud
    k = 0
    for row in grid:
        m = 0
        for el in row:

            pygame.draw.rect(screen, el, pygame.Rect(k*cell_size, m*cell_size, cell_size,cell_size))
            m+=1
        k+=1
    #squares with color
    for k in range(6):
        pygame.draw.rect(screen, colors[k], pygame.Rect(800-cell_size, k*cell_size,cell_size,cell_size))
        pygame.draw.rect(screen, white, pygame.Rect(800-cell_size, k*cell_size, cell_size,cell_size), 2)

    #selected color
    #61
    selected_seg_y = -5
    for color in colors:
        if current_color == color:
            break
        selected_seg_y += 61
    screen.blit(selected_color, (700, selected_seg_y))
    #version
    screen.blit(version, (10, 565))
    #clock etc.
    pygame.display.flip()
    clock.tick(cell_size)