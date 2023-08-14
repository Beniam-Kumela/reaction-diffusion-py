# Import modules
import pygame as pg
import sys
import numpy as np
import numba as nb

# Generate random numbers for color options
nums = np.linspace(1, 8, 8)
rand_num = np.random.choice(nums)
selected_option = f"option{int(rand_num)}"

# Create start menu
def start_menu(): 
    image = pg.image.load('start_menu.png') # Load start menu  picture
    
    scaled_image = pg.transform.scale(image, (display_size, display_size)) # Scale to display size
    
    # Create performance buttons 
    button_width, button_height = 40, 20
    coral_button = pg.Rect(210, 435, button_width, button_height)
    mitosis_button = pg.Rect(270, 435, button_width + 15, button_height)
    coral_button_color = (150, 150, 150)
    mitosis_button_color = (150, 150, 150)
    
    selected = None
    
    while selected is None: # When user presses Enter, while hovering over button, start program
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if coral_button.collidepoint(pg.mouse.get_pos()):
                        feed = 0.04
                        k = 0.06
                        selected = 1 # Make sure to break function when user presses Enter
                    elif mitosis_button.collidepoint(pg.mouse.get_pos()):
                        feed = 0.0367
                        k = 0.0649
                        selected = 1
                    
        # Render all fonts, containers, and surfaces
        display_surface.fill((0, 0, 0))
        display_surface.blit(scaled_image, (0, 0))
        
        pg.draw.rect(display_surface, coral_button_color, coral_button)
        pg.draw.rect(display_surface, mitosis_button_color, mitosis_button)
        
        font = pg.font.SysFont('none', 20)
        low_button_text = font.render("Coral", True, (0, 0, 0))
        high_button_text = font.render("Mitosis", True, (0, 0, 0))
        
        display_surface.blit(low_button_text, (coral_button.centerx - button_width // 2, coral_button.centery - button_height // 2))
        display_surface.blit(high_button_text, (mitosis_button.centerx - button_width // 2, mitosis_button.centery - button_height // 2))
        
        font = pg.font.SysFont('none', 50, bold = False)
        title = font.render("Reaction Diffusion Simulator",  True, (255, 255, 255))
        display_surface.blit(title, (display_surface.get_width() / 2 - title.get_width() / 2, 10))
        
        # Render descriptive text. Note that multi-line string indicator (''') will not work so each line needs to be formatted at a time.
        font = pg.font.SysFont('none', 25)
        description1 = font.render("This a Python implementation of the Gray-Scott model.", True, (255, 255, 255))
        description2 = font.render("The program will start by rendering a box in the middle.", True, (255, 255, 255))
        description3 = font.render("This shape will then slowly diffuse into the solution.", True, (255, 255, 255))
        description4 = font.render("The following key combinations will give these shapes:", True, (255, 255, 255))
        description5 = font.render("Circle = O + left-click", True, (255, 255, 255))
        description6 = font.render("Cross = C + left-click", True, (255, 255, 255))
        description7 = font.render("Star = S + left-click", True, (255, 255, 255))
        description8 = font.render("Square = B + left-click", True, (255, 255, 255))
        description9 = font.render("The colors are chosen at random each time the program runs.", True, (255, 255, 255))
        description10 = font.render("Click one of the performance modes below", True, (255, 255, 255))
        description11 = font.render("based on your computer's capabilities:", True, (255, 255, 255))
        description12 = font.render("It should turn green if selected.", True, (255, 255, 255))
        description13 = font.render("Press 'Enter' or 'Return' while hovering over the button.", True, (255, 255, 255))

        display_surface.blit(description1, (display_surface.get_width() / 2 - description1.get_width() / 2, 90))
        display_surface.blit(description2, (display_surface.get_width() / 2 - description2.get_width() / 2, 110))
        display_surface.blit(description3, (display_surface.get_width() / 2 - description3.get_width() / 2, 130))
        display_surface.blit(description4, (display_surface.get_width() / 2 - description4.get_width() / 2, 150))
        display_surface.blit(description5, (display_surface.get_width() / 2 - description5.get_width() / 2, 170))
        display_surface.blit(description6, (display_surface.get_width() / 2 - description6.get_width() / 2, 190))
        display_surface.blit(description7, (display_surface.get_width() / 2 - description7.get_width() / 2, 210))
        display_surface.blit(description8, (display_surface.get_width() / 2 - description8.get_width() / 2, 230))
        display_surface.blit(description9, (display_surface.get_width() / 2 - description9.get_width() / 2, 270))
        display_surface.blit(description10, (display_surface.get_width() / 2 - description10.get_width() / 2, 290))
        display_surface.blit(description11, (display_surface.get_width() / 2 - description11.get_width() / 2, 310))
        display_surface.blit(description12, (display_surface.get_width() / 2 - description12.get_width() / 2, 330))
        display_surface.blit(description13, (display_surface.get_width() / 2 - description13.get_width() / 2, 350))
        

        pg.display.flip()
        clock.tick(60)
        
        # Green color when button is pressed
        if pg.mouse.get_pressed()[0]:
            if coral_button.collidepoint(pg.mouse.get_pos()):
                coral_button_color = (0, 128, 0)
                
            if mitosis_button.collidepoint(pg.mouse.get_pos()):
                mitosis_button_color = (0, 128, 0)
          
    return feed, k

# Create function for animating screen
def animate(feed, k):
    o_pressed = False
    c_pressed = False
    b_pressed = False
    s_pressed = False
    n = 128
    
    # Initialize surface and reaction diffusion starting conditions
    running = True    
    s = pg.Surface((n, n))   
    grida = np.ones((n, n))
    gridb = np.zeros((n, n))
    pixels = np.zeros((n, n, n), dtype=float)
    pixels[:, :, 0] = 1
        
    dA = 0.5
    dB = 0.25
    
    # Start with small perturbation of B in the center of the grid
    for i in range(5):
        for j in range(5):
            gridb[((n//2)+i)][((n//2)+j)] = 1
            gridb[((n//2)-i)][((n//2)-j)] = 1
            gridb[((n//2)-i)][((n//2)+j)] = 1
            gridb[((n//2)+i)][((n//2)-j)] = 1
    
    # Function to swap previous grid with calculated future grid             
    def swap(grida, gridb, pixels):        
        temp1 = np.copy(grida)
        grida = np.copy(pixels[:, :, 0])
        pixels[:, :, 0] = temp1
        
        temp2 = np.copy(gridb)
        gridb = np.copy(pixels[:, :, 1])
        pixels[:, :, 1] = temp2
        
        return grida, gridb, pixels

    # Function that uses the 5 - point stencil method to approximate the 2D discrete laplacian scaled by 1/4.
    # More information here: https://en.wikipedia.org/wiki/Discrete_Laplace_operator#Implementation_via_operator_discretization 
    def laplace(grid, x, y, n):
        sum = 0
        sum += grid[x, y] * -1
        sum += grid[(x-1) % n, y] * 0.25
        sum += grid[(x+1) % n, y] * 0.25
        sum += grid[x, (y+1) % n] * 0.25
        sum += grid[x, (y-1) % n] * 0.25
        
        return sum
    
    # The following functions give dye to selected points on grid using simple computer graphics raster algorithms.
    # Sqaure function
    def draw_box():
        x = gridx
        y = gridy
        for i in range(5):
            for j in range(5):
                gridb[(x+i) % n][(y+j) % n] = 1
                gridb[(x-i) % n][(y-j) % n] = 1
                gridb[(x-i) % n][(y+j) % n] = 1
                gridb[(x+i) % n][(y-j) % n] = 1
    
    # Simple 4 point cross function
    def draw_cross():
        x = gridx
        y = gridy
        for i in range(10):
            gridb[x][(y+i) % n] = 1
            gridb[x][(y-i) % n] = 1
            gridb[(x+i) % n][y] = 1
            gridb[(x-i) % n][y] = 1
    
    # 8 point cross function            
    def draw_star():
        x = gridx
        y = gridy
        for i in range(10):
            gridb[x][(y+i) % n] = 1
            gridb[x][(y-i) % n] = 1
            gridb[(x+i) % n][y] = 1
            gridb[(x-i) % n][y] = 1
            gridb[(x-i) % n][(y-i) % n] = 1
            gridb[(x+i) % n][(y-i) % n] = 1
            gridb[(x-i) % n][(y+i) % n] = 1
            gridb[(x+i) % n][(y+i) % n] = 1
    
    # Circle rastering using Midpoint Circle Algorithm 
    # More information here: https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#Algorithm
    def draw_circle():
        cx = gridx
        cy = gridy
        radius = 5
        x = radius
        y = 0
        decision_param = 1- radius
        
        while x >= y:
            gridb[(cx + x) % n][(cy + y) % n] = 1
            gridb[(cx + y) % n][(cy + x) % n] = 1
            gridb[(cx - y) % n][(cy + x) % n] = 1
            gridb[(cx - x) % n][(cy + y) % n] = 1
            gridb[(cx - x) % n][(cy - y) % n] = 1
            gridb[(cx - y) % n][(cy - x) % n] = 1
            gridb[(cx + y) % n][(cy - x) % n] = 1
            gridb[(cx + x) % n][(cy - y) % n] = 1
            
            if decision_param <=0:
                y += 1
                decision_param += 2 * y + 1
            
            if decision_param > 0:
                x -= 1
                decision_param -= 2 * x + 1
    
    # Scale mouse position on display surface to grid size            
    def display_to_anim(mouse_x, mouse_y):
        gridx = mouse_x * n // display_size
        gridy = mouse_y * n // display_size
        
        return gridx, gridy
                                    
    while running:
        arr = pg.surfarray.pixels3d(s)
        
        # 2D Gray-Scott Reaction Diffusion Algorithm
        # More information here: https://www.karlsims.com/rd.html
        for x in nb.prange(n):
            for y in nb.prange(n):
                a = grida[x, y]
                b = gridb[x, y]
                pixels[x, y, 0] = a + (dA * laplace(grida, x, y, n)) - (a * b * b) + (feed * (1 - a))
                pixels[x, y, 1] = b + (dB * laplace(gridb, x, y, n)) + (a * b * b) - ((k + feed) * b)
                
                # Different color mapping options
                if selected_option == "option1":
                    arr[x, y, 0] = pixels[x, y, 0] * 255
                    arr[x, y, 1] = 0
                    arr[x, y, 2] = pixels[x, y, 1] * 255
                
                if selected_option == "option2":
                    arr[x, y, 0] = pixels[x, y, 0] * 255
                    arr[x, y, 1] = pixels[x, y, 1] * 255
                    arr[x, y, 2] = 0
                
                if selected_option == "option3":
                    arr[x, y, 0] = pixels[x, y, 0] * 255
                    arr[x, y, 1] = pixels[x, y, 1] * 255
                    arr[x, y, 2] = 255
                
                if selected_option == "option4":
                    arr[x, y, 0] = 0
                    arr[x, y, 1] = pixels[x, y, 1] * 255
                    arr[x, y, 2] = pixels[x, y, 0] * 255
                
                if selected_option == "option5":
                    arr[x, y, 0] = 255
                    arr[x, y, 1] = pixels[x, y, 1] * 255
                    arr[x, y, 2] = pixels[x, y, 0] * 255
                
                if selected_option == "option6":
                    arr[x, y, 0] = pixels[x, y, 0] * 255
                    arr[x, y, 1] = pixels[x, y, 1] * 255
                    arr[x, y, 2] = pixels[x, y, 0] * 255
                
                if selected_option == "option7":
                    arr[x, y, 0] = pixels[x, y, 1] * 255
                    arr[x, y, 1] = pixels[x, y, 1] * 255
                    arr[x, y, 2] = pixels[x, y, 0] * 255
                
                if selected_option == "option8":
                    arr[x, y, 0] = pixels[x, y, 0] * 255
                    arr[x, y, 1] = pixels[x, y, 1] * 255
                    arr[x, y, 2] = pixels[x, y, 1] * 255
                
                        
        grida, gridb, pixels = swap(grida, gridb, pixels)        
        
        # Listening for key and mouse positions to draw shapes in correct locations  
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_o:
                    o_pressed = True
                if event.key == pg.K_c:
                    c_pressed = True
                if event.key == pg.K_b:
                    b_pressed = True
                if event.key == pg.K_s:
                    s_pressed = True
                              
            if event.type == pg.KEYUP:
                if event.key == pg.K_o:
                    o_pressed = False
                if event.key == pg.K_c:
                    c_pressed = False
                if event.key == pg.K_b:
                    b_pressed = False
                if event.key == pg.K_s:
                    s_pressed = False
                    
            if event.type == pg.MOUSEBUTTONDOWN and o_pressed:
                mouse_x, mouse_y = pg.mouse.get_pos()
                gridx, gridy = display_to_anim(mouse_x, mouse_y)
                draw_circle()
            
            if event.type == pg.MOUSEBUTTONDOWN and c_pressed:
                mouse_x, mouse_y = pg.mouse.get_pos()
                gridx, gridy = display_to_anim(mouse_x, mouse_y)
                draw_cross()
            
            if event.type == pg.MOUSEBUTTONDOWN and b_pressed:
                mouse_x, mouse_y = pg.mouse.get_pos()
                gridx, gridy = display_to_anim(mouse_x, mouse_y)
                draw_box()
                
            if event.type == pg.MOUSEBUTTONDOWN and s_pressed:
                mouse_x, mouse_y = pg.mouse.get_pos()
                gridx, gridy = display_to_anim(mouse_x, mouse_y)
                draw_star()
                
            if event.type == pg.QUIT:
                running = False
        
        # Scaling display size to grid size
        pg.transform.scale(s, (display_size, display_size), display_surface)                  
        pg.display.update()
        
def main():
    global display_surface, display_size, clock
    
    display_size = 512
    display_surface = pg.display.set_mode((display_size, display_size), pg.HWSURFACE | pg.DOUBLEBUF)
    pg.display.set_caption("Diffusion")
    clock = pg.time.Clock()
    
    feed, k = start_menu()

    animate(feed, k)
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()