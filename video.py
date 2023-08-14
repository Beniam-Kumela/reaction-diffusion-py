# Import modules
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time
from tqdm import tqdm

# User dialogue
print('''
Welcome to the Reaction Diffusion Video Generator!
The characteristic stripes on a tiger, splotches on a cow, and organization of coral beds can be explained using the Gray-Scott reaction diffusion model.
We will intialize an NxN matrix, seed it with some chemical, and watch it diffuse across the solution.
Let's get started by initializing some conditions.
''')

# User input
n = int(input("Grid size (default 200): "))
F = float(input("Feed rate (default = 0.037): "))
k = float(input("Kill rate (default = 0.06): "))
f = int(input("How many frames? (0.05s per frame): "))
color = input("Color map? 'inferno' (black and orange) or 'winter' (blue and green): ")
print('Thank you for inputting info! This will take a while but the progress meter will let you know when it is done.')

# Initialize remaining conditions
Du = 0.1
Dv = 0.05

# Define vectorized 2D, 5-point stencil Laplcaian operator
def Laplacian(Z):
    return(Z[:-2, 1:-1] + Z[2:, 1:-1] + Z[1:-1, :-2] + Z[1:-1, 2:] - 4 * Z[1:-1, 1:-1])

# Define forward Euler method used by the Gray-Scott model
def integration(U,V):
    deltaU = Du * Laplacian(U) - U[1:-1, 1:-1] * V[1:-1, 1:-1]**2 + F * (1- U[1:-1, 1:-1])
    deltaV = Dv * Laplacian(V) + U[1:-1, 1:-1] * V[1:-1, 1:-1]**2 - (F + k) * V[1:-1, 1:-1]
    
    return deltaU, deltaV

U = np.ones((n+2, n+2))
V = np.zeros((n+2, n+2))

# Define some initial perturbations
r = 5
U[n//2-r:n//2+r, n//2-r:n//2+r] = 0.5
V[n//2-r:n//2+r, n//2-r:n//2+r] = 0.25

U += 0.05 * np.random.random((n+2, n+2))
V += 0.05 * np.random.random((n+2, n+2))

fig, ax = plt.subplots()
ax.axis('off')
im = ax.imshow(V, cmap=color, interpolation = 'bicubic', extent = [-1, 1, -1, 1])

# Animate grid function
def update(frame):
    global U, V
    for i in range (10):
        deltaU, deltaV = integration(U,V)
        U[1:-1, 1:-1] += deltaU
        V[1:-1, 1:-1] += deltaV
        U = np.clip(U, 0, 1)
        V = np.clip(V, 0, 1)
    im.set_array(V)
    return (im,)

# Save animation and let user know when it is completed
ani = FuncAnimation(fig, update, frames=tqdm(range(f), initial=1, position=0), interval=50, blit=True)
ani.save('reaction_diffusion.gif', dpi=100)
print(f"The animation was {0.05 * f} seconds long.")
print('''
Animation saved as reaction_diffusion.gif within the folder in which you installed this program.
Thank you!
''')