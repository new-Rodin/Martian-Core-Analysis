import pygame
import math

# Initialize Pygame
pygame.init()

# Parameters
screen_size = 800  # Screen size in pixels
planet_radius = 3390  # Radius of Mars (in km)
core_radius = 1830    # Core radius (in km)
geo_center = (400, 400)  # Screen center
s_wave_speed = 5        # S-wavefront speed (in km per frame)
p_wave_speed = 8        # P-wavefront speed (in km per frame)
p_wave_speed_core = p_wave_speed * 0.75  # Slowed speed in core
scale_factor = 400 / planet_radius  # Scale to fit the screen
fps = 60  # Frames per second

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
cyan = (0, 255, 255)  # S-wavefront color
yellow = (255, 255, 0)  # P-wavefront color
orange = (255, 165, 0)  # P-wavefront in core color

# Initialize screen
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Seismic Wave Propagation")
clock = pygame.time.Clock()

# Function to draw the planet and core
def draw_planet():
    pygame.draw.circle(screen, white, geo_center, int(planet_radius * scale_factor), 2)
    pygame.draw.circle(screen, red, geo_center, int(core_radius * scale_factor), 2)

# Function to draw the S-wavefront (visible only in the mantle)
def draw_s_wavefront(radius, hypocenter):
    angle_steps = 500
    for angle in range(angle_steps):
        theta = 2 * math.pi * angle / angle_steps
        x_wave = int(radius * math.cos(theta) + hypocenter[0])
        y_wave = int(radius * math.sin(theta) + hypocenter[1])

        # Calculate distance from planet's center to determine visibility
        distance_from_center = math.sqrt((x_wave - geo_center[0])**2 + (y_wave - geo_center[1])**2)

        # Only draw wavefront in the mantle region
        if core_radius * scale_factor <= distance_from_center <= planet_radius * scale_factor:
            pygame.draw.circle(screen, cyan, (x_wave, y_wave), 1)

# Function to draw the P-wavefront (restricted and slowed in the core - visual change)
# Function to draw the P-wavefront (restricted and slowed in the core - visual change)
def draw_p_wavefront(radius, hypocenter):
    angle_steps = 500
    for angle in range(angle_steps):
        theta = 2 * math.pi * angle / angle_steps
        x_wave_Mantle = int(radius * math.cos(theta) + hypocenter[0])
        y_wave_Mantle = int(radius * math.sin(theta) + hypocenter[1])

        # Calculate distance from planet's center for the *mantle* wave position
        distance_from_center = math.sqrt((x_wave_Mantle - geo_center[0])**2 + (y_wave_Mantle - geo_center[1])**2)

        # Only draw wavefront within the planet
        if distance_from_center <= planet_radius * scale_factor:
            # Check if the *mantle wave position* is in the core
            if distance_from_center <= core_radius * scale_factor:
                # Calculate 'slowed down' radius for core region visualization
                slowed_radius_factor = p_wave_speed_core / p_wave_speed
                core_radius_effect = radius * slowed_radius_factor # Scale down radius to represent slower wave
                x_wave_Core = int(core_radius_effect * math.cos(theta) + hypocenter[0])
                y_wave_Core = int(core_radius_effect * math.sin(theta) + hypocenter[1])
                pygame.draw.circle(screen, orange, (x_wave_Core, y_wave_Core), 1) # Draw inner 'slowed' part in orange

                # Optional: Keep the yellow outline - can comment out if you only want to see core effect
                # pygame.draw.circle(screen, yellow, (x_wave_Mantle, y_wave_Mantle), 1)

            else: # Mantle wave position is outside the core (but still within planet)
                pygame.draw.circle(screen, yellow, (x_wave_Mantle, y_wave_Mantle), 1)
# Main loop
running = True
wavefronts = dict()  # List to store all active hypocenters and their wavefront radii
c = 0 # Initialize hypocenter counter outside the loop


while running:
    screen.fill(black)  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect mouse click to add a new hypocenter
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = pygame.mouse.get_pos()

            # Check if the click is inside the planet's radius
            distance_from_center = math.sqrt((click_position[0] - geo_center[0])**2 + (click_position[1] - geo_center[1])**2)
            if distance_from_center <= planet_radius * scale_factor:
                # Add new hypocenter: store the position and initial S and P radii
                wavefronts[c]={'hypocenter': click_position, 's_radius': 0, 'p_radius': 0}
                c+=1

    # Draw planet and core
    draw_planet()

    # Update and draw wavefronts for all hypocenters
    for c_key in list(wavefronts.keys()): # Iterate using keys to avoid issues after deletion
        if c_key not in wavefronts: # Check if the key still exists after potential deletion in the loop
            continue

        wave = wavefronts[c_key]
        hypocenter = wave['hypocenter']
        s_radius = wave['s_radius']
        p_radius = wave['p_radius']

        draw_s_wavefront(s_radius, hypocenter)
        draw_p_wavefront(p_radius, hypocenter)

        # Update S-wavefront radius
        wave['s_radius'] += s_wave_speed * scale_factor

        # Update P-wavefront radius
        wave['p_radius'] += p_wave_speed * scale_factor

        # Stop wavefronts if they exceed the planet's edge (increased limit for visual effect)
        if wave['s_radius'] > 2 * planet_radius * scale_factor: # Increased limit
            del wavefronts[c_key]
        if wave['p_radius'] > 2 * planet_radius * scale_factor: # Increased limit
            del wavefronts[c_key]

    # Refresh screen
    pygame.display.flip()
    clock.tick(fps)

# Quit Pygame
pygame.quit()